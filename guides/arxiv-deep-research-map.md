# ArXiv Deep Research Map for Agent Cortex

Purpose: deepen this repo with a practical, operator-first arXiv map across all major categories.

How to use this map:
- Start with the "Top 3 must-read" papers in each category.
- Use "Expansion" to go deeper once you have a baseline.
- Re-check benchmark claims against current leaderboards before publishing hard numbers.

## 1) Agent Frameworks and Reasoning Loops

Top 3 must-read (and why):
- [ReAct (2022)](https://arxiv.org/abs/2210.03629) - Canonical think+act loop for tool-using agents.
- [Reflexion (2023)](https://arxiv.org/abs/2303.11366) - Strong pattern for self-critique and iterative improvement.
- [Toolformer (2023)](https://arxiv.org/abs/2302.04761) - Foundation for model-native tool-use behavior.

Expansion:
- [Generative Agents (2023)](https://arxiv.org/abs/2304.03442)
- [A Survey on LLM-based Autonomous Agents (2023)](https://arxiv.org/abs/2308.11432)

## 2) Coding Agents

Top 3 must-read (and why):
- [SWE-bench (2023)](https://arxiv.org/abs/2310.06770) - Core real-repo bug-fix benchmark.
- [SWE-bench Multimodal (2024)](https://arxiv.org/abs/2410.03859) - Extends coding eval to visual software artifacts.
- [SWE-bench Goes Live! (2025)](https://arxiv.org/abs/2505.23419) - Live benchmark operations and methodology insights.

Expansion:
- [SWE-Gym (2024)](https://arxiv.org/abs/2412.21139)
- [OmniCode (2026)](https://arxiv.org/abs/2602.02262)
- [Agent-Diff (2026)](https://arxiv.org/abs/2602.11224)

## 3) MCP, Tool Use, and Agent Reliability

Top 3 must-read (and why):
- [MCPMark (2025)](https://arxiv.org/abs/2509.24002) - Current high-signal MCP stress test (real tasks, hard ceilings).
- [τ-bench (2024)](https://arxiv.org/abs/2406.12045) - Reliability framing with pass^k in interactive tool workflows.
- [Towards a Science of AI Agent Reliability (2026)](https://arxiv.org/abs/2602.16666) - Reliability science framing beyond headline accuracy.

Expansion:
- [AgentBench (2023)](https://arxiv.org/abs/2308.03688)
- [MCP-Bench (2025)](https://arxiv.org/abs/2508.20453)
- [MCPAgentBench (2025)](https://arxiv.org/abs/2512.24565)
- [MCPToolBench++ (2025)](https://arxiv.org/abs/2508.07575)

## 4) Web and Computer-Use Agents

Top 3 must-read (and why):
- [WebArena (2023)](https://arxiv.org/abs/2307.13854) - Realistic browser-task benchmark baseline.
- [VisualWebArena (2024)](https://arxiv.org/abs/2401.13649) - Adds visual grounding pressure to web-agent evals.
- [OSWorld (2024)](https://arxiv.org/abs/2404.07972) - Open-ended desktop environment with strong realism.

Expansion:
- [OS-Harm (2025)](https://arxiv.org/abs/2506.14866)

## 5) Context Engineering and Memory

Top 3 must-read (and why):
- [RAG (2020)](https://arxiv.org/abs/2005.11401) - Retrieval architecture baseline for external memory.
- [MemGPT (2023)](https://arxiv.org/abs/2310.08560) - Memory tiering and virtual-context perspective.
- [Self-RAG (2023)](https://arxiv.org/abs/2310.11511) - Retrieval with self-critique control loop.

Expansion:
- [Lost in the Middle (2023)](https://arxiv.org/abs/2307.03172)
- [RETRO (2021)](https://arxiv.org/abs/2112.04426)
- [kNN-LM (2020)](https://arxiv.org/abs/1911.00172)
- [Evaluating Very Long-Term Conversational Memory of LLM Agents (2024)](https://arxiv.org/abs/2402.17753)
- [Mem-Gallery (2026)](https://arxiv.org/abs/2601.03515)

## 6) Prompt and Programmatic Prompt Engineering

Top 3 must-read (and why):
- [Chain-of-Thought (2022)](https://arxiv.org/abs/2201.11903) - Core reasoning prompt primitive.
- [Self-Consistency (2022)](https://arxiv.org/abs/2203.11171) - Robustness boost for reasoning via sampling.
- [Tree of Thoughts (2023)](https://arxiv.org/abs/2305.10601) - Deliberate search over candidate thoughts.

Expansion:
- [DSPy (2023)](https://arxiv.org/abs/2310.03714)

## 7) Security and Robustness

Top 3 must-read (and why):
- [Universal and Transferable Adversarial Attacks on Aligned LMs (2023)](https://arxiv.org/abs/2307.15043) - Baseline offensive pressure test.
- [StruQ (2024)](https://arxiv.org/abs/2402.06363) - Structured prompt/query defense pattern.
- [SecAlign (2024)](https://arxiv.org/abs/2410.05451) - Alignment-based defense for prompt injection.

Expansion:
- [Too Helpful to Be Safe (2026)](https://arxiv.org/abs/2601.10758)
- [MCP-in-SoS (2026)](https://arxiv.org/abs/2603.10194)
- [Compatibility at a Cost (2026)](https://arxiv.org/abs/2603.10163)

## 8) Voice and Multimodal Agents

Top 3 must-read (and why):
- [Whisper / Robust Speech Recognition via Large-Scale Weak Supervision (2022)](https://arxiv.org/abs/2212.04356) - Reliable speech baseline for voice agents.
- [Visual Instruction Tuning (LLaVA, 2023)](https://arxiv.org/abs/2304.08485) - Core multimodal instruction-following pattern.
- [Mem-Gallery (2026)](https://arxiv.org/abs/2601.03515) - Long-horizon multimodal conversational memory benchmark.

## 9) Evaluation Science and LLM-as-a-Judge

Top 3 must-read (and why):
- [HELM (2022)](https://arxiv.org/abs/2211.09110) - Holistic evaluation methodology.
- [MT-Bench / Chatbot Arena LLM-as-a-Judge analysis (2023)](https://arxiv.org/abs/2306.05685) - Judge-model strengths/limits in practice.
- [Systematic Evaluation of LLM-as-a-Judge (2024)](https://arxiv.org/abs/2408.13006) - Template effects and judge reliability caveats.

## 10) Quant and Trading Agents

Top 3 must-read (and why):
- [FinRL Library (2020)](https://arxiv.org/abs/2011.09607) - Practical DRL trading baseline.
- [FinRL Framework (2021)](https://arxiv.org/abs/2111.09395) - End-to-end automation framing for quant agents.
- [FinRL-Podracer (2021)](https://arxiv.org/abs/2111.05188) - Throughput/scalability for production-ish experiments.

Expansion:
- [Large Language Models in Finance: A Survey (2023)](https://arxiv.org/abs/2311.10723)
- [LLM Agent in Financial Trading: A Survey (2024)](https://arxiv.org/abs/2408.06361)

## 11) Blockchain Identity, Payments, and DeFi-Adjacent Research

Top 3 must-read (and why):
- [Deployment of a Blockchain-Based Self-Sovereign Identity (2018)](https://arxiv.org/abs/1806.01926) - SSI implementation grounding.
- [Design Patterns for Blockchain-based Self-Sovereign Identity (2020)](https://arxiv.org/abs/2005.12112) - Reusable SSI architecture patterns.
- [Decentralized Finance (2023)](https://arxiv.org/abs/2304.01918) - Broad DeFi systems framing.

Expansion:
- [Is DeFi Actually Decentralized? (2022)](https://arxiv.org/abs/2206.08401)
- [Smart-LLaMA (2024)](https://arxiv.org/abs/2411.06221)
- [Generative LLM Usage in Smart-Contract Vulnerability Detection (2025)](https://arxiv.org/abs/2504.04685)

---

## Recent ArXiv Watchlist (last ~90 days, as of 2026-03-12)

Note: this watchlist is intentionally short and high-signal; verify final inclusion quality when papers leave preprint churn.

- [Towards a Science of AI Agent Reliability (2026-02)](https://arxiv.org/abs/2602.16666)
- [The Convergence of Schema-Guided Dialogue Systems and the Model Context Protocol (2026-02)](https://arxiv.org/abs/2602.18764)
- [Too Helpful to Be Safe: User-Mediated Attacks on Planning and Web-Use Agents (2026-01)](https://arxiv.org/abs/2601.10758)
- [Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents (2026-01)](https://arxiv.org/abs/2601.03515)
- [OmniCode: A Benchmark for Evaluating Software Engineering Agents (2026-02)](https://arxiv.org/abs/2602.02262)
- [Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation (2026-02)](https://arxiv.org/abs/2602.11224)
- [MCP-in-SoS: Risk assessment framework for open-source MCP servers (2026-03)](https://arxiv.org/abs/2603.10194)
- [Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities (2026-03)](https://arxiv.org/abs/2603.10163)

## Monthly Refresh Workflow (template)

Use this on the first week of each month:

1) Pull candidates
- Query arXiv for each category using category keywords and date filter for last 45 days.
- Keep a raw scratch list (20-40 papers total).

2) Apply inclusion gate
- Keep papers that pass at least 3 of 5:
  - Clear method/benchmark contribution
  - Reproducibility artifacts (code/data/eval details)
  - Strong operator relevance (how to build, test, secure, deploy)
  - Non-trivial novelty versus existing map
  - Cross-category leverage (useful outside one niche)

3) Curate final set
- Promote 1-3 papers per category max per month.
- Move low-signal or superseded papers to an archive list.

4) Update repo docs
- Update this map.
- Update README only if a paper changes the practical narrative (for example, reliability ceilings, new benchmark standard).

5) Log rationale
- For each promoted paper, add one-line "why it matters" in commit message or PR body.

Suggested commit format:
- docs(research): monthly arxiv refresh YYYY-MM
