# ArXiv Deep Research Map for Agent Cortex

Purpose: a high-signal arXiv reading map that deepens coverage across the major categories in this repo.

How to use this:
- Start with "Core" papers in each category.
- Use "Expansion" papers when designing or benchmarking production systems.
- Treat benchmark scores as moving targets; always check live leaderboards and method cards.

## 1) Agent Frameworks and Reasoning Loops

Core:
- [ReAct (2022)](https://arxiv.org/abs/2210.03629) - Reasoning + acting loop for tool-using agents.
- [Reflexion (2023)](https://arxiv.org/abs/2303.11366) - Verbal self-feedback for iterative improvement.
- [Toolformer (2023)](https://arxiv.org/abs/2302.04761) - Self-supervised tool-use behavior induction.

Expansion:
- [Generative Agents (2023)](https://arxiv.org/abs/2304.03442) - Memory/planning/reflection architecture in sandbox worlds.
- [A Survey on LLM-based Autonomous Agents (2023)](https://arxiv.org/abs/2308.11432) - Broad architecture landscape.

## 2) Coding Agents

Core:
- [SWE-bench (2023)](https://arxiv.org/abs/2310.06770) - Real GitHub issue resolution benchmark.
- [SWE-bench Multimodal (2024)](https://arxiv.org/abs/2410.03859) - Visual software understanding extension.
- [SWE-bench Goes Live! (2025)](https://arxiv.org/abs/2505.23419) - Live benchmark methodology and updates.

Expansion:
- [SWE-Gym (2024)](https://arxiv.org/abs/2412.21139) - Training environment for SWE agents/verifiers.

## 3) MCP, Tool Use, and Agent Reliability

Core:
- [MCPMark (2025)](https://arxiv.org/abs/2509.24002) - Real-world MCP benchmark (127 tasks).
- [τ-bench (2024)](https://arxiv.org/abs/2406.12045) - Tool-agent-user interaction benchmark with pass^k reliability framing.
- [AgentBench (2023)](https://arxiv.org/abs/2308.03688) - Multi-domain benchmark for LLM agents.

Expansion:
- [GAIA (2023)](https://arxiv.org/abs/2311.12983) - Tool-heavy general-assistant benchmark.

## 4) Web and Computer-Use Agents

Core:
- [WebArena (2023)](https://arxiv.org/abs/2307.13854) - Realistic web-task environment.
- [VisualWebArena (2024)](https://arxiv.org/abs/2401.13649) - Visually grounded web-agent benchmark.
- [OSWorld (2024)](https://arxiv.org/abs/2404.07972) - Open-ended desktop computer-use benchmark.

## 5) Context Engineering and Memory

Core:
- [RAG (2020)](https://arxiv.org/abs/2005.11401) - Retrieval-augmented generation foundation.
- [MemGPT (2023)](https://arxiv.org/abs/2310.08560) - OS-inspired memory hierarchy for LLM agents.
- [Self-RAG (2023)](https://arxiv.org/abs/2310.11511) - Retrieval + critique loop.

Expansion:
- [Lost in the Middle (2023)](https://arxiv.org/abs/2307.03172) - Long-context retrieval/placement failure mode.
- [RETRO (2021)](https://arxiv.org/abs/2112.04426) - Retrieval-heavy architecture with external memory.
- [kNN-LM (2020)](https://arxiv.org/abs/1911.00172) - Non-parametric memory at inference time.

## 6) Prompt and Programmatic Prompt Engineering

Core:
- [Chain-of-Thought (2022)](https://arxiv.org/abs/2201.11903)
- [Self-Consistency (2022)](https://arxiv.org/abs/2203.11171)
- [Tree of Thoughts (2023)](https://arxiv.org/abs/2305.10601)

Expansion:
- [DSPy (2023)](https://arxiv.org/abs/2310.03714) - Compiling declarative LM programs.

## 7) Security and Robustness

Core:
- [Universal and Transferable Adversarial Attacks on Aligned LMs (2023)](https://arxiv.org/abs/2307.15043)
- [StruQ (2024)](https://arxiv.org/abs/2402.06363) - Structured-query defense against prompt injection.
- [SecAlign (2024)](https://arxiv.org/abs/2410.05451) - Preference-optimization defense for prompt injection.

## 8) Voice and Multimodal Agents

Core:
- [Whisper / Robust Speech Recognition via Large-Scale Weak Supervision (2022)](https://arxiv.org/abs/2212.04356)
- [Visual Instruction Tuning (LLaVA, 2023)](https://arxiv.org/abs/2304.08485)

## 9) Evaluation Science and LLM-as-a-Judge

Core:
- [HELM (2022)](https://arxiv.org/abs/2211.09110) - Holistic evaluation framework.
- [MT-Bench and Chatbot Arena / LLM-as-a-Judge analysis (2023)](https://arxiv.org/abs/2306.05685)
- [Systematic Evaluation of LLM-as-a-Judge (2024)](https://arxiv.org/abs/2408.13006)

## 10) Quant and Trading Agents

Core:
- [FinRL Library (2020)](https://arxiv.org/abs/2011.09607)
- [FinRL Framework (2021)](https://arxiv.org/abs/2111.09395)
- [FinRL-Podracer (2021)](https://arxiv.org/abs/2111.05188)

Expansion:
- [Large Language Models in Finance: A Survey (2023)](https://arxiv.org/abs/2311.10723)
- [LLM Agent in Financial Trading: A Survey (2024)](https://arxiv.org/abs/2408.06361)

## 11) Blockchain Identity, Payments, and DeFi Adjacent Research

Core:
- [Deployment of a Blockchain-Based Self-Sovereign Identity (2018)](https://arxiv.org/abs/1806.01926)
- [Design Patterns for Blockchain-based Self-Sovereign Identity (2020)](https://arxiv.org/abs/2005.12112)
- [Decentralized Finance (2023)](https://arxiv.org/abs/2304.01918)

Expansion:
- [Is DeFi Actually Decentralized? (Aave network analysis, 2022)](https://arxiv.org/abs/2206.08401)
- [Smart-LLaMA (2024)](https://arxiv.org/abs/2411.06221) - LLM post-training for smart-contract vulnerability detection.
- [Generative LLM Usage in Smart-Contract Vulnerability Detection (2025)](https://arxiv.org/abs/2504.04685)

---

Suggested maintenance cadence:
- Monthly: refresh benchmark-centric categories (MCP/tool-use/coding/computer-use).
- Quarterly: refresh foundational categories (memory/context/security/multimodal/quant).
- Keep this map opinionated: prefer papers with clear methods, reproducibility artifacts, and practical operator takeaways.
