package main

import (
	"fmt"
	"math/rand"
	"os"
	"path/filepath"
	"strings"
	"time"
)

var themes = []string{
	"procedural labyrinth",
	"AI-run gladiator arena",
	"virtual petri dish",
	"signal-jammed battlefield",
}

var genres = []string{
	"top-down shooter",
	"resource management sim",
	"co-op puzzler",
	"survival arena",
}

var actions = []string{
	"redirect projectiles mid-flight",
	"hack enemy squads as temporary allies",
	"scrub your own footprints from the map",
	"record and replay your past runs as clones",
}

var constraints = []string{
	"fog of war hides everything but sound cues",
	"ammo is shared across all weapons",
	"healing always has a delayed effect",
	"every ability has a visible cooldown arc",
}

var aiTwists = []string{
	"a small heuristic bot auto-plays for a few seconds when you freeze",
	"the game tracks your common mistakes and surfaces them as hints",
	"enemy patterns are shuffled based on a simple Markov chain",
	"the map spawns extra cover when you’re low on health",
}

func pick(list []string) string {
	return list[rand.Intn(len(list))]
}

func slugify(text string) string {
	text = strings.ToLower(text)
	text = strings.ReplaceAll(text, " ", "-")
	text = strings.ReplaceAll(text, "/", "-")
	text = strings.ReplaceAll(text, ".", "-")
	return text
}

func main() {
	rand.Seed(time.Now().UnixNano())

	root, _ := filepath.Abs(filepath.Join(filepath.Dir(os.Args[0]), ".."))
	mechDir := filepath.Join(root, "mechanics")
	_ = os.MkdirAll(mechDir, 0o755)

	theme := pick(themes)
	genre := pick(genres)
	action := pick(actions)
	constraint := pick(constraints)
	twist := pick(aiTwists)

	title := fmt.Sprintf("%s %s", strings.Title(action), strings.Title(genre))
	dateStr := time.Now().UTC().Format("2006-01-02")
	slug := slugify(title)
	filename := fmt.Sprintf("%s-%s-go-note.md", dateStr, slug)
	mechPath := filepath.Join(mechDir, filename)

	body := fmt.Sprintf(`# %s

**Date:** %s  
**Go prototype**

## Setup

- Theme: %s
- Genre: %s

## Mechanic

- Core: %s
- Constraint: %s
- AI twist: %s

### Go notes

- Treat the game loop as a pure tick() function: state -> state.
- Consider a simple bot that calls tick() with its own actions for testing.
`, title, dateStr, theme, genre, action, constraint, twist)

	if _, err := os.Stat(mechPath); os.IsNotExist(err) {
		_ = os.WriteFile(mechPath, []byte(strings.TrimSpace(body)+"\n"), 0o644)
	}
}
