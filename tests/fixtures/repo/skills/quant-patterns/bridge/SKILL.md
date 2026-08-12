---
name: quant-bridge
description: "Use when testing playbook exemptions. Fixture playbook: exempt from the §3 required-section check (SKILL_SPEC §7)."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [numpy-core]
tags: [quantitative-finance, fixture]
related_skills: [numpy-core]
---

# Quant Bridge (fixture playbook)

Fixture playbook: no `source_commit`/`graph` block and no §3 sections — both per §7.
It must pass the section check and its `composes` must resolve.

## Steps
1. Load `numpy-core` for array work.

## Pitfalls
1. None — this fixture is meant to be clean.

## Composed Skills & Bridges
- [numpy-core](../numpy/core/SKILL.md)
