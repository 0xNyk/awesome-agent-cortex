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
- [Hermes Stack](#hermes-stack)
- [CLI and TUI Tools](#cli-and-tui-tools)
- [MCP Ecosystem](#mcp-ecosystem)
- [Prompt Engineering](#prompt-engineering)
- [Agent Harnessing and Evaluation](#agent-harnessing-and-evaluation)
- [Context Engineering](#context-engineering)
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

## Hermes Stack

Hermes Agent runtime, deployment rails, and operator resources.

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Open-source autonomous AI agent with CLI, gateway, memory, subagents, and broad tool integrations.
- [hermes-fly](https://github.com/alexfazio/hermes-fly) - Fly.io deployment and operations CLI for Hermes Agent with deploy, logs, doctor, and teardown workflows.
- [Hermes Agent + hermes-fly Best Practices (this repo)](guides/hermes-agent-hermes-fly-playbook.md) - Practical setup, operations, security, and optimization playbook.
- [Hermes Stack Quickstart Recipes (this repo)](guides/hermes-stack-quickstart-recipes.md) - Copy/paste recipes for local dev, hosted production, secure mode, and CI operations.
- [Hermes Stack Maturity Ladder (this repo)](guides/hermes-stack-maturity-ladder.md) - L1-L3 readiness model with upgrade paths and operational checklist.

## CLI and TUI Tools

Terminal-based agent interfaces and developer tools.

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Agentic CLI that operates directly in the terminal.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's command-line interface for Gemini models.
- [Glow](https://github.com/charmbracelet/glow) - Terminal Markdown renderer useful for agent output.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - CLI and gateway agent runtime with tools, memory, delegation, and automation support.
- [hermes-fly](https://github.com/alexfazio/hermes-fly) - CLI wizard to deploy and operate Hermes Agent on Fly.io.
- [lazygit](https://github.com/jesseduffield/lazygit) - Terminal UI for git commonly paired with coding agents.
- [llm](https://github.com/simonw/llm) - CLI tool for interacting with LLMs from the terminal.
- [mods](https://github.com/charmbracelet/mods) - AI on the command line built on Charm.
- [OpenCodex](https://github.com/openai/codex) - Lightweight CLI coding agent from OpenAI.
- [sgpt](https://github.com/tbckr/sgpt) - Command-line productivity tool powered by LLMs.
- [tmux](https://github.com/tmux/tmux) - Terminal multiplexer for running agents in persistent sessions.
- [Warp](https://www.warp.dev) - Modern terminal with built-in AI assistance.
- [Zellij](https://github.com/zellij-org/zellij) - Terminal workspace with plugin system for agent integration.

## MCP Ecosystem

Model Context Protocol servers, clients, and tooling.

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Curated list of MCP server implementations.
- [FastMCP](https://github.com/PrefectHQ/fastmcp) - Pythonic framework for building MCP servers and clients quickly.
- [mcp](https://github.com/modelcontextprotocol/servers) - Official reference MCP server implementations.
- [MCP Agent](https://github.com/lastmile-ai/mcp-agent) - Framework patterns for building agents on top of MCP.
- [MCP Go SDK](https://github.com/mark3labs/mcp-go) - Go implementation of the Model Context Protocol.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Official inspector and debugging tool for MCP servers.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK for building MCP servers.
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - Community registry service for discovering MCP servers.
- [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Official Rust SDK for building MCP servers.
- [MCP Spec](https://spec.modelcontextprotocol.io) - Official Model Context Protocol specification.
- [MCP Specification Repo](https://github.com/modelcontextprotocol/modelcontextprotocol) - Canonical specification and documentation repository.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Official TypeScript SDK for building MCP servers.
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - MCP server for browser automation via Playwright.
- [Smithery](https://smithery.ai) - Registry and hosting platform for MCP servers.

## Prompt Engineering

System prompts, templates, and agent prompt patterns.

- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library) - Official prompt examples from Anthropic.
- [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) - Collection of prompt examples for ChatGPT.
- [Claude System Prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) - Guide to writing effective system prompts.
- [DSPy](https://github.com/stanfordnlp/dspy) - Framework for programming with foundation models instead of prompting.
- [fabric](https://github.com/danielmiessler/fabric) - Framework for augmenting humans using AI with curated prompts.
- [LangChain Hub](https://smith.langchain.com/hub) - Community-driven prompt and chain sharing platform.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - Testing and evaluation framework for LLM prompts.
- [System Prompts](https://github.com/mustvlad/ChatGPT-System-Prompts) - Collection of system prompts for various AI models.

## Agent Harnessing and Evaluation

Harnesses, benchmarks, and evaluation frameworks for measuring agent quality and reliability.

- [AgentBench](https://github.com/THUDM/AgentBench) - Multi-domain benchmark suite for evaluating LLMs as agents.
- [AgentEvals](https://github.com/langchain-ai/agentevals) - Evaluation utilities for scoring agent trajectories and outcomes.
- [AutoGen agbench](https://github.com/microsoft/autogen/tree/main/python/packages/agbench) - Benchmark runner for AutoGen agent workflows.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) - Gym-style environment for training and evaluating browser agents.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - Open-source framework for reproducible LLM and agent evaluations.
- [MLE-bench](https://github.com/openai/mle-bench) - Benchmark harness for autonomous ML engineering tasks.
- [OSWorld](https://github.com/xlang-ai/OSWorld) - Open-ended benchmark environment for desktop computer-use agents.
- [OpenCUA](https://github.com/xlang-ai/OpenCUA) - Open foundation stack for building and evaluating computer-use agents.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Canonical benchmark for coding agents on real GitHub issue tasks.
- [Tau-Bench](https://github.com/sierra-research/tau-bench) - Realistic interactive benchmark for measuring agent reliability.
- [WebArena](https://github.com/web-arena-x/webarena) - Real-world web task benchmark environment for browser agents.
- [WorkArena](https://github.com/ServiceNow/WorkArena) - Enterprise task benchmark for browser-based agent workflows.
- [Agent Harnessing Playbook (this repo)](guides/agent-harnessing-playbook.md) - Practical framework for benchmark design, regression gates, and release readiness.

## Context Engineering

Methods and references for designing robust, efficient context pipelines.

- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - Practical engineering patterns for agent design and execution loops.
- [Anthropic: Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) - Retrieval architecture guidance for improving grounding and precision.
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - Official prompt and instruction design guidance.
- [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals) - Official framework for building eval loops and quality gates.
- [OpenAI Cookbook: Getting Started with Evals](https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals) - Practical eval setup walkthrough.
- [RAG (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) - Foundational retrieval-augmented generation paper.
- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2203.02155) - Foundational reasoning/prompting technique paper.
- [Lost in the Middle (Liu et al., 2023)](https://arxiv.org/abs/2307.03172) - Key long-context failure analysis paper.
- [Context Engineering Playbook (this repo)](guides/context-engineering-playbook.md) - Practical context budget, memory, retrieval, and anti-drift checklist.

## Agent Configs and Dotfiles

Configuration files and workflow examples for AI coding tools.

- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) - Curated list of Cursor rule files.
- [Claude Code Memory Files](https://docs.anthropic.com/en/docs/claude-code/memory) - Guide to CLAUDE.md and project memory.
- [Claude Code Starter Configs](claude/) - Ready-to-use CLAUDE.md, rules, hooks, and skills for Claude Code projects.
- [CursorDirectory](https://cursor.directory) - Community-shared Cursor rules and configurations.
- [dotfiles](https://dotfiles.github.io) - Guide to managing dotfiles including agent configurations.

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

- [Awesome Solana AI](https://github.com/solana-foundation/awesome-solana-ai) - Solana Foundation's curated list of AI-Solana projects.
- [GOAT SDK](https://github.com/goat-sdk/goat) - Open-source toolkit connecting AI agents to 200+ on-chain tools across Solana and EVM chains.
- [Helius SDK](https://github.com/helius-labs/helius-sdk) - TypeScript SDK for Solana RPC, webhooks, and DAS API.
- [Jupiter Swap API Docs](https://dev.jup.ag/docs/swap-api) - Official documentation for integrating Jupiter routing and swaps.
- [LangChain Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit) - LangChain tools for Solana agent operations.
- [Light Protocol](https://github.com/Lightprotocol/light-protocol) - ZK compression for scalable on-chain agent state.
- [Metaplex](https://github.com/metaplex-foundation/metaplex-program-library) - Solana programs for NFTs and digital assets used in agent identity.
- [Solana Actions](https://github.com/solana-developers/solana-actions) - Spec and tools for blockchain-powered actions and blinks.
- [Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit) - Toolkit for connecting AI agents to Solana protocols.
- [Solana Web3.js](https://github.com/solana-labs/solana-web3.js) - JavaScript SDK for interacting with the Solana blockchain.

## Agent Identity and Wallets

On-chain identity, wallets, and trust infrastructure for autonomous AI agents.

- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - Toolkit for giving AI agents programmable wallet capabilities.
- [Crossmint](https://www.crossmint.com) - Wallet-as-a-service for agent-owned wallets and NFT minting.
- [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) - Proposed standard for cross-chain agent identity.
- [Lit Protocol](https://github.com/LIT-Protocol/js-sdk) - Decentralized key management and programmable signing.
- [Privy](https://www.privy.io) - Embedded wallet infrastructure for agent authentication.
- [Safe](https://github.com/safe-global/safe-smart-account) - Multi-signature smart account for EVM agent treasuries.
- [Solana Agent Identity](https://github.com/sendaifun/solana-agent-kit) - Agent wallet and identity features in Solana Agent Kit.
- [Squads Protocol](https://github.com/Squads-Protocol/v4) - Multisig and smart account protocol for Solana agents.
- [Turnkey](https://www.turnkey.com) - Secure key infrastructure for programmatic wallet management.
- [UCAN](https://github.com/ucan-wg/spec) - User-controlled authorization for decentralized agent capabilities.

## Agent Payments

Payment protocols and infrastructure for autonomous agent transactions.

- [Awesome x402](https://github.com/Merit-Systems/awesome-x402) - Curated resources for the x402 payment protocol ecosystem.
- [Coinbase Agentic Wallets](https://www.coinbase.com/developer-platform/discover/launches/agentic-wallets) - Wallet infrastructure for AI agents with programmable spending limits.
- [Google A2A x402 Extension](https://github.com/google-agentic-commerce/a2a-x402) - Cryptocurrency payments for the Agent-to-Agent protocol via x402.
- [lobster.cash](https://www.lobster.cash) - Agent payment solution on Solana with Visa Intelligent Commerce integration by Crossmint.
- [x402 Foundation](https://www.x402.org) - Open protocol foundation governing the x402 payment standard.
- [x402 Protocol](https://github.com/coinbase/x402) - Open HTTP payment protocol using the 402 status code for agent-to-service payments.

## DeFi Agents

AI agents for decentralized finance operations and strategy.

- [Autonolas](https://github.com/valory-xyz/open-autonomy) - Framework for building autonomous agent services on-chain.
- [DeFi Llama API](https://defillama.com/docs/api) - Open API for DeFi protocol data used by trading agents.
- [ElizaOS DeFi Plugins](https://github.com/elizaOS/eliza/tree/main/packages) - DeFi protocol integrations for ElizaOS agents.
- [Gauntlet](https://www.gauntlet.xyz) - Risk management and simulation platform for DeFi agents.
- [Griffain](https://griffain.com) - AI agent platform for Solana DeFi operations.
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
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Open-source financial LLM framework.
- [FinRL](https://github.com/AI4Finance-Foundation/FinRL) - Deep reinforcement learning library for quantitative finance.
- [Freqtrade](https://github.com/freqtrade/freqtrade) - Open-source algorithmic trading bot in Python.
- [Hummingbot](https://github.com/hummingbot/hummingbot) - Open-source market making and arbitrage bot.
- [Lean](https://github.com/QuantConnect/Lean) - Algorithmic trading engine by QuantConnect.
- [NautilusTrader](https://github.com/nautechsystems/nautilus_trader) - High-performance algorithmic trading platform in Rust and Python.
- [Qlib](https://github.com/microsoft/qlib) - AI-oriented quantitative investment platform from Microsoft.
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) - Multi-agent LLM framework simulating a trading firm.
- [VectorBT](https://github.com/polakowo/vectorbt) - Fast backtesting and analysis library for trading strategies.
- [Zipline](https://github.com/stefan-jansen/zipline-reloaded) - Pythonic algorithmic trading library for backtesting.

## Agent Observability and Testing

Debugging, tracing, evaluation, and testing tools for AI agents.

- [AgentOps](https://github.com/AgentOps-AI/agentops) - Monitoring, cost tracking, and benchmarking for agent workflows.
- [Braintrust](https://www.braintrust.dev) - Evaluation and observability platform for AI products.
- [DeepEval](https://github.com/confident-ai/deepeval) - Open-source LLM evaluation framework.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Validation and safety guardrails framework for LLM outputs.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability and monitoring platform.
- [LangFuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform for tracing and evaluation.
- [LangSmith](https://smith.langchain.com) - Platform for debugging, testing, and monitoring LLM applications.
- [LiteLLM](https://github.com/BerriAI/litellm) - LLM gateway and proxy with logging, cost tracking, and routing controls.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Toolkit for adding programmable safety and policy guardrails to LLM systems.
- [OpenAI Evals](https://github.com/openai/evals) - Framework and benchmark registry for evaluating LLM systems.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry-based observability for LLM applications.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability platform from Arize.
- [Portkey](https://github.com/Portkey-AI/gateway) - AI gateway with observability, caching, and fallback routing.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - LLM evaluation and red-teaming toolkit.
- [SigNoz](https://github.com/SigNoz/signoz) - OpenTelemetry-native observability platform for traces, logs, and metrics.
- [Weave](https://github.com/wandb/weave) - Toolkit for tracking and evaluating LLM applications from W&B.

## Research Papers

Curated papers on AI agents, multi-agent systems, and agent infrastructure.

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Comprehensive survey of LLM-based agent architectures.
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

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and
related or neighboring rights to this work.
