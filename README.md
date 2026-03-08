# Awesome Agent Cortex [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> The sovereign agent stack — practical scripts, on-chain identity, and
> knowledge graphs for AI agents that think, remember, and own themselves.

A curated list covering the full AI agent ecosystem: frameworks, coding agents,
MCP tooling, knowledge graphs, blockchain identity, decentralized finance
agents, quantitative trading, and observability. What makes this list unique is
the combination of practical developer tooling with on-chain identity and memory
infrastructure — resources no other awesome list brings together.

## Contents

- [Agent Frameworks](#agent-frameworks)
- [Coding Agents](#coding-agents)
- [CLI and TUI Tools](#cli-and-tui-tools)
- [MCP Ecosystem](#mcp-ecosystem)
- [Prompt Engineering](#prompt-engineering)
- [Agent Configs and Dotfiles](#agent-configs-and-dotfiles)
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

- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework from Microsoft Research.
- [Claude Agent SDK](https://github.com/anthropics/anthropic-sdk-python) - Official Python SDK for building agents with Claude models.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based multi-agent orchestration framework.
- [ElizaOS](https://github.com/elizaOS/eliza) - Multi-agent simulation framework for autonomous characters.
- [Google ADK](https://github.com/google/adk-python) - Agent Development Kit for building agents with Gemini.
- [Google A2A](https://github.com/google/A2A) - Agent-to-Agent protocol for cross-framework agent communication.
- [Haystack](https://github.com/deepset-ai/haystack) - LLM orchestration framework for building search and RAG pipelines.
- [Julep](https://github.com/julep-ai/julep) - Stateful agent platform with built-in persistence and task workflows.
- [LangChain](https://github.com/langchain-ai/langchain) - Composable framework for building LLM-powered applications.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Library for building stateful multi-agent workflows as graphs.
- [Letta](https://github.com/letta-ai/letta) - Stateful agents with long-term memory (formerly MemGPT).
- [Magentic-One](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one) - Multi-agent team for complex web and file tasks.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Official SDK for building agents with OpenAI models.
- [OpenClaw](https://github.com/openclaw/openclaw) - Self-hosted personal AI agent with multi-platform messaging and skill registry.
- [Phidata](https://github.com/phidatahq/phidata) - Toolkit for building AI assistants with memory and tools.
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
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) - Comprehensive Claude Code harness with agent skills, hooks, and multi-language support.
- [claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Community-sourced tips and tricks.
- [CLAUDE.md Guide](https://docs.anthropic.com/en/docs/claude-code/memory) - Official documentation on memory files.
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) - Event-driven shell command automation.
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/memory#slash-commands-as-custom-skills) - Reusable prompt-driven workflows.

## CLI and TUI Tools

Terminal-based agent interfaces and developer tools.

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Agentic CLI that operates directly in the terminal.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's command-line interface for Gemini models.
- [Glow](https://github.com/charmbracelet/glow) - Terminal Markdown renderer useful for agent output.
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
- [mcp](https://github.com/modelcontextprotocol/servers) - Official reference MCP server implementations.
- [MCP CLI](https://github.com/modelcontextprotocol/cli) - Command-line inspector and debugging tool for MCP.
- [MCP Go SDK](https://github.com/mark3labs/mcp-go) - Go implementation of the Model Context Protocol.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK for building MCP servers.
- [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Official Rust SDK for building MCP servers.
- [MCP Spec](https://spec.modelcontextprotocol.io) - Official Model Context Protocol specification.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Official TypeScript SDK for building MCP servers.
- [Playwright MCP](https://github.com/anthropics/mcp-playwright) - MCP server for browser automation via Playwright.
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

## Agent Configs and Dotfiles

Configuration files and workflow examples for AI coding tools.

- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) - Curated list of Cursor rule files.
- [Claude Code Memory Files](https://docs.anthropic.com/en/docs/claude-code/memory) - Guide to CLAUDE.md and project memory.
- [CursorDirectory](https://cursor.directory) - Community-shared Cursor rules and configurations.
- [dotfiles](https://dotfiles.github.io) - Guide to managing dotfiles including agent configurations.

## Knowledge Graphs and Memory

Agent memory architectures, knowledge graphs, and second-brain integrations.

- [Cognee](https://github.com/topoteretes/cognee) - Memory management layer for LLM apps using knowledge graphs.
- [FalkorDB](https://github.com/FalkorDB/FalkorDB) - Ultra-fast graph database for AI agent knowledge.
- [GraphRAG](https://github.com/microsoft/graphrag) - Graph-based retrieval augmented generation from Microsoft.
- [Khoj](https://github.com/khoj-ai/khoj) - Personal AI assistant with long-term memory and knowledge search.
- [LightRAG](https://github.com/HKUDS/LightRAG) - Simple and fast RAG framework using graph structures.
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI assistants and agents.
- [Memgraph](https://github.com/memgraph/memgraph) - In-memory graph database for real-time agent queries.
- [Neo4j](https://github.com/neo4j/neo4j) - Graph database platform widely used for agent knowledge stores.
- [Obsidian](https://obsidian.md) - Knowledge base and note-taking app usable as agent memory backend.
- [obsidian-graph-query](https://github.com/catacgc/obsidian-graph-query) - Query and traverse Obsidian vault graphs programmatically.
- [ODIN](https://github.com/memgraph/odin) - Knowledge graph construction tool built on Memgraph.
- [Pinecone](https://www.pinecone.io) - Vector database for semantic memory and retrieval.
- [Qdrant](https://github.com/qdrant/qdrant) - High-performance vector search engine for agent memory.
- [txtai](https://github.com/neuml/txtai) - All-in-one embeddings database for semantic search and workflows.
- [Weaviate](https://github.com/weaviate/weaviate) - Vector database with built-in modules for AI workloads.

## Solana Agent Infrastructure

Tools and SDKs for building AI agents on Solana.

- [ARC (AI Rig Complex)](https://github.com/ARC-Agency/arc) - Framework for deploying AI agents on Solana.
- [Awesome Solana AI](https://github.com/solana-foundation/awesome-solana-ai) - Solana Foundation's curated list of AI-Solana projects.
- [GOAT SDK](https://github.com/goat-sdk/goat) - Open-source toolkit connecting AI agents to 200+ on-chain tools across Solana and EVM chains.
- [Helius SDK](https://github.com/helius-labs/helius-sdk) - TypeScript SDK for Solana RPC, webhooks, and DAS API.
- [Jupiter SDK](https://github.com/jup-ag/jupiter-core) - Solana DEX aggregator SDK for agent-driven swaps.
- [LangChain Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit) - LangChain tools for Solana agent operations.
- [Light Protocol](https://github.com/Lightprotocol/light-protocol) - ZK compression for scalable on-chain agent state.
- [Metaplex](https://github.com/metaplex-foundation/metaplex-program-library) - Solana programs for NFTs and digital assets used in agent identity.
- [Solana Actions](https://github.com/solana-developers/solana-actions) - Spec and tools for blockchain-powered actions and blinks.
- [Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit) - Toolkit for connecting AI agents to Solana protocols.
- [Solana Web3.js](https://github.com/solana-labs/solana-web3.js) - JavaScript SDK for interacting with the Solana blockchain.

## Agent Identity and Wallets

On-chain identity, wallets, and trust infrastructure for autonomous AI agents.

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

- [Braintrust](https://www.braintrust.dev) - Evaluation and observability platform for AI products.
- [DeepEval](https://github.com/confident-ai/deepeval) - Open-source LLM evaluation framework.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability and monitoring platform.
- [LangFuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform for tracing and evaluation.
- [LangSmith](https://smith.langchain.com) - Platform for debugging, testing, and monitoring LLM applications.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry-based observability for LLM applications.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability platform from Arize.
- [Portkey](https://github.com/Portkey-AI/gateway) - AI gateway with observability, caching, and fallback routing.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - LLM evaluation and red-teaming toolkit.
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
