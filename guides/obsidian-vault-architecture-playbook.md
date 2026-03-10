# Obsidian Vault Architecture Playbook (for Agents)

Reference architecture for using Obsidian as a reliable agent memory backend.

## 1) Vault layout model

Suggested top-level folders:
- inbox/ (raw captures)
- notes/ (working notes)
- graph/ (normalized knowledge artifacts)
- atlas/ (maps-of-content and indexes)
- templates/ (note schemas)
- data/ (optional exports/cache)

Principles:
- separate ingestion from curated knowledge
- keep predictable paths for automation
- maintain human readability first, machine structure second

## 2) Metadata schema

Use Properties/frontmatter consistently:
- id
- title
- type (note, concept, playbook, source)
- status (draft, reviewed, canonical, archived)
- tags
- created_at / updated_at
- source_links
- confidence

Avoid free-form sprawl for key fields.

## 3) Linking strategy

Use three link classes:
1. Structural links
- index/atlas -> child pages

2. Semantic links
- concept-to-concept relations

3. Provenance links
- note -> external source / evidence

Maintain backlinks but avoid circular noise.

## 4) Agent integration patterns

A) Local plugin model
- Use Obsidian plugin APIs for in-vault CRUD and graph-aware updates.

B) External process model
- Use Local REST API + filesystem watchers for out-of-app agents.

C) Hybrid model
- External ingestion + in-vault curation pass.

## 5) Query and retrieval stack

Recommended layers:
- Dataview queries for structured fields
- Graph tooling (Juggl/native graph) for relation traversal
- Full-text search enhancements (Omnisearch-style)
- Optional export/index pipeline for external RAG systems

## 6) Sync and versioning

- Use Obsidian Git (or equivalent) for auditability.
- Prefer branch-based curation for large automated updates.
- Keep periodic snapshots before bulk rewrites.

## 7) Operational controls

- Validate links after automated edits.
- Enforce template/schema checks for new notes.
- Run periodic dead-link and orphan-note audits.
- Keep a canonical index for each major domain.

## 8) Common failure modes

- Schema drift across notes
- Over-linking that degrades graph utility
- Automated edits breaking wikilinks
- Large stale inbox backlog

Mitigation:
- strict templates
- curation queues
- periodic graph hygiene jobs
- promotion workflow (draft -> canonical)

## 9) Quick checklist

- [ ] Folder architecture defined and documented
- [ ] Metadata schema enforced
- [ ] Structural indexes in atlas/
- [ ] Agent read/write boundaries documented
- [ ] Link and orphan audits scheduled
- [ ] Versioning/snapshot policy in place

## 10) Key references

- Obsidian data model: https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data
- Properties: https://help.obsidian.md/Editing+and+formatting/Properties
- Plugin guide: https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin
- Vault API: https://docs.obsidian.md/Reference/TypeScript+API/Vault
- obsidian-api: https://github.com/obsidianmd/obsidian-api
- Dataview: https://github.com/blacksmithgu/obsidian-dataview
- Local REST API: https://github.com/coddingtonbear/obsidian-local-rest-api
- Advanced URI: https://github.com/Vinzent03/obsidian-advanced-uri
- Obsidian Git: https://github.com/Vinzent03/obsidian-git
