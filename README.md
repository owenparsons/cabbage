# cabbage

Quick LLM answers from your terminal.

```
$ cabbage "how do I find all .py files recursively?"
find . -name "*.py"
```

Avoids needing to spin up Claude Code or open a browser session just for a simple one-line query. Just ask a question and get an answer.

## Prerequisites

- Python 3.8+
- [Claude Code](https://claude.ai/claude-code) CLI installed and authenticated

## Install

```bash
pipx install .
```

## Usage

```bash
cabbage "how do I undo the last git commit?"
cabbage "explain the difference between rebase and merge"
cabbage "regex to match email addresses"
```

Wrap your question in quotes to avoid shell interpretation of special characters like `?` and `*`.

## Why "cabbage"?

This tool is a small, simple wrapper around [Claude](https://claude.ai), so you could think of it as Claude's child. The most famous Claude that comes to my mind when I think of the name is the composer [Claude Debussy](https://en.wikipedia.org/wiki/Claude_Debussy), whose [daughter was affectionately nicknamed *Chouchou*]((https://interlude.hk/claude-emma-debussy-the-story-of-debussys-doomed-daughter/)) (a French term of endearment that translates loosely to "little cabbage"). Hence, cabbage.
