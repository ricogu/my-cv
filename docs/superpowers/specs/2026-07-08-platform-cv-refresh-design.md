# Platform CV Refresh Design

## Purpose

Refresh the CV for a Senior Platform Engineer target role while preserving the user's broader strengths in software tooling development and AI-assisted workflow optimization.

## Supported Context

The recent knowledge entries after May 2026 show work around Kubernetes platform engineering, Gardener/IronCore operations, cluster lifecycle automation, reliability hardening, Helm-based delivery, internal tooling, documentation, and OpenCode-based workflow automation. AAS MCP/auth review experience is intentionally excluded.

## Positioning

The CV should present the user as a Senior Platform Engineer with deep cloud-native infrastructure experience, strong software tooling skills, and practical AI-assisted engineering workflow habits.

The top-level narrative should be:

Platform engineering at SAP scale; Kubernetes/Gardener/IronCore reliability; software tooling for delivery and operations; AI-assisted workflows as a productivity multiplier.

## Content Changes

Update the current role title from Senior Software Engineer to Senior Platform Engineer.

Keep the current role high-level. Emphasize:

- Kubernetes, Gardener, IronCore, and Cluster API based platform engineering.
- Cluster lifecycle automation, bare-metal provisioning workflows, and multi-cluster delivery tooling.
- Reliability hardening through rollout safety, credential/configuration lifecycle improvements, and operational automation.
- Internal software tooling and AI-assisted engineering workflows for delivery quality, knowledge reuse, code review, and developer productivity.

Remove reviewer-focused content from the proposed CV update. Do not mention AAS MCP/auth review work.

Trim the older Senior DevOps Engineer role so it supports, but does not compete with, the current platform role. Keep only the strongest high-level themes: GitOps transformation, platform/delivery tooling, Kubernetes operators and integrations, observability, and earlier LLM developer tooling exploration.

## File Scope

Primary edits should be made in `rico-cv.tex`.

If `rico-cv.tex` changes, update `cv-data.yaml` with a shorter abstracted version that remains aligned with the LaTeX source while preserving YAML-only content.

## Verification

After editing, compile the CV with `pdflatex rico-cv.tex` and inspect the result for build success and obvious layout overflow.
