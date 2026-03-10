# Neural Linking and Memory Playbook

A practical guide for using neural memory and neural-linking concepts in real agent systems.

## 1) What "neural linking" means for agents

In practice, neural linking is the combination of:
- retrieval linking (query -> relevant memory chunks)
- relational linking (entity/relation edges across memories)
- neural-symbolic linking (neural perception + explicit rules)

Goal: convert fragmented context into connected, actionable state.

## 2) Architecture pattern

Use a layered memory system:

1. Working memory (short horizon)
- Current objective, active plan, last tool outputs.

2. Episodic memory (session horizon)
- Compressed summaries and key decisions.

3. Semantic memory (long horizon)
- Stable facts, entities, relationships, procedures.

4. Retrieval layer
- Hybrid retrieval + rerank + link-aware packing.

## 3) Retrieval and linking pipeline

Recommended pipeline:
1. Normalize query (entities, time, domain terms)
2. Hybrid retrieve (lexical + vector)
3. Rerank by relevance and diversity
4. Build/expand local relation graph for top candidates
5. Pack context with citations and dependency order

Keep each retrieved chunk annotated with:
- source
- timestamp
- confidence
- relation targets (if available)

## 4) Neural + symbolic fusion pattern

Use neural models for:
- retrieval relevance
- semantic similarity
- uncertain inference

Use symbolic logic for:
- hard constraints
- safety/policy rules
- deterministic validation

Rule of thumb:
- probabilistic tasks -> neural
- compliance-critical tasks -> symbolic checks

## 5) Failure modes to watch

- Link drift: stale links between entities over time
- Retrieval pollution: unrelated chunks dominate context
- Over-compression: removes dependencies needed for reasoning
- Rule bypass: neural confidence overrides explicit constraints

Mitigations:
- link freshness checks
- duplicate suppression + rerank thresholds
- compression with protected fields
- mandatory symbolic validation on high-impact outputs

## 6) Evaluation checklist

- [ ] Multi-hop retrieval accuracy
- [ ] Entity linkage precision/recall
- [ ] Contradiction handling across linked memories
- [ ] Memory freshness under updates
- [ ] Constraint adherence after neural reasoning

## 7) Operator defaults

- Keep memory writes structured and sparse.
- Rebuild relation neighborhoods periodically.
- Prefer citations in final outputs.
- Treat long-context windows as fallback, not default design.

## 8) Core references

- Neural Turing Machines: https://arxiv.org/abs/1410.5401
- End-to-End Memory Networks: https://arxiv.org/abs/1503.08895
- Differentiable Neural Computer: https://arxiv.org/abs/1605.08582
- Transformer-XL: https://arxiv.org/abs/1901.02860
- Compressive Transformer: https://arxiv.org/abs/1911.05507
- RAG: https://arxiv.org/abs/2005.11401
- RETRO: https://arxiv.org/abs/2112.04426
- Neural Bellman-Ford Networks: https://arxiv.org/abs/2106.06935
- DeepProbLog: https://github.com/ML-KULeuven/deepproblog
