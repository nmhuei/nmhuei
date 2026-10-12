# Electric Grid Surge

Run after `Platane/snk/svg-only@v3`:

```sh
python3 scripts/electric_surge.py dist/github-contribution-grid-snake.svg dist/github-contribution-grid-snake-dark.svg
```

The script uses only the Python standard library. A filename containing `dark`
selects the dark palette. The workflow keeps the existing profile image URLs.

- Each active cell keeps its original hit time, flashes white for 50 ms, then
  switches to the empty-cell color. CSS uses discrete transitions for the flash.
- The leader is a compact plasma tip that turns with the route. A warm white
  core, tapered yellow shell, and soft halo connect it to the arc. Its 83 ms
  flicker varies opacity subtly, from 78% to 100%.
- Adjacent route segments define connected plasma polygons. Their width and
  color decay from yellow through cyan to purple. SVG animation moves the
  vertices and gradient endpoints together, including through route turns.
- The capacitor fills in equal steps per discharged cell and resets each loop.

The output contains no JavaScript or external assets. Movement uses the original
snk CSS timeline; plasma and capacitor use SVG declarative animation. Reduced
motion disables the rapid leader flicker. Unsupported snk cell or movement
formats fail the workflow before publication. Reprocessing an output is a no-op.

To inspect an output, open the SVG in a browser, or embed it with an HTML `img`
element. Static image converters do not show the animation.
