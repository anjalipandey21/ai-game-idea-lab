# AI Game Idea Lab 🎮🤖

A daily lab where I experiment with AI-flavoured game mechanics in **Python**, **JavaScript**, and **Go**.

Every day, a GitHub Action runs a small script that:
- Generates a fresh **game mechanic idea**
- Adds it as a markdown file under [`mechanics/`](mechanics/)
- Appends the idea to this README log

The goal is to build a living notebook of mechanics that could turn into:
- Tiny prototypes
- Game jam ideas
- AI-driven experiments (RL, heuristics, simple models)

---

## How it works

### 🕒 Daily automation

The workflow in [`.github/workflows/main.yml`](.github/workflows/main.yml):

- Runs once per day (via cron)
- Calls `scripts/generate_mechanic.py`
- If there are changes, it commits and pushes them back to the repo

This keeps the repo active and slowly builds a catalogue of mechanics over time.

### 🧠 Python generator

[`scripts/generate_mechanic.py`](scripts/generate_mechanic.py) creates:

- A title (`Pause Time Roguelike`, `Clone The Player Platformer`, etc.)
- A **theme**, **genre**, **core action**, **constraint**, and an **AI twist**
- A markdown file under `mechanics/YYYY-MM-DD-some-title.md`
- A log entry in this README

The ideas are intentionally small and “game-jam friendly”.

### 🟨 JavaScript + 🟦 Go notes

- [`scripts/generate_mechanic.js`](scripts/generate_mechanic.js)  
  Notes & sketches for browser / canvas prototypes.

- [`scripts/generate_mechanic.go`](scripts/generate_mechanic.go)  
  Notes for building simulation-style prototypes in Go.

These can be run manually to generate extra notes in the same `mechanics/` folder.

---

## 🔴 Tiny browser game prototype

Under [`web/`](web/) there’s a simple HTML5 canvas game:

- Move a square with **arrow keys / WASD**
- Avoid “glitches” (enemy squares) flying across the screen
- The difficulty slowly ramps up

This is a lightweight playground where some of the generated mechanics can be prototyped.

To run it locally:

```bash
cd web
python -m http.server 8000  # or any static HTTP server
# then open http://localhost:8000 in your browser
