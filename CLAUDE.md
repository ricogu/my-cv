# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A personal CV/resume written in LaTeX using the `moderncv` package. The single source file `rico-cv.tex` compiles to a PDF.

## Build

Requires a LaTeX distribution with `moderncv` installed (e.g., TeX Live, MiKTeX).

```bash
# Compile locally
pdflatex rico-cv.tex
```

The GitHub Actions workflow (`.github/workflows/generate-cv.yml`) automatically builds the PDF on push to `main` using `xu-cheng/latex-action@v3` and deploys it to GitHub Pages.

## Branches

- **`main`** — Source branch. Contains `rico-cv.tex` and the CI workflow. All edits happen here.
- **`gh-pages`** — Deployment branch managed by the CI workflow (`peaceiris/actions-gh-pages`). Hosts the compiled `rico-cv.pdf` and serves GitHub Pages. Do not edit this branch directly.

## Architecture

- **`rico-cv.tex`** — The entire CV source. Uses `moderncv` with the `casual` style and `blue` color theme. Page layout uses `geometry` at 0.75 scale.
- **`.github/workflows/generate-cv.yml`** — CI pipeline: builds LaTeX → cleans aux files → deploys PDF to `gh-pages` branch for GitHub Pages hosting.
- Output PDF is named `rico-cv.pdf`.
