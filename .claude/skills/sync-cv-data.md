---
name: sync-cv-data
description: >
  Sync cv-data.yaml with changes from rico-cv.tex. Reads the LaTeX CV,
  compares with the current YAML, and produces an updated abstracted version.
  Triggered automatically when rico-cv.tex is modified.
---

# Sync CV Data

You are updating `cv-data.yaml` to reflect changes made to `rico-cv.tex`.

## Instructions

1. Read `rico-cv.tex` to understand the current full CV content.
2. Read `cv-data.yaml` to understand the current website content.
3. Compare the two and identify sections that are out of sync (new entries, changed bullets, removed content, updated dates/titles).
4. Update `cv-data.yaml` with an **abstracted** version of the LaTeX content:
   - Keep job titles, company names, and dates exact
   - Summarize bullet points: shorter, fewer details, 3-4 bullets max per role
   - Focus on technologies and impact, not process details
   - Preserve any YAML-only content that doesn't exist in the LaTeX (e.g., publications, diploma)
5. Show the user what changed (before/after diff) and ask for approval before writing.

## YAML Structure

The YAML must maintain this structure:

```yaml
personal:
  name, full_name, title, typed_items, email, phone, address, linkedin, github, facebook
about:
  headline, summary
experience:
  - title, company, period, bullets[]
education:
  - degree, school, period, bullets[]
publications:
  - citation strings (HTML allowed for <strong> tags)
```

## Abstraction Guidelines

- LaTeX `\cventry{dates}{title}{company}{city}{}{items}` maps to one experience/education entry
- Keep the essence but simplify: "Led GitOps transformation for multi-cluster Kyma/Gardener environments using FluxCD & ArgoCD" → "Managed Kubernetes clusters via GitOps principles (Helm, Kustomize, ArgoCD)"
- The `personal` section should stay in sync with `\name`, `\title`, `\address`, `\phone`, `\email`, `\social` commands
- The `about.summary` should reflect the `\section{Objective}` content but shorter
- Do NOT copy the LaTeX verbatim — the website version should be concise and scannable
