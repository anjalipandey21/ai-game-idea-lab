#!/usr/bin/env python3
import random
from datetime import datetime
from pathlib import Path
import textwrap
import unicodedata
import re

ROOT = Path(__file__).resolve().parents[1]
MECH_DIR = ROOT / "mechanics"
MECH_DIR.mkdir(parents=True, exist_ok=True)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-")
    return text.lower()


THEMES = [
    "cyberpunk city",
    "post-apocalyptic wasteland",
    "orbital station",
    "ancient ruins with futuristic tech",
    "neon dungeon",
    "AI training arena",
]

GENRES = [
    "roguelike",
    "tactical card game",
    "platformer",
    "puzzle game",
    "tower defense",
    "real-time tactics",
]

CORE_ACTIONS = [
    "pause time",
    "invert gravity",
    "clone the player",
    "rewrite enemy behavior",
    "corrupt the game rules",
    "scramble the map layout",
]

CONSTRAINTS = [
    "player only sees partial information",
    "you can only act every third turn",
    "resources decay over time",
    "controls randomly remap under stress",
    "you must sacrifice a power to gain another",
    "the level layout changes every time you fail",
]

AI_TWISTS = [
    "an on-device model predicts the next enemy move",
    "a simple RL agent controls an ally with its own agenda",
    "a tiny classifier labels player decisions as “risky” or “safe” and changes rewards",
    "procedural levels are generated using weighted prompts",
    "NPC dialogue is blended from a Markov chain over past matches",
    "enemy spawning adapts to your failure patterns",
]

IMPLEMENTATION_NOTES = [
    "Prototype state transitions as a pure function so it’s easy to plug in different AI policies.",
    "Log every decision to a JSONL file so you can replay and train simple agents later.",
    "Keep the AI very small (heuristics or shallow models) so it’s easy to reason about in code.",
    "Expose all tuning knobs (weights, thresholds) via a config file rather than hard-coding.",
    "Separate the simulation core from rendering so you can run experiments headless.",
]


def build_mechanic():
    theme = random.choice(THEMES)
    genre = random.choice(GENRES)
    action = random.choice(CORE_ACTIONS)
    constraint = random.choice(CONSTRAINTS)
    twist = random.choice(AI_TWISTS)
    note = random.choice(IMPLEMENTATION_NOTES)

    title = f"{action.title()} {genre.title()}"
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"

    body = f"""\
    # {title}

    **Date:** {date_str}  
    **Theme:** {theme}  
    **Genre:** {genre}

    ## Core mechanic

    The player can **{action}** in a **{genre}** set in a **{theme}**.

    ## Constraint

    Design around this constraint: **{constraint}**.

    ## AI twist

    Integrate AI in a lightweight way: **{twist}**.

    ## Implementation sketch

    - Represent game state as a simple data structure (no engine magic).
    - Add a small API surface for the AI to inspect state and suggest actions.
    - {note}
    - Start with a debug CLI prototype before wiring into any UI or engine.

    ## Notes for future you

    - How could this work as a 5-minute game jam prototype?
    - What would be the *fun breakpoint* to test first?
    - Is the AI making things more readable or more chaotic?
    """

    body = textwrap.dedent(body).strip() + "\n"
    return filename, title, body


def append_to_readme(title: str, filename: str):
    readme_path = ROOT / "README.md"
    date_str = datetime.utcnow().strftime("%Y-%m-%d")

    if not readme_path.exists():
        readme_path.write_text(
            "# AI Game Idea Lab\n\n"
            "Daily AI-flavoured game mechanics in Python, JS, and Go.\n\n"
            "## Daily log\n\n",
            encoding="utf-8",
        )

    existing = readme_path.read_text(encoding="utf-8")
    entry = f"- {date_str}: [{title}](mechanics/{filename})\n"

    if entry not in existing:
        updated = existing + entry
        readme_path.write_text(updated, encoding="utf-8")


def main():
    filename, title, body = build_mechanic()
    mech_path = MECH_DIR / filename

    if mech_path.exists():
        # Avoid regenerating on the same day if rerun.
        return

    mech_path.write_text(body, encoding="utf-8")
    append_to_readme(title, filename)


if __name__ == "__main__":
    main()
