# Awesome Agent Cortex [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> The sovereign agent stack — practical scripts, on-chain identity, and
> knowledge graphs for AI agents that think, remember, and own themselves.

A curated list covering the full AI agent ecosystem: frameworks, coding agents,
MCP tooling, knowledge graphs, blockchain identity, decentralized finance
agents, quantitative trading, and observability. What makes this list unique is
the combination of practical developer tooling with on-chain identity and memory
infrastructure — resources no other awesome list brings together.

Note: Some resources are intentionally listed in multiple sections when they are
core to more than one workflow domain (for example, prompt + eval, or coding +
CLI usage).

## Contents

- [Agent Frameworks](#agent-frameworks)
- [Coding Agents](#coding-agents)
- [Voice and Multimodal Agents](#voice-and-multimodal-agents)
- [Hermes Stack](#hermes-stack)
- [CLI and TUI Tools](#cli-and-tui-tools)
- [Agent Runtime Infrastructure](#agent-runtime-infrastructure)
- [MCP Ecosystem](#mcp-ecosystem)
- [Prompt Engineering](#prompt-engineering)
- [Agent Harnessing and Evaluation](#agent-harnessing-and-evaluation)
- [ArXiv Deep Research Map](#arxiv-deep-research-map)
- [Context Engineering](#context-engineering)
- [Neural Networks and Neural Linking](#neural-networks-and-neural-linking)
- [Obsidian Vault Architecture for Agents](#obsidian-vault-architecture-for-agents)
- [Agent Security and Robustness](#agent-security-and-robustness)
- [Agent Configs and Dotfiles](#agent-configs-and-dotfiles)
- [Skill Engineering and Playbooks](#skill-engineering-and-playbooks)
- [Knowledge Graphs and Memory](#knowledge-graphs-and-memory)
- [Solana Agent Infrastructure](#solana-agent-infrastructure)
- [Agent Identity and Wallets](#agent-identity-and-wallets)
- [Agent Payments](#agent-payments)
- [DeFi Agents](#defi-agents)
- [Quant and Trading Agents](#quant-and-trading-agents)
- [Agent Observability and Testing](#agent-observability-and-testing)
- [Research Papers](#research-papers)
- [Communities](#communities)

## Agent Frameworks

Multi-agent orchestration, single-agent SDKs, and runtime frameworks.

- [AG2](https://github.com/ag2ai/ag2) - Open-source AgentOS for building multi-agent systems (evolved from AutoGen).
- [Agno](https://github.com/agno-agi/agno) - Framework for building and running agentic software at scale.
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework from Microsoft Research.
- [Claude Agent SDK](https://github.com/anthropics/anthropic-sdk-python) - Official Python SDK for building agents with Claude models.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based multi-agent orchestration framework.
- [ElizaOS](https://github.com/elizaOS/eliza) - Multi-agent simulation framework for autonomous characters.
- [Google A2A](https://github.com/google/A2A) - Agent-to-Agent protocol for cross-framework agent communication.
- [Google ADK](https://github.com/google/adk-python) - Agent Development Kit for building agents with Gemini.
- [Haystack](https://github.com/deepset-ai/haystack) - LLM orchestration framework for building search and RAG pipelines.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Tool-using autonomous agent platform with memory, skills, delegation, and MCP support.
- [Julep](https://github.com/julep-ai/julep) - Stateful agent platform with built-in persistence and task workflows.
- [LangChain](https://github.com/langchain-ai/langchain) - Composable framework for building LLM-powered applications.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Library for building stateful multi-agent workflows as graphs.
- [Letta](https://github.com/letta-ai/letta) - Stateful agents with long-term memory (formerly MemGPT).
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for document agents, retrieval, and workflow orchestration.
- [Magentic-One](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one) - Multi-agent team for complex web and file tasks.
- [Mastra](https://github.com/mastra-ai/mastra) - TypeScript framework for building AI applications and agents.
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Framework for building, orchestrating, and deploying agents with Python and .NET support.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Official SDK for building agents with OpenAI models.
- [OpenClaw](https://github.com/openclaw/openclaw) - Self-hosted personal AI agent with multi-platform messaging and skill registry.
- [Phidata](https://github.com/phidatahq/phidata) - Toolkit for building AI assistants with memory and tools.
- [PydanticAI](https://github.com/pydantic/pydantic-ai) - Type-safe agent framework built around Pydantic.
- [Rig](https://github.com/0xPlaygrounds/rig) - Rust framework for building LLM-powered applications.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - SDK for integrating LLMs into apps with plugin architecture.
- [Smolagents](https://github.com/huggingface/smolagents) - Lightweight agent framework from Hugging Face.
- [Swarm](https://github.com/openai/swarm) - Educational framework for multi-agent handoffs and routines.

## Coding Agents

AI agents that write, review, and debug code.

- [Aider](https://github.com/Aider-AI/aider) - AI pair programming in the terminal with git integration.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic's agentic CLI for code generation and editing.
- [Cline](https://github.com/cline/cline) - Autonomous coding agent for VS Code with tool use.
- [Continue](https://github.com/continuedev/continue) - Open-source AI code assistant for VS Code and JetBrains.
- [Cursor](https://cursor.com) - AI-first code editor built on VS Code.
- [Devin](https://devin.ai) - Autonomous software engineering agent by Cognition.
- [Goose](https://github.com/block/goose) - Autonomous developer agent from Block.
- [OpenCodex](https://github.com/openai/codex) - OpenAI's CLI coding agent.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Platform for AI software development agents (formerly OpenDevin).
- [SWE-Agent](https://github.com/princeton-nlp/SWE-agent) - Agent for automatically resolving GitHub issues.
- [Windsurf](https://codeium.com/windsurf) - AI-native IDE by Codeium with agentic flows.

### Claude Code Resources

- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Curated list of Claude Code resources.
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) - Event-driven shell command automation.
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/memory#slash-commands-as-custom-skills) - Reusable prompt-driven workflows.
- [CLAUDE.md Guide](https://docs.anthropic.com/en/docs/claude-code/memory) - Official documentation on memory files.
- [claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Community-sourced tips and tricks.
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) - Comprehensive Claude Code harness with agent skills, hooks, and multi-language support.

### Codex Resources

- [Codex Docs](https://developers.openai.com/codex) - Official Codex documentation hub.
- [Codex CLI](https://developers.openai.com/codex/cli) - Guide to local Codex CLI workflows.
- [Codex Non-Interactive Mode](https://developers.openai.com/codex/noninteractive) - Batch and CI automation with `codex exec`.
- [AGENTS.md Guide (Codex)](https://developers.openai.com/codex/guides/agents-md) - Instruction hierarchy and scoping patterns for Codex.
- [Codex Optimization Playbook (this repo)](guides/codex-optimization-playbook.md) - Practical operator patterns for speed, safety, and quality.

## Voice and Multimodal Agents

Agents with voice, vision, and multimodal capabilities.

- [ElevenLabs](https://github.com/elevenlabs/elevenlabs-python) - Text-to-speech and voice cloning API for agent voice interfaces.
- [LiveKit Agents](https://github.com/livekit/agents) - Framework for building real-time multimodal AI agents.
- [Pipecat](https://github.com/pipecat-ai/pipecat) - Framework for building voice and multimodal conversational agents.
- [TEN Framework](https://github.com/TEN-framework/ten-framework) - Open-source framework for conversational voice AI agents.
- [Ultravox](https://github.com/fixie-ai/ultravox) - Fast multimodal LLM for real-time voice AI.
- [Vapi](https://vapi.ai) - Platform for building and deploying voice AI agents.
- [Vocode Core](https://github.com/vocodedev/vocode-core) - Modular open-source framework for building voice-based LLM agents.
- [Whisper](https://github.com/openai/whisper) - Open-source speech recognition model from OpenAI.

## Hermes Stack

Hermes Agent runtime, deployment rails, and operator resources.

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Open-source autonomous AI agent with CLI, gateway, memory, subagents, and broad tool integrations.
- [Hermes Hub (this repo)](hermes/README.md) - Local operator knowledge base for Hermes setup, configuration, memory/skills workflows, and contribution orientation.
- [Hermes Agent + hermes-fly Best Practices (this repo)](guides/hermes-agent-hermes-fly-playbook.md) - Practical setup, operations, security, and optimization playbook.
- [Hermes Agent Optimization Playbook (this repo)](guides/hermes-agent-optimization-playbook.md) - Deep operator guide for context, delegation, memory, and execution tuning.
- [Hermes Agent Self-Evolution](https://github.com/NousResearch/hermes-agent-self-evolution) - Evolutionary self-improvement framework for optimizing Hermes Agent prompts, skills, and code.
- [Hermes Paperclip Adapter](https://github.com/NousResearch/hermes-paperclip-adapter) - Adapter for running Hermes Agent as a managed employee inside Paperclip.
- [hermes-fly](https://github.com/alexfazio/hermes-fly) - Fly.io deployment and operations CLI for Hermes Agent with deploy, logs, doctor, and teardown workflows.
- [Hermes Stack Maturity Ladder (this repo)](guides/hermes-stack-maturity-ladder.md) - L1-L3 readiness model with upgrade paths and operational checklist.
- [Hermes Stack Quickstart Recipes (this repo)](guides/hermes-stack-quickstart-recipes.md) - Copy/paste recipes for local dev, hosted production, secure mode, and CI operations.

## CLI and TUI Tools

Terminal-based agent interfaces and developer tools.

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Agentic CLI that operates directly in the terminal.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's command-line interface for Gemini models.
- [Glow](https://github.com/charmbracelet/glow) - Terminal Markdown renderer useful for agent output.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - CLI and gateway agent runtime with tools, memory, delegation, and automation support.
- [hermes-fly](https://github.com/alexfazio/hermes-fly) - CLI wizard to deploy and operate Hermes Agent on Fly.io.
- [lazygit](https://github.com/jesseduffield/lazygit) - Terminal UI for git commonly paired with coding agents.
- [llm](https://github.com/simonw/llm) - CLI tool for interacting with LLMs from the terminal.
- [aichat](https://github.com/sigoden/aichat) - All-in-one LLM CLI with chat, shell assistant, RAG, and agent features.
- [OpenCodex](https://github.com/openai/codex) - Lightweight CLI coding agent from OpenAI.
- [sgpt](https://github.com/tbckr/sgpt) - Command-line productivity tool powered by LLMs.
- [tmux](https://github.com/tmux/tmux) - Terminal multiplexer for running agents in persistent sessions.
- [Warp](https://www.warp.dev) - Modern terminal with built-in AI assistance.
- [Zellij](https://github.com/zellij-org/zellij) - Terminal workspace with plugin system for agent integration.

## Agent Runtime Infrastructure

Execution sandboxes and runtime platforms for safely running agent actions and generated code.

- [CUA](https://github.com/trycua/cua) - Open-source infrastructure for computer-use agents with sandboxes, SDKs, and benchmarks.
- [Daytona](https://github.com/daytonaio/daytona) - Secure and elastic runtime infrastructure for AI-generated code execution.
- [E2B](https://github.com/e2b-dev/E2B) - Open-source secure cloud sandbox environment for AI agents.
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - Secure and fast microVM technology for isolated agent execution.
- [gVisor](https://github.com/google/gvisor) - Application kernel for containers that adds a strong isolation boundary.
- [Kata Containers](https://github.com/kata-containers/kata-containers) - Lightweight VM-based container runtime for stronger workload isolation.
- [Modal](https://modal.com) - Serverless compute platform often used for running agent workloads and tools.
- [RunPod Python SDK](https://github.com/runpod/runpod-python) - Python SDK for RunPod serverless and worker-based AI workloads.

## MCP Ecosystem

Model Context Protocol servers, clients, and tooling.

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Curated list of MCP server implementations.
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) - Official Chrome DevTools MCP server for coding and browser automation agents.
- [FastMCP](https://github.com/PrefectHQ/fastmcp) - Pythonic framework for building MCP servers and clients quickly.
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - Official MCP server for GitHub workflows and repository actions.
- [mcp](https://github.com/modelcontextprotocol/servers) - Official reference MCP server implementations.
- [MCP Agent](https://github.com/lastmile-ai/mcp-agent) - Framework patterns for building agents on top of MCP.
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - Cross-language curriculum and practical examples for learning MCP.
- [MCP Go SDK](https://github.com/mark3labs/mcp-go) - Go implementation of the Model Context Protocol.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Official inspector and debugging tool for MCP servers.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK for building MCP servers.
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - Community registry service for discovering MCP servers.
- [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Official Rust SDK for building MCP servers.
- [MCP Spec](https://modelcontextprotocol.io/specification) - Official Model Context Protocol specification.
- [MCP Specification Repo](https://github.com/modelcontextprotocol/modelcontextprotocol) - Canonical specification and documentation repository.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Official TypeScript SDK for building MCP servers.
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - MCP server for browser automation via Playwright.
- [Smithery](https://smithery.ai) - Registry and hosting platform for MCP servers.

## Prompt Engineering

Instruction-writing craft: system prompts, response framing, and reusable prompt templates.
Focus here on *what to ask and how to phrase it* at the prompt layer.

- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library) - Official prompt examples from Anthropic.
- [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) - Collection of prompt examples for ChatGPT.
- [Claude System Prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) - Guide to writing effective system prompts.
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - Official guide to designing reliable prompts and instruction patterns.
- [DSPy](https://github.com/stanfordnlp/dspy) - Framework for programming with foundation models instead of prompting.
- [fabric](https://github.com/danielmiessler/fabric) - Framework for augmenting humans using AI with curated prompts.
- [LangChain Hub](https://smith.langchain.com/hub) - Community-driven prompt and chain sharing platform.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - Testing and evaluation framework for LLM prompts.
- [System Prompts](https://github.com/mustvlad/ChatGPT-System-Prompts) - Collection of system prompts for various AI models.

## Agent Harnessing and Evaluation

Harnesses, benchmarks, and evaluation frameworks for measuring agent quality and reliability.

### Benchmark Reality Check (real-world tool use)

- [MCPMark (paper)](https://arxiv.org/abs/2509.24002) - 127-task MCP benchmark; reports best pass@1 at 52.56% (gpt-5-medium), with several strong models below 30% pass@1.
- [MCPMark (leaderboard)](https://mcpmark.ai/) - Live model comparisons for realistic MCP task execution.
- [τ-bench](https://arxiv.org/abs/2406.12045) - Tool-agent-user benchmark; reports strong function-calling agents still below 50% task success in its setup.
- [OSWorld](https://arxiv.org/abs/2404.07972) - Open-ended computer-use benchmark; reports best model 12.24% vs 72.36% human success in initial results.
- [WebArena](https://arxiv.org/abs/2307.13854) - Realistic web-task benchmark; reports best GPT-4-based agent at 14.41% vs 78.24% human.
- [GAIA](https://arxiv.org/abs/2311.12983) - General assistant benchmark; original framing reports large human-model gap on tool-heavy questions.

- [AgentBench](https://github.com/THUDM/AgentBench) - Multi-domain benchmark suite for evaluating LLMs as agents.
- [AgentEvals](https://github.com/langchain-ai/agentevals) - Evaluation utilities for scoring agent trajectories and outcomes.
- [AutoGen agbench](https://github.com/microsoft/autogen/blob/main/python/packages/agbench/README.md) - Benchmark runner for AutoGen agent workflows.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) - Gym-style environment for training and evaluating browser agents.
- [browser-use](https://github.com/browser-use/browser-use) - Framework for browser task automation and agent web interaction loops.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - Open-source framework for reproducible LLM and agent evaluations.
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) - Open robustness benchmark for measuring jailbreak resistance in language models and agents.
- [MCPMark](https://github.com/eval-sys/mcpmark) - Stress-testing benchmark for evaluating model and agent capability on MCP tasks.
- [MLE-bench](https://github.com/openai/mle-bench) - Benchmark harness for autonomous ML engineering tasks.
- [OSWorld](https://github.com/xlang-ai/OSWorld) - Open-ended benchmark environment for desktop computer-use agents.
- [OpenCUA](https://github.com/xlang-ai/OpenCUA) - Open foundation stack for building and evaluating computer-use agents.
- [Stagehand](https://github.com/browserbase/stagehand) - Browser automation framework for agentic web workflows and reproducible runs.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Canonical benchmark for coding agents on real GitHub issue tasks.
- [Tau-Bench](https://github.com/sierra-research/tau-bench) - Realistic interactive benchmark for measuring agent reliability.
- [WebArena](https://github.com/web-arena-x/webarena) - Real-world web task benchmark environment for browser agents.
- [WorkArena](https://github.com/ServiceNow/WorkArena) - Enterprise task benchmark for browser-based agent workflows.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - Security and robustness benchmark suite for tool-using agents.
- [AppWorld](https://github.com/StonyBrookNLP/appworld) - Multi-application environment for benchmarking autonomous task completion.
- [AgentLab](https://github.com/ServiceNow/AgentLab) - Research platform for developing and evaluating web agents.
- [ALFWorld](https://alfworld.github.io/) - Interactive long-horizon benchmark environment for embodied planning agents.
- [HELM](https://crfm.stanford.edu/helm/latest/) - Standardized evaluation framework for model and agent behavior comparison.
- [GAIA Benchmark](https://huggingface.co/gaia-benchmark) - Realistic benchmark for tool-using, multi-step general assistant tasks.
- [Agent Harnessing Playbook (this repo)](guides/agent-harnessing-playbook.md) - Practical framework for benchmark design, regression gates, and release readiness.

## ArXiv Deep Research Map

Deep-dive reading map organized by the major categories in this repository.

- [ArXiv Deep Research Map (this repo)](guides/arxiv-deep-research-map.md) - Curated paper paths with per-category must-reads, a recent watchlist, and a monthly refresh workflow across frameworks, coding, MCP/tool use, eval reliability, memory, security, multimodal, quant, and on-chain/DeFi-adjacent research.

## Context Engineering

Systems-level context design: memory, retrieval, compression, routing, and long-horizon state management.
Focus here on *what information the model gets, when, and in what form*.

- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) - Engineering principles for building reliable, production-grade LLM agents.
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - Practical engineering patterns for agent design and execution loops.
- [Anthropic: Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) - Retrieval architecture guidance for improving grounding and precision.
- [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Production guidance for context composition and lifecycle management.
- [Anthropic: Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) - Patterns for long-horizon orchestration and reliability.
- [LangChain: Context Engineering for Agents](https://blog.langchain.com/context-engineering-for-agents/) - Practical taxonomy for writing, selecting, compressing, and isolating context.
- [Manus: Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) - Practitioner lessons from building production autonomous workflows.
- [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals) - Official framework for building eval loops and quality gates.
- [OpenAI Cookbook: Getting Started with Evals](https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals) - Practical eval setup walkthrough.
- [RAG (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) - Foundational retrieval-augmented generation paper.
- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2203.02155) - Foundational reasoning/prompting technique paper.
- [Lost in the Middle (Liu et al., 2023)](https://arxiv.org/abs/2307.03172) - Key long-context failure analysis paper.
- [Context Engineering Playbook (this repo)](guides/context-engineering-playbook.md) - Practical context budget, memory, retrieval, and anti-drift checklist.
- [Agent Operator Trend Signals (this repo)](guides/agent-operator-trend-signals-2026.md) - Synthesized practitioner themes for harness and context strategy.

## Neural Networks and Neural Linking

Neural memory, retrieval, and graph-linking foundations relevant to advanced agent cognition.

- [Neural Turing Machines (2014)](https://arxiv.org/abs/1410.5401) - Foundational differentiable external-memory architecture.
- [End-to-End Memory Networks (2015)](https://arxiv.org/abs/1503.08895) - Multi-hop memory lookup architecture for iterative reasoning.
- [Differentiable Neural Computer (2016)](https://arxiv.org/abs/1605.08582) - Enhanced neural memory addressing for long-horizon reasoning.
- [Transformer-XL (2019)](https://arxiv.org/abs/1901.02860) - Segment-level recurrence for long-context memory reuse.
- [Compressive Transformer (2019)](https://arxiv.org/abs/1911.05507) - Compressed memory tiers for scalable sequence retention.
- [RAG (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) - Canonical retrieval-augmented generation architecture.
- [kNN Language Models (2020)](https://arxiv.org/abs/1911.00172) - Non-parametric memory retrieval at inference time.
- [RETRO (2021)](https://arxiv.org/abs/2112.04426) - Retrieval-heavy architecture for efficient knowledge access.
- [Neural Bellman-Ford Networks (2021)](https://arxiv.org/abs/2106.06935) - Graph neural reasoning for multi-hop relational inference.
- [DeepProbLog](https://github.com/ML-KULeuven/deepproblog) - Neural-symbolic framework combining perception models and logic rules.
- [Neural Linking and Memory Playbook (this repo)](guides/neural-linking-memory-playbook.md) - Practical guide for agent memory architectures and neural-symbolic linking patterns.

## Obsidian Vault Architecture for Agents

Obsidian-specific architecture patterns and APIs for using vaults as agent memory backends.

- [How Obsidian Stores Data](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data) - Canonical vault-on-disk model and config layout.
- [Obsidian Properties](https://help.obsidian.md/Editing+and+formatting/Properties) - Structured metadata schema for machine-readable note attributes.
- [Obsidian Plugin Guide](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin) - Official plugin architecture and lifecycle entrypoint.
- [Obsidian TypeScript API (Vault)](https://docs.obsidian.md/Reference/TypeScript+API/Vault) - Programmatic CRUD layer for vault files.
- [obsidian-api](https://github.com/obsidianmd/obsidian-api) - Official API type definitions for plugin development.
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview) - Query engine for structured note metadata and graph-aware retrieval.
- [Juggl](https://github.com/HEmile/juggl) - Advanced graph exploration plugin for complex link topology workflows.
- [Local REST API Plugin](https://github.com/coddingtonbear/obsidian-local-rest-api) - Local HTTP interface for external agent integrations.
- [Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) - URI-based automation hooks for cross-tool workflows.
- [Obsidian Git](https://github.com/Vinzent03/obsidian-git) - Versioned vault operations for auditable agent writes.
- [Obsidian Vault Architecture Playbook (this repo)](guides/obsidian-vault-architecture-playbook.md) - Reference architecture and operational patterns for agent-connected Obsidian systems.

## Agent Security and Robustness

Safety, red-teaming, and robustness tools for hardening agent behavior.

- [garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanning and red-teaming toolkit for security testing.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Validation and safety guardrails framework for LLM outputs.
- [Invariant](https://github.com/invariantlabs-ai/invariant) - Guardrails framework for secure and robust agent development.
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) - Open robustness benchmark for measuring jailbreak resistance in language models and agents.
- [llm-attacks](https://github.com/llm-attacks/llm-attacks) - Reference implementation and resources for adversarial jailbreak attack evaluation.
- [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) - Official security guidance for MCP authorization flows, threats, and mitigations.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Toolkit for adding programmable safety and policy guardrails to LLM systems.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - Red-teaming and robustness testing toolkit for LLM systems.
- [PyRIT](https://github.com/Azure/PyRIT) - Python Risk Identification Tool for proactively testing generative AI security risks.

## Agent Configs and Dotfiles

Configuration files and workflow examples for AI coding tools.

- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) - Curated list of Cursor rule files.
- [Claude Code Memory Files](https://docs.anthropic.com/en/docs/claude-code/memory) - Guide to CLAUDE.md and project memory.
- [Claude Code Starter Configs](claude/) - Ready-to-use CLAUDE.md, rules, hooks, and skills for Claude Code projects.
- [Codex CLI Starter Configs](codex/) - Ready-to-use AGENTS.md and config for OpenAI Codex CLI projects.
- [Cursor Starter Configs](cursorrules/) - Ready-to-use .cursorrules and rule files for Cursor projects.
- [CursorDirectory](https://cursor.directory) - Community-shared Cursor rules and configurations.
- [dotfiles](https://dotfiles.github.io) - Guide to managing dotfiles including agent configurations.
- [Trail of Bits Claude Code Config](https://github.com/trailofbits/claude-code-config) - Opinionated Claude Code defaults and workflows from a security-focused engineering team.

## Skill Engineering and Playbooks

Hands-on resources for designing, testing, and shipping high-quality agent skills.

- [Anthropic: The Complete Guide to Building Skills for Claude (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) - Canonical end-to-end guide covering structure, triggering, testing, and distribution.
- [anthropics/skills](https://github.com/anthropics/skills) - Official production-ready skill examples and reference implementations.
- [Claude Skill Engineering Playbook (this repo)](guides/claude-skill-engineering-playbook.md) - Distilled patterns, anti-patterns, templates, and troubleshooting from the Anthropic guide.
- [Claude Skills Quickstart Checklist (this repo)](guides/claude-skills-quickstart-checklist.md) - Build-test-ship checklist for repeatable skill quality.

## Knowledge Graphs and Memory

Agent memory architectures, knowledge graphs, and second-brain integrations.

- [Cognee](https://github.com/topoteretes/cognee) - Memory management layer for LLM apps using knowledge graphs.
- [FalkorDB](https://github.com/FalkorDB/FalkorDB) - Ultra-fast graph database for AI agent knowledge.
- [Graphiti](https://github.com/getzep/graphiti) - Real-time knowledge graph framework for AI agents.
- [GraphRAG](https://github.com/microsoft/graphrag) - Graph-based retrieval augmented generation from Microsoft.
- [Khoj](https://github.com/khoj-ai/khoj) - Personal AI assistant with long-term memory and knowledge search.
- [LangMem](https://github.com/langchain-ai/langmem) - Memory management toolkit for building long-horizon agent systems.
- [LightRAG](https://github.com/HKUDS/LightRAG) - Simple and fast RAG framework using graph structures.
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI assistants and agents.
- [Memgraph](https://github.com/memgraph/memgraph) - In-memory graph database for real-time agent queries.
- [Neo4j](https://github.com/neo4j/neo4j) - Graph database platform widely used for agent knowledge stores.
- [Obsidian](https://obsidian.md) - Knowledge base and note-taking app usable as agent memory backend.
- [obsidian-graph-query](https://github.com/azuma520/obsidian-graph-query) - Query and traverse Obsidian vault graphs programmatically.
- [ODIN](https://github.com/memgraph/odin) - Knowledge graph construction tool built on Memgraph.
- [Pinecone](https://www.pinecone.io) - Vector database for semantic memory and retrieval.
- [Qdrant](https://github.com/qdrant/qdrant) - High-performance vector search engine for agent memory.
- [txtai](https://github.com/neuml/txtai) - All-in-one embeddings database for semantic search and workflows.
- [Weaviate](https://github.com/weaviate/weaviate) - Vector database with built-in modules for AI workloads.
- [Zep](https://github.com/getzep/zep) - Memory infrastructure and retrieval stack for AI assistants and agents.

## Solana Agent Infrastructure

Tools and SDKs for building AI agents on Solana.

- [Anchor](https://github.com/solana-foundation/anchor) - Core Solana framework for building and integrating smart contracts and clients.
- [Awesome Solana AI](https://github.com/solana-foundation/awesome-solana-ai) - Solana Foundation's curated list of AI-Solana projects.
- [GOAT SDK](https://github.com/goat-sdk/goat) - Open-source toolkit connecting AI agents to 200+ on-chain tools across Solana and EVM chains.
- [Helius SDK](https://github.com/helius-labs/helius-sdk) - TypeScript SDK for Solana RPC, webhooks, and DAS API.
- [Jito-Solana](https://github.com/jito-foundation/jito-solana) - MEV-aware Solana client infrastructure for advanced execution agents.
- [Jupiter Swap API Docs](https://dev.jup.ag/docs/swap-api) - Official documentation for integrating Jupiter routing and swaps.
- [LangChain Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit) - LangChain tools for Solana agent operations.
- [Light Protocol](https://github.com/Lightprotocol/light-protocol) - ZK compression for scalable on-chain agent state.
- [Metaplex](https://github.com/metaplex-foundation/metaplex-program-library) - Solana programs for NFTs and digital assets used in agent identity.
- [Pyth Crosschain](https://github.com/pyth-network/pyth-crosschain) - Oracle infrastructure for low-latency market data used by agent strategies.
- [Solana Actions](https://github.com/solana-developers/solana-actions) - Spec and tools for blockchain-powered actions and blinks.
- [Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit) - Toolkit for connecting AI agents to Solana protocols.
- [Solana Kit](https://github.com/anza-xyz/kit) - Modern Solana client SDK stack for building high-quality applications and agents.
- [Solana Web3.js](https://github.com/solana-labs/solana-web3.js) - JavaScript SDK for interacting with the Solana blockchain.
- [Switchboard Solana SDK](https://github.com/switchboard-xyz/solana-sdk) - Verifiable oracle and data-feed SDK for agent decision systems.
- [Yellowstone gRPC](https://github.com/rpcpool/yellowstone-grpc) - High-throughput real-time Solana data streams for low-latency agents and indexers.
- [Solana Agent Architecture Playbook (this repo)](guides/solana-agent-architecture-playbook.md) - Reference architecture, security controls, and ops checklist for production Solana agents.

## Agent Identity and Wallets

On-chain identity, wallets, and trust infrastructure for autonomous AI agents.

- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - Toolkit for giving AI agents programmable wallet capabilities.
- [Crossmint](https://www.crossmint.com) - Wallet-as-a-service for agent-owned wallets and NFT minting.
- [EIP-1271](https://eips.ethereum.org/EIPS/eip-1271) - Standard for contract wallet signature validation in dapps and agent auth flows.
- [EIP-4337](https://eips.ethereum.org/EIPS/eip-4337) - Account abstraction standard enabling programmable smart accounts for agents.
- [EIP-4361 (SIWE)](https://eips.ethereum.org/EIPS/eip-4361) - Sign-In with Ethereum standard for wallet-based authentication.
- [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) - EOA delegation model for temporary smart-account-like behavior.
- [ERC-7579](https://ercs.ethereum.org/ERCS/erc-7579) - Modular smart account standard for plugin-based permissions and execution.
- [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) - Proposed standard for cross-chain agent identity.
- [Lit Protocol](https://github.com/LIT-Protocol/js-sdk) - Decentralized key management and programmable signing.
- [Privy](https://www.privy.io) - Embedded wallet infrastructure for agent authentication.
- [Safe](https://github.com/safe-global/safe-smart-account) - Multi-signature smart account for EVM agent treasuries.
- [Sign-In With Solana](https://github.com/phantom/sign-in-with-solana) - Wallet-native authentication pattern for Solana apps and agents.
- [Solana Agent Identity](https://github.com/sendaifun/solana-agent-kit) - Agent wallet and identity features in Solana Agent Kit.
- [Squads Protocol](https://github.com/Squads-Protocol/v4) - Multisig and smart account protocol for Solana agents.
- [Turnkey](https://www.turnkey.com) - Secure key infrastructure for programmatic wallet management.
- [UCAN](https://github.com/ucan-wg/spec) - User-controlled authorization for decentralized agent capabilities.
- [AIP (Agent Identity Protocol)](https://github.com/The-Nexus-Guard/aip) - Cryptographic identity, trust vouching, and encrypted messaging for AI agents. Ed25519 signatures, W3C Verifiable Credentials, behavioral trust scoring (PDR). `pip install aip-identity`.

## Agent Payments

Payment protocols and infrastructure for autonomous agent transactions.

- [Awesome x402](https://github.com/Merit-Systems/awesome-x402) - Curated resources for the x402 payment protocol ecosystem.
- [Coinbase Agentic Wallets](https://www.coinbase.com/developer-platform/discover/launches/agentic-wallets) - Wallet infrastructure for AI agents with programmable spending limits.
- [Google A2A x402 Extension](https://github.com/google-agentic-commerce/a2a-x402) - Cryptocurrency payments for the Agent-to-Agent protocol via x402.
- [lobster.cash](https://www.lobster.cash) - Agent payment solution on Solana with Visa Intelligent Commerce integration by Crossmint.
- [Request Network](https://request.network) - Crypto-native invoicing and payment request rails for agent billing workflows.
- [Solana Pay](https://solanapay.com) - Open payments standard for Solana-based checkout and transfer flows.
- [Superfluid](https://superfluid.org) - Streaming payment primitives for machine-to-machine and agent subscriptions.
- [x402 Foundation](https://www.x402.org) - Open protocol foundation governing the x402 payment standard.
- [x402 Protocol](https://github.com/coinbase/x402) - Open HTTP payment protocol using the 402 status code for agent-to-service payments.

## DeFi Agents

AI agents for decentralized finance operations and strategy.

- [Autonolas](https://github.com/valory-xyz/open-autonomy) - Framework for building autonomous agent services on-chain.
- [DeFi Llama API](https://defillama.com/docs/api) - Open API for DeFi protocol data used by trading agents.
- [Drift Protocol v2](https://github.com/drift-labs/protocol-v2) - On-chain perpetuals protocol infrastructure for autonomous trading agents.
- [ElizaOS DeFi Plugins](https://github.com/elizaOS/eliza/tree/main/packages) - DeFi protocol integrations for ElizaOS agents.
- [Gauntlet](https://www.gauntlet.xyz) - Risk management and simulation platform for DeFi agents.
- [Griffain](https://griffain.com) - AI agent platform for Solana DeFi operations.
- [Kamino KLend SDK](https://github.com/Kamino-Finance/klend-sdk) - Lending protocol SDK for credit and yield allocation agents.
- [Lulo](https://lulo.fi) - Yield optimization protocol with agent-friendly APIs.
- [Orca Whirlpools SDK](https://github.com/orca-so/whirlpools) - Solana concentrated liquidity SDK for agent strategies.
- [Raydium SDK](https://github.com/raydium-io/raydium-sdk-V2) - Solana AMM SDK for agent-driven liquidity provision.
- [Spectral Finance](https://www.spectral.finance) - On-chain credit scoring and risk models for agent decisions.
- [Virtuals Protocol](https://www.virtuals.io) - Agent tokenization and autonomous commerce protocol tracking agentic GDP.
- [Yearn Vaults](https://github.com/yearn/yearn-vaults-v3) - Automated yield vaults usable as agent strategy backends.

## Quant and Trading Agents

Quantitative finance frameworks and AI-driven trading systems.

- [AlphaAgent](https://github.com/LLMQuant/AlphaAgent) - LLM-powered agent for quantitative trading research.
- [BitQuant](https://github.com/OpenGradient/BitQuant) - Multi-agent quantitative analysis framework.
- [DriftPy](https://github.com/drift-labs/driftpy) - Python SDK for building Solana-based perp and risk management agents.
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Open-source financial LLM framework.
- [FinRL](https://github.com/AI4Finance-Foundation/FinRL) - Deep reinforcement learning library for quantitative finance.
- [Freqtrade](https://github.com/freqtrade/freqtrade) - Open-source algorithmic trading bot in Python.
- [Hummingbot](https://github.com/hummingbot/hummingbot) - Open-source market making and arbitrage bot.
- [Lean](https://github.com/QuantConnect/Lean) - Algorithmic trading engine by QuantConnect.
- [NautilusTrader](https://github.com/nautechsystems/nautilus_trader) - High-performance algorithmic trading platform in Rust and Python.
- [Phoenix v1](https://github.com/Ellipsis-Labs/phoenix-v1) - On-chain central limit order book protocol for low-latency execution agents.
- [Qlib](https://github.com/microsoft/qlib) - AI-oriented quantitative investment platform from Microsoft.
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) - Multi-agent LLM framework simulating a trading firm.
- [VectorBT](https://github.com/polakowo/vectorbt) - Fast backtesting and analysis library for trading strategies.
- [Zipline](https://github.com/stefan-jansen/zipline-reloaded) - Pythonic algorithmic trading library for backtesting.

## Agent Observability and Testing

Debugging, tracing, evaluation, and testing tools for AI agents.

- [AgentOps](https://github.com/AgentOps-AI/agentops) - Monitoring, cost tracking, and benchmarking for agent workflows.
- [Braintrust](https://www.braintrust.dev) - Evaluation and observability platform for AI products.
- [DeepEval](https://github.com/confident-ai/deepeval) - Open-source LLM evaluation framework.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability and monitoring platform.
- [LangFuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform for tracing and evaluation.
- [LangSmith](https://smith.langchain.com) - Platform for debugging, testing, and monitoring LLM applications.
- [LiteLLM](https://github.com/BerriAI/litellm) - LLM gateway and proxy with logging, cost tracking, and routing controls.
- [OpenAI Evals](https://github.com/openai/evals) - Framework and benchmark registry for evaluating LLM systems.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry-based observability for LLM applications.
- [Opik](https://github.com/comet-ml/opik) - Open-source platform for LLM and agent tracing, evaluation, and monitoring.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability platform from Arize.
- [Portkey](https://github.com/Portkey-AI/gateway) - AI gateway with observability, caching, and fallback routing.
- [SigNoz](https://github.com/SigNoz/signoz) - OpenTelemetry-native observability platform for traces, logs, and metrics.
- [TruLens](https://github.com/truera/trulens) - Open-source framework for evaluating and tracking LLM and agent experiments.
- [Weave](https://github.com/wandb/weave) - Toolkit for tracking and evaluating LLM applications from W&B.

## Research Papers

Curated papers on AI agents, multi-agent systems, and agent infrastructure.

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Comprehensive survey of LLM-based agent architectures.
- [ArXiv Deep Research Map (this repo)](guides/arxiv-deep-research-map.md) - Category-by-category reading map spanning frameworks, coding, MCP/tool use, memory, security, multimodal, and quant/on-chain adjacent domains.
- [Awesome AI Agent Papers](https://github.com/VoltAgent/awesome-ai-agent-papers) - Continuously updated collection of agent research papers.
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) - Foundational paper on reasoning in language models.
- [Generative Agents](https://arxiv.org/abs/2304.03442) - Simulating human behavior with LLM-driven agents in a sandbox.
- [MemGPT](https://arxiv.org/abs/2310.08560) - OS-inspired memory management for LLM context windows.
- [ReAct](https://arxiv.org/abs/2210.03629) - Synergizing reasoning and acting in language models.
- [Reflexion](https://arxiv.org/abs/2303.11366) - Language agents with verbal reinforcement learning.
- [The Landscape of Emerging AI Agent Architectures](https://arxiv.org/abs/2404.11584) - Survey of multi-agent design patterns.
- [Toolformer](https://arxiv.org/abs/2302.04761) - Language models that learn to use tools autonomously.
- [Voyager](https://arxiv.org/abs/2305.16291) - Open-ended embodied agent with LLM-powered curriculum.

## Communities

Forums, Discord servers, newsletters, and social accounts.

- [AI Agent Discord Servers](https://discord.gg/crewai) - CrewAI community Discord.
- [Anthropic Discord](https://discord.gg/anthropic) - Official Anthropic community.
- [ElizaOS Discord](https://discord.gg/elizaos) - Community for ElizaOS agent builders.
- [LangChain Discord](https://discord.gg/langchain) - LangChain developer community.
- [Latent Space Podcast](https://www.latent.space) - Podcast covering AI engineering and agents.
- [r/artificial](https://www.reddit.com/r/artificial/) - Subreddit for AI discussions and news.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) - Community for local LLM deployment and agent experimentation.
- [Solana AI Discord](https://discord.gg/solana) - Solana developer community with AI channels.

---

## Contributing

Contributions welcome. Read the [contribution guidelines](CONTRIBUTING.md) first.

## ❤️ Support the Project

If you find this project useful, consider supporting my open-source work.

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support-orange?logo=buymeacoffee)](https://buymeacoffee.com/nyk_builderz)

**Solana donations**

`BYLu8XD8hGDUtdRBWpGWu5HKoiPrWqCxYFSh4oxXuvPg`

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and
related or neighboring rights to this work.

---


<p align="center">
  <a href="https://star-history.com/#0xNyk/awesome-agent-cortex&Date">
    <img src="https://api.star-history.com/svg?repos=0xNyk/awesome-agent-cortex&type=Date" alt="Star History" width="400">
  </a>
</p>