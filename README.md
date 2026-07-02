<div align="center">

# 👋 Xin chào, I'm Huei

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&duration=3000&pause=800&color=39FF14&center=true&vCenter=true&width=600&lines=AI+%26+Cyber+Security+Student;Reverse+Engineer;Rust+%26+Systems+Builder;Learning+by+Shipping;Decrypting+Complexity" alt="Typing SVG" />

<a href="https://github.com/nmhuei">
  <img src="https://img.shields.io/github/followers/nmhuei?style=social&logo=github" alt="GitHub followers" />
</a>
<a href="https://github.com/nmhuei">
  <img src="https://img.shields.io/github/stars/nmhuei?style=social&logo=github&label=Total%20Stars" alt="GitHub stars" />
</a>

[![Profile Views](https://komarev.com/ghpvc/?username=nmhuei&color=39FF14&style=flat-square&label=Profile+Views)](https://github.com/nmhuei)

---

### 🧠 System Architecture

```mermaid

%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '14px', 'primaryColor': '#1a1a2e', 'secondaryColor': '#16213e', 'tertiaryColor': '#0f3460', 'lineColor': '#e94560' }}}%%

graph TB
    subgraph Core["🧑‍💻 nmhuei"]
        direction LR
        R[Rust<br/>Systems] 
        P[Python<br/>AI/Agent]
        CPP[C++20<br/>Infra]
    end

    subgraph AI["🤖 AI Layer"]
        OC[opencode2claude<br/>Bridge 50+ LLMs]
        BQ[botquanganh_mcp<br/>CTF Solver Agent]
        AQA[ai-quick-ask<br/>Ollama Chrome Ext]
    end

    subgraph SEC["🛡️ Security Layer"]
        MCP[MCP Ecosystem<br/>Tool Integration]
        RE[Reverse Engineering<br/>IDA / Ghidra / r2]
        CTF[CTF Challenges<br/>Pwn / Web / Crypto]
    end

    subgraph APPS["📱 Applications"]
        MON[monitor<br/>Distributed System TUI]
        NONO[nonograms<br/>Auto-Solver]
        EMAIL[email_blaster<br/>CLI Mailer]
    end

    AI -->|MCP Protocol| MCP
    SEC -->|Automated| CTF
    AI -->|Infrastructure| Core
    APPS -->|Built With| Core

    style Core fill:#16213e,color:#fff,stroke:#0f3460
    style AI fill:#1a1a2e,color:#fff,stroke:#e94560
    style SEC fill:#1a1a2e,color:#fff,stroke:#39FF14
    style APPS fill:#16213e,color:#fff,stroke:#0f3460
```

</div>

---

## ⚡ About Me

> *"Decrypting complexity, automating the future."*

<div align="center">
  <table>
    <tr>
      <td align="center">📍 <b>Location</b></td>
      <td>Cầu Giấy, Hà Nội, Vietnam</td>
      <td align="center">🎯 <b>Focus</b></td>
      <td><b>AI & Cyber Security</b> intersection</td>
    </tr>
    <tr>
      <td align="center">🌱 <b>Philosophy</b></td>
      <td colspan="3">"Learning by shipping" — building real things to master complex systems</td>
    </tr>
    <tr>
      <td align="center">🔧 <b>Stack</b></td>
      <td colspan="3">
        <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++" />
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
        <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" />
      </td>
    </tr>
  </table>
</div>

---

## 🚀 Featured Projects

### AI & Cyber Security (MCP Tools)

<table>
  <tr>
    <td width="33%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/botquanganh_mcp">
          <img src="https://img.shields.io/badge/botquanganh__mcp-FF6B35?style=for-the-badge&logo=python&logoColor=white" /><br/>
          🛡️ MCP CTF Solver
        </a>
      </h3>
      <p align="center">
        An advanced MCP server enabling AI agents to autonomously solve CTF challenges (pwn/web).<br/><br/>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python" />
        <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker" />
        <img src="https://img.shields.io/badge/MCP-000?style=flat-square" />
      </p>
    </td>
    <td width="34%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/chatCLI">
          <img src="https://img.shields.io/badge/chatCLI-FF6B35?style=for-the-badge&logo=rust&logoColor=white" /><br/>
          💬 Decentralized Chat TUI
        </a>
      </h3>
      <p align="center">
        A decentralized terminal chat client in <b>Rust</b> with end-to-end encryption (DH + AES-256-GCM), UPnP port forwarding, and MCP integration.<br/><br/>
        <img src="https://img.shields.io/badge/Rust-000?style=flat-square&logo=rust" />
        <img src="https://img.shields.io/badge/ratatui-000?style=flat-square" />
        <img src="https://img.shields.io/badge/AES--256--GCM-000?style=flat-square" />
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/opencode2claude">
          <img src="https://img.shields.io/badge/opencode2claude-FF6B35?style=for-the-badge&logo=rust&logoColor=white" /><br/>
          🌉 LLM Bridge
        </a>
      </h3>
      <p align="center">
        Use Claude Code with <b>50+ LLMs</b>. Features WARP proxy pool, token estimation, casing resolution. Single ~5MB binary.<br/><br/>
        <img src="https://img.shields.io/badge/Rust-000?style=flat-square&logo=rust" />
        <img src="https://img.shields.io/crates/v/opencode2claude?style=flat-square" />
        <img src="https://img.shields.io/badge/WARP-000?style=flat-square" />
      </p>
    </td>
  </tr>
</table>

### Infrastructure & Automation

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/monitor">
          🖥️ <b>Distributed System Monitor</b>
        </a>
      </h3>
      <p align="center">
        <b>C++20</b> distributed monitoring platform with ncursesw TUI, Prometheus integration, and real-time CPU/RAM/Disk/Network metrics.<br/><br/>
        <img src="https://img.shields.io/badge/C%2B%2B-20-00599C?style=flat-square&logo=cplusplus" />
        <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus" />
        <img src="https://img.shields.io/badge/ncursesw-000?style=flat-square" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/ai-quick-ask">
          🤖 <b>AI Quick Ask</b>
        </a>
      </h3>
      <p align="center">
        Chrome extension for querying local <b>Ollama</b> LLMs instantly via text highlight + hotkeys.<br/><br/>
        <img src="https://img.shields.io/badge/Chrome_Extension-4285F4?style=flat-square&logo=googlechrome" />
        <img src="https://img.shields.io/badge/Ollama-000?style=flat-square&logo=ollama" />
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript" />
      </b>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/email_blaster">
          📧 <b>Email Blaster</b>
        </a>
      </h3>
      <p align="center">
        Automated CLI batch email sender using SendGrid API with template injection, rate limiting, and dry-run safety.<br/><br/>
        <img src="https://img.shields.io/badge/Shell_Script-000?style=flat-square&logo=gnubash" />
        <img src="https://img.shields.io/badge/SendGrid-000?style=flat-square&logo=sendgrid" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">
        <a href="https://github.com/nmhuei/nonograms">
          🧩 <b>Nonograms Solver</b>
        </a>
      </h3>
      <p align="center">
        Auto-solver for nonograms.org puzzles. Rust solver + Python automation + Chrome extension for in-browser solving.<br/><br/>
        <img src="https://img.shields.io/badge/Rust-000?style=flat-square&logo=rust" />
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python" />
        <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite" />
      </p>
    </td>
  </tr>
</table>

---

## 📊 GitHub Analytics

<div align="center">
  <table>
    <tr>
      <td>
        <img height="180em" src="https://github-readme-stats-anuraghazra1.vercel.app/api?username=nmhuei&count_private=true&show_icons=true&theme=radical&hide_border=true&bg_color=0d1117&include_all_commits=true" alt="GitHub Stats" />
      </td>
      <td>
        <img height="180em" src="https://github-readme-stats-anuraghazra1.vercel.app/api/top-langs/?username=nmhuei&layout=compact&langs_count=8&theme=radical&hide_border=true&bg_color=0d1117&exclude_repo=nmhuei" alt="Top Languages" />
      </td>
    </tr>
  </table>
  <img height="180em" src="https://github-readme-streak-stats.herokuapp.com/?user=nmhuei&theme=radical&hide_border=true&background=0d1117" alt="GitHub Streak" />
</div>

---

## 🛠️ Tech Arsenal

<div align="center">

### Languages & Runtimes

<img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" />
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnubash&logoColor=white" />

### Frameworks & Libraries

<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/Axum-000?style=for-the-badge&logo=rust&logoColor=white" />
<img src="https://img.shields.io/badge/FastMCP-000?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white" />

### Infrastructure & Tools

<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
<img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />

### Security Arsenal

<img src="https://img.shields.io/badge/Burp_Suite-FF6600?style=for-the-badge&logo=portswigger&logoColor=white" />
<img src="https://img.shields.io/badge/IDA_Pro-000?style=for-the-badge&logo=hexrays&logoColor=white" />
<img src="https://img.shields.io/badge/Ghidra-000?style=for-the-badge&logo=nsa&logoColor=white" />
<img src="https://img.shields.io/badge/radare2-000?style=for-the-badge&logo=radare2&logoColor=white" />
<img src="https://img.shields.io/badge/pwndbg-000?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Cloudflare-000?style=for-the-badge&logo=cloudflare&logoColor=F38020" />

</div>

---

## 📈 Current Focus

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '14px', 'pie1': '#e94560', 'pie2': '#0f3460', 'pie3': '#16213e', 'pie4': '#1a1a2e', 'pie5': '#39FF14', 'pie6': '#FF6B35', 'pie7': '#4ea8de' }}}%%
pie showData
    title Weekly Activity Distribution
    "Rust (opencode2claude)" : 35
    "Python (botquanganh_mcp)" : 25
    "C++20 (monitor)" : 15
    "CTF / Security Research" : 12
    "Learning" : 8
    "Other Projects" : 5
```

---

## 🐍 Contribution Graph

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nmhuei/nmhuei/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/nmhuei/nmhuei/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/nmhuei/nmhuei/output/github-contribution-grid-snake.svg">
  </picture>
</p>

---

## 🤝 Connect

<div align="center">
  <a href="https://github.com/nmhuei">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/nmhuei">
    <img src="https://img.shields.io/badge/Portfolio-000?style=for-the-badge&logo=aboutdotme&logoColor=white" />
  </a>
  <a href="https://github.com/nmhuei/nmhuei/issues">
    <img src="https://img.shields.io/badge/Contact-FF6B35?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</div>

<div align="center">
  
  **Thanks for stopping by** ⭐
  
  *If any of my projects helped you, consider starring them — it helps others discover them too!*
  
</div>

</div>