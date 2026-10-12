#!/usr/bin/env python3
"""Convert Platane/snk v3 SVG timelines into a self-contained electrical surge."""
import argparse
import bisect
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def node(tag, attrs=None):
    return ET.Element(f'{{{NS}}}{tag}', attrs or {})


def convert(source, dark=False):
    root = ET.fromstring(source)
    if root.get('data-electric-surge'):
        return source
    style = root.find(f'{{{NS}}}style')
    if style is None:
        raise ValueError('Missing snk stylesheet')
    css = style.text or ''
    duration = re.search(r'animation:none\s+(\d+)ms', css)
    if not duration:
        raise ValueError('Unsupported snk duration')
    duration = int(duration[1])
    spike = 50 / duration * 100
    hits = []

    def flash(match):
        name, before, level, after = match.groups()
        hit = (float(before) + float(after)) / 2
        end = hit + spike
        if end >= 100:
            raise ValueError('Flash overlaps loop boundary')
        hits.append(hit)
        return (f'@keyframes {name}' + '{' +
                f'0%,{hit:.8f}%{{fill:var(--{level});animation-timing-function:steps(1,end)}}'
                f'{hit + 0.000001:.8f}%{{fill:#FFFFFF;filter:drop-shadow(0 0 4px #FFF7A0);animation-timing-function:steps(1,end)}}'
                f'{end:.8f}%,100%{{fill:var(--ce);filter:none}}' + '}')

    css, count = re.subn(
        r'@keyframes (c[\da-z]+)\{([\d.]+)%\{fill:var\(--(c\d+)\)\}'
        r'([\d.]+)%,100%\{fill:var\(--ce\)\}\}', flash, css)
    cells = [e for e in root if 'c' in e.get('class', '').split()]
    active = [e for e in cells if len(e.get('class').split()) > 1]
    if count != len(active):
        raise ValueError('Unsupported snk cell timeline; refusing partial conversion')

    segments = [e for e in root if 's' in e.get('class', '').split()]
    segments.sort(key=lambda e: int(e.get('class').split()[1][1:], 36))
    if len(segments) < 2:
        raise ValueError('Missing snk movement segments')
    tracks = []
    for segment in segments:
        name = segment.get('class').split()[1]
        match = re.search(r'@keyframes ' + name + r'\{((?:[^{}]*\{[^{}]*\})+)\}', css)
        if not match:
            raise ValueError(f'Missing movement timeline: {name}')
        track = {}
        for times, x, y in re.findall(r'([\d.% ,]+)\{transform:translate\(([-\d.]+)px,([-\d.]+)px\)\}', match[1]):
            for time in times.split(','):
                track[float(time.strip().rstrip('%'))] = (float(x) + 8, float(y) + 8)
        if 0 not in track:
            initial = re.search(r'\.s\.' + name + r'\{transform:translate\(([-\d.]+)px,([-\d.]+)px\)', css)
            if not initial:
                raise ValueError('Missing initial movement position')
            track[0] = (float(initial[1]) + 8, float(initial[2]) + 8)
        track[100] = track[0]
        tracks.append(sorted(track.items()))

    def position(track, time):
        i = bisect.bisect_right([p[0] for p in track], time) - 1
        t, a = track[i]
        if i == len(track) - 1:
            return a
        next_t, b = track[i + 1]
        ratio = (time - t) / (next_t - t)
        return tuple(a[j] + (b[j] - a[j]) * ratio for j in (0, 1))

    defs = node('defs')
    root.insert(0, defs)
    # Each connector has its own longitudinal gradient, including at turns.
    colors = ['#FFE600', '#00F5FF', '#3b1566']
    def color(t):
        index = min(int(t * 2), 1)
        ratio = t * 2 - index
        a, b = colors[index:index + 2]
        return '#' + ''.join(f'{round(int(a[k:k+2],16)*(1-ratio)+int(b[k:k+2],16)*ratio):02x}' for k in (1,3,5))

    arc_group = node('g', {'class': 'plasma'})
    root.insert(list(root).index(segments[0]), arc_group)
    for i in reversed(range(len(tracks) - 1)):
        times = sorted({t for track in tracks[i:i+2] for t, _ in track})
        gradient = node('linearGradient', {'id': f'arc-{i}', 'gradientUnits': 'userSpaceOnUse'})
        for offset, value in [('0%', color(i/(len(tracks)-1))), ('100%', color((i+1)/(len(tracks)-1)))]:
            gradient.append(node('stop', {'offset': offset, 'stop-color': value}))
        defs.append(gradient)
        points = []
        endpoints = [[], [], [], []]
        for time in times:
            a, b = position(tracks[i], time), position(tracks[i+1], time)
            dx, dy = b[0]-a[0], b[1]-a[1]
            length = math.hypot(dx, dy) or 1
            nx, ny = -dy/length, dx/length
            width = 3.3 * (1-i/(len(tracks)-1))
            tail = 3.3 * (1-(i+1)/(len(tracks)-1)) + .15
            mx, my = (a[0]+b[0])/2 + nx*2.6, (a[1]+b[1])/2 + ny*2.6
            vertices = [(a[0]+nx*width,a[1]+ny*width), (mx+nx*width,my+ny*width),
                        (b[0]+nx*tail,b[1]+ny*tail), (b[0]-nx*tail,b[1]-ny*tail),
                        (mx-nx*width,my-ny*width), (a[0]-nx*width,a[1]-ny*width)]
            points.append(' '.join(f'{x:.2f},{y:.2f}' for x,y in vertices))
            for values, value in zip(endpoints, (*a,*b)):
                values.append(f'{value:.3f}')
        timing = {'dur': f'{duration}ms', 'repeatCount': 'indefinite', 'calcMode': 'linear',
                  'keyTimes': ';'.join(f'{t/100:.8f}' for t in times)}
        for attr, values in zip(('x1','y1','x2','y2'), endpoints):
            gradient.set(attr, values[0])
            gradient.append(node('animate', dict(timing, attributeName=attr, values=';'.join(values))))
        polygon = node('polygon', {'points': points[0], 'fill': f'url(#arc-{i})'})
        polygon.append(node('animate', dict(timing, attributeName='points', values=';'.join(points))))
        arc_group.append(polygon)

    head = node('g', {'class': segments[0].get('class')})
    # A compact plasma tip follows the direction of travel and joins the arc
    # at its center. Keep rotation separate from snk's translation animation.
    halo = node('radialGradient', {'id': 'leader-halo'})
    for offset, color_value, opacity in [('0%', '#FFFDE0', '0.8'),
                                          ('35%', '#FFE600', '0.35'),
                                          ('100%', '#FFE600', '0')]:
        halo.append(node('stop', {'offset': offset, 'stop-color': color_value,
                                 'stop-opacity': opacity}))
    defs.append(halo)
    center = node('g', {'transform': 'translate(8 8)'})
    leader = node('g', {'class': 'leader'})
    tip = node('g')
    angles = []
    for index, (time, point) in enumerate(tracks[0][:-1]):
        following = tracks[0][index + 1][1]
        dx, dy = following[0] - point[0], following[1] - point[1]
        angle = math.degrees(math.atan2(dy, dx)) if dx or dy else (angles[-1] if angles else 0)
        angles.append(angle)
    angles.append(angles[0])
    tip.set('transform', f'rotate({angles[0]})')
    tip.append(node('animateTransform', {
        'attributeName': 'transform', 'type': 'rotate', 'calcMode': 'discrete',
        'dur': f'{duration}ms', 'repeatCount': 'indefinite',
        'keyTimes': ';'.join(f'{t / 100:.8f}' for t, _ in tracks[0]),
        'values': ';'.join(f'{angle:.3f}' for angle in angles)}))
    tip.append(node('ellipse', {'cx': '0', 'cy': '0', 'rx': '9', 'ry': '6',
                                'fill': 'url(#leader-halo)'}))
    tip.append(node('path', {'d': 'M 7,0 Q 0,-4.5 -6,-2.4 L -3,0 L -6,2.4 Q 0,4.5 7,0 Z',
                             'fill': '#FFE600', 'fill-opacity': '.85'}))
    tip.append(node('path', {'d': 'M 6,0 Q 0,-2.3 -4,0 Q 0,2.3 6,0 Z',
                             'fill': '#FFFDE8'}))
    leader.append(tip)
    center.append(leader)
    head.append(center)
    for segment in segments:
        root.remove(segment)
    root.append(head)
    # Replace stacked level counters with one cell-count capacitor timeline.
    bars = [e for e in root if 'u' in e.get('class','').split()]
    if not bars:
        raise ValueError('Missing capacitor geometry')
    x = min(float(e.get('x','0')) for e in bars)
    width = max(float(e.get('x','0'))+float(e.get('width')) for e in bars)-x
    y = bars[0].get('y','0')
    height = bars[0].get('height','10')
    for bar in bars:
        root.remove(bar)
    root.append(node('rect', {'x':str(x),'y':y,'width':str(width),'height':height,'rx':'2','fill':'var(--ce)','stroke':'#00F5FF','stroke-width':'.6'}))
    bar = node('rect', {'x':str(x),'y':y,'width':'0','height':height,'rx':'2','fill':'#FFE600'})
    sorted_hits = sorted(hits)
    if sorted_hits:
        bar.append(node('animate', {'attributeName':'width','dur':f'{duration}ms','repeatCount':'indefinite','calcMode':'discrete',
                                   'keyTimes':';'.join(['0']+[f'{t/100:.8f}' for t in sorted_hits]+['1']),
                                   'values':';'.join(['0']+[f'{width*(i+1)/len(hits):.4f}' for i in range(len(hits))]+[str(width)])}))
    root.append(bar)
    palette = ('#161b22','#3b1566','#7928ca','#00d2ff','#ffe600') if dark else ('#ebedf0','#ded2f2','#ad7bd9','#008d9a','#9b7400')
    css += ':root{' + ';'.join(f'--c{i}:{v}' for i,v in enumerate(palette)) + f';--ce:{palette[0]}' + '}'
    css += '''.plasma{filter:drop-shadow(0 0 3px #00F5FF)}
.leader{filter:drop-shadow(0 0 4px #FFE600);animation:surge-flicker 83ms steps(1,end) infinite}
@keyframes surge-flicker{0%,100%{opacity:1}35%{opacity:.78}70%{opacity:.94}}
@media(prefers-reduced-motion:reduce){.leader{animation:none}}
'''
    style.text = css
    root.set('data-electric-surge', '1')
    desc = root.find(f'{{{NS}}}desc')
    if desc is not None:
        desc.text = 'Electric Grid Surge: 50 ms cell discharge, plasma arcs, lightning leader and capacitor. Route generated with https://github.com/Platane/snk.'
    return ET.tostring(root, encoding='unicode')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    # Validate all inputs before replacing either theme.
    results = [(path, convert(path.read_text(), dark="dark" in path.stem)) for path in args.files]
    for path, result in results:
        path.write_text(result)
        print(f'Electric surge: {path} ({len(result):,} bytes)')


if __name__ == '__main__':
    main()
