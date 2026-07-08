# AGENTS.md

This file is the central source of AI-agent guidance for this repository.

## Project Overview

A personal CV/resume written in LaTeX using the `moderncv` package. The primary source file is `rico-cv.tex`, which compiles to `rico-cv.pdf`.

The website data is maintained separately in `cv-data.yaml` and should stay aligned with the LaTeX CV at a concise, abstracted level.

## Build

Requires a LaTeX distribution with `moderncv` installed, such as TeX Live or MiKTeX.

```bash
pdflatex rico-cv.tex
```

The GitHub Actions workflow `.github/workflows/generate-cv.yml` automatically builds the PDF on push to `main` using `xu-cheng/latex-action@v3` and deploys it to GitHub Pages.

## Branches

- `main` is the source branch. Edit `rico-cv.tex`, `cv-data.yaml`, and workflow/source files here.
- `gh-pages` is managed by CI through `peaceiris/actions-gh-pages`. Do not edit this branch directly.

## Architecture

- `rico-cv.tex` is the authoritative PDF CV source. It uses `moderncv` with the `casual` style, `blue` color theme, and `geometry` scale `0.88`.
- `cv-data.yaml` contains concise website/profile data derived from the CV while preserving YAML-only content such as publications.
- `site-template/index.html.j2` and `scripts/build-site.py` generate website output from `cv-data.yaml`.
- `.github/workflows/generate-cv.yml` builds and deploys the generated PDF/site content.
- Generated outputs include `rico-cv.pdf`, `rico-cv.aux`, `rico-cv.log`, `rico-cv.out`, and `build/`.

## Editing Guidance

- Keep CV wording concise, high-level, and role-targeted.
- When changing `rico-cv.tex`, update `cv-data.yaml` with a shorter abstracted version of the same content.
- Preserve YAML-only content in `cv-data.yaml`, especially publications and extra education entries that are not present in the LaTeX CV.
- Do not commit generated build artifacts unless explicitly requested.
