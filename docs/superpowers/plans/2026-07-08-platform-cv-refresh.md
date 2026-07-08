# Platform CV Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh the CV so it targets Senior Platform Engineer roles while preserving software tooling and AI-assisted workflow strengths.

**Architecture:** `rico-cv.tex` remains the authoritative PDF source. `cv-data.yaml` is kept as the shorter website data model, synchronized from the LaTeX source while preserving YAML-only content. Verification is build-based because this is a content update, not application code.

**Tech Stack:** LaTeX `moderncv`, YAML, `pdflatex`, `rg`, `git diff --check`.

---

## File Structure

- Modify `rico-cv.tex`: primary CV content, including title, summary, core competencies, current role, and trimmed Senior DevOps Engineer role.
- Modify `cv-data.yaml`: website data synchronized to the LaTeX changes in a shorter, abstracted form.
- Generated but do not intentionally commit: `rico-cv.pdf`, `rico-cv.aux`, `rico-cv.log`, `rico-cv.out`.

## Implementation Tasks

### Task 1: Update LaTeX CV Positioning

**Files:**
- Modify: `rico-cv.tex:31-74`

- [ ] **Step 1: Verify current content still needs the update**

Run:

```bash
rg -n "Senior Software Engineer|seed/shoot|kubeinception|code review|AAS|FastMCP|OIDC" rico-cv.tex
```

Expected: matches include `Senior Software Engineer`, `seed/shoot`, `kubeinception`, and `code review`. `AAS`, `FastMCP`, and `OIDC` should not match.

- [ ] **Step 2: Update title and summary**

In `rico-cv.tex`, replace the title and Summary block with:

```latex
\title{Senior Platform Engineer \& Cloud Native Software Engineer}
```

```latex
    \section{Summary}
    \cvitem{}{
        Senior \textbf{Platform Engineer/Cloud Native Software Engineer} with 10+ years of experience building, automating, and operating Kubernetes-based infrastructure platforms. Specialized in \textbf{Gardener, IronCore, Cluster API, GitOps, platform reliability, and software tooling}. Practical experience using AI-assisted engineering workflows to improve delivery quality, operational knowledge reuse, and developer productivity.
    }
```

- [ ] **Step 3: Replace Core Competencies with platform-oriented categories**

In `rico-cv.tex`, replace the current `Core Competencies` item list with:

```latex
    \section{Core Competencies}
    \cvitem{}{\begin{itemize}
        \item \textbf{Cloud \& Platforms:} SAP Cloud Infrastructure, Kubernetes, Gardener, IronCore, Cluster API, SAP BTP, Kyma, Azure
        \item \textbf{GitOps \& Platform Automation:} FluxCD, ArgoCD, Helm, Kustomize, Crossplane, External Secrets Operator, Renovate
        \item \textbf{Reliability \& Operations:} Cluster lifecycle automation, rollout safety, credential lifecycle, observability, alerting, runbooks
        \item \textbf{Software Tooling:} Go, Java, Python, Bash, Node.js, GitHub Apps, GitHub Actions, Docker, Terraform
        \item \textbf{AI-Assisted Engineering:} OpenCode, Claude Code, MCP, semantic search, knowledge automation, SDD, TDD workflows
    \end{itemize}}
```

- [ ] **Step 4: Update current role title and bullets**

In `rico-cv.tex`, replace the current role entry with:

```latex
    \cventry{May 2026 -- Present}{Senior Platform Engineer}{SAP SE, SAP Cloud Infrastructure}{Munich}{}{
        \begin{itemize}
            \item Contributing to SAP cloud infrastructure platform engineering across Kubernetes, Gardener, IronCore, and Cluster API based environments.
            \item Improving cluster lifecycle automation, bare-metal provisioning workflows, and multi-cluster delivery tooling for large-scale infrastructure operations.
            \item Hardening platform reliability through safer rollout mechanisms, credential and configuration lifecycle improvements, and operational automation.
            \item Developing internal software tooling and AI-assisted engineering workflows to improve delivery quality, knowledge reuse, and developer productivity.
        \end{itemize}
    }
```

- [ ] **Step 5: Trim Senior DevOps Engineer role**

In `rico-cv.tex`, replace the Senior DevOps Engineer bullet list with:

```latex
        \begin{itemize}
            \item Led GitOps transformation for multi-cluster Kyma/Gardener environments using FluxCD, ArgoCD, Helm, Kustomize, and Crossplane.
            \item Built platform and delivery tooling for PR governance, deployment validation, semantic versioning, and CI/CD automation.
            \item Implemented Kubernetes operators and cloud-native integrations for SAP BTP and business network platforms.
            \item Centralized observability, audit logging, and alerting across distributed cloud environments.
            \item Explored LLM-based developer tooling, semantic search, and Kubernetes-hosted AI services.
        \end{itemize}
```

- [ ] **Step 6: Verify LaTeX content no longer contains excluded details**

Run:

```bash
rg -n "Senior Software Engineer|seed/shoot|kubeinception|code review|AAS|FastMCP|OIDC|#12197|#12212|zoneSelection" rico-cv.tex
```

Expected: no matches.

- [ ] **Step 7: Commit LaTeX source update**

Run:

```bash
git add rico-cv.tex
git commit -m "content: retarget CV for platform engineering"
```

Expected: commit succeeds and stages only `rico-cv.tex`.

### Task 2: Synchronize Website YAML Data

**Files:**
- Modify: `cv-data.yaml:4-52`

- [ ] **Step 1: Verify YAML still needs synchronization**

Run:

```bash
rg -n "Senior Software Engineer|seed/shoot|kubeinception|code review|AAS|FastMCP|OIDC" cv-data.yaml
```

Expected: matches include `Senior Software Engineer`, `seed/shoot`, and `kubeinception`. `AAS`, `FastMCP`, and `OIDC` should not match.

- [ ] **Step 2: Update personal and about sections**

In `cv-data.yaml`, update these fields:

```yaml
personal:
  title: "Senior Platform Engineer & Cloud Native Software Engineer"

about:
  headline: "Senior Platform Engineer & Cloud Native Software Engineer"
  summary: >
    Senior Platform Engineer / Cloud Native Software Engineer with 10+
    years of experience building, automating, and operating Kubernetes-based
    infrastructure platforms. Specialized in Gardener, IronCore, Cluster API,
    GitOps, platform reliability, and software tooling, with practical
    AI-assisted workflows for delivery quality and knowledge reuse.
```

Keep the existing `personal.name`, `personal.full_name`, `personal.typed_items`, contact fields, and social links unchanged.

- [ ] **Step 3: Update core competencies**

In `cv-data.yaml`, replace `core_competencies` with:

```yaml
core_competencies:
  - category: "Cloud & Platforms"
    skills: ["SAP Cloud Infrastructure", "Kubernetes", "Gardener", "IronCore", "Cluster API", "SAP BTP", "Kyma", "Azure"]
  - category: "GitOps & Platform Automation"
    skills: ["FluxCD", "ArgoCD", "Helm", "Kustomize", "Crossplane", "External Secrets Operator", "Renovate"]
  - category: "Reliability & Operations"
    skills: ["Cluster lifecycle automation", "Rollout safety", "Credential lifecycle", "Observability", "Alerting", "Runbooks"]
  - category: "Software Tooling"
    skills: ["Go", "Java", "Python", "Bash", "Node.js", "GitHub Apps", "GitHub Actions", "Docker", "Terraform"]
  - category: "AI-Assisted Engineering"
    skills: ["OpenCode", "Claude Code", "MCP", "Semantic Search", "Knowledge Automation", "SDD", "TDD"]
```

- [ ] **Step 4: Update current role YAML entry**

In `cv-data.yaml`, replace the first `experience` entry with:

```yaml
  - title: "Senior Platform Engineer"
    company: "SAP SE, SAP Cloud Infrastructure, Munich"
    period: "May 2026 - Present"
    bullets:
      - "Contributing to Kubernetes, Gardener, IronCore, and Cluster API based platform engineering for SAP cloud infrastructure"
      - "Improving cluster lifecycle automation, bare-metal provisioning workflows, and multi-cluster delivery tooling"
      - "Hardening platform reliability through rollout safety, credential and configuration lifecycle improvements, and operational automation"
      - "Developing internal software tooling and AI-assisted workflows for delivery quality, knowledge reuse, and developer productivity"
```

- [ ] **Step 5: Trim Senior DevOps Engineer YAML entry**

In `cv-data.yaml`, replace the Senior DevOps Engineer entry with:

```yaml
  - title: "Senior DevOps Engineer"
    company: "SAP SE, SAP Business Network, Munich"
    period: "Nov 2021 - Apr 2026"
    bullets:
      - "Led GitOps transformation for multi-cluster Kyma/Gardener environments using FluxCD, ArgoCD, Helm, Kustomize, and Crossplane"
      - "Built platform and delivery tooling for PR governance, deployment validation, semantic versioning, and CI/CD automation"
      - "Implemented Kubernetes operators and cloud-native integrations for SAP BTP and business network platforms"
      - "Centralized observability, audit logging, and alerting across distributed cloud environments"
      - "Explored LLM-based developer tooling, semantic search, and Kubernetes-hosted AI services"
```

- [ ] **Step 6: Verify YAML content no longer contains excluded details**

Run:

```bash
rg -n "Senior Software Engineer|seed/shoot|kubeinception|code review|AAS|FastMCP|OIDC|#12197|#12212|zoneSelection" cv-data.yaml
```

Expected: no matches.

- [ ] **Step 7: Commit YAML synchronization**

Run:

```bash
git add cv-data.yaml
git commit -m "content: sync platform CV website data"
```

Expected: commit succeeds and stages only `cv-data.yaml`.

### Task 3: Build and Review CV Output

**Files:**
- Verify: `rico-cv.tex`
- Generated: `rico-cv.pdf`, `rico-cv.aux`, `rico-cv.log`, `rico-cv.out`

- [ ] **Step 1: Run LaTeX build**

Run:

```bash
pdflatex -interaction=nonstopmode rico-cv.tex
```

Expected: command exits successfully and writes `rico-cv.pdf`.

- [ ] **Step 2: Check source diff quality**

Run:

```bash
git diff --check
```

Expected: no whitespace errors.

- [ ] **Step 3: Confirm intended tracked-file state**

Run:

```bash
git status --short
```

Expected: only generated/untracked artifacts may remain, such as `.playwright-mcp/`, `rico-cv.out`, or `rico-cv.pdf`. No unintended tracked source changes should remain after the two content commits.

- [ ] **Step 4: Report verification result**

Report the `pdflatex` result, any generated artifacts left uncommitted, and the two content commits created by Tasks 1 and 2.

## Self-Review

Spec coverage:

- Current role title changes to Senior Platform Engineer in Task 1 and Task 2.
- Current role stays high-level and excludes reviewer/AAS MCP/auth details in Task 1 and Task 2.
- Older Senior DevOps Engineer content is trimmed in Task 1 and Task 2.
- `cv-data.yaml` synchronization is covered in Task 2.
- Build verification is covered in Task 3.

Placeholder scan:

- No TODO, TBD, or unspecified implementation steps remain.

Type/content consistency:

- LaTeX and YAML use the same role title and aligned high-level bullet themes.
