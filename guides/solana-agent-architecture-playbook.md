# Solana Agent Architecture Playbook

Reference architecture and operating model for production-grade Solana agents.

## 1) Reference architecture

Control plane
- Planner/policy engine
- Risk and permission policy layer
- Prompt/skill/context layer
- Eval + regression harness

Execution plane
- Solana SDK/client layer (Solana Kit, web3.js, Anchor clients)
- Data and event streams (Helius webhooks, Yellowstone gRPC)
- Oracle layer (Pyth, Switchboard)
- Protocol adapters (Jupiter, Drift, Orca, Raydium, Kamino)

Safety plane
- Wallet/key custody and policy enforcement (Safe/Squads/Turnkey style controls)
- Transaction simulation and pre-trade checks
- Rate limits, max loss, max position size, per-protocol exposure caps
- Circuit breaker and kill-switch automation

Observability plane
- Structured traces/logs, tx lifecycle telemetry
- PnL and risk dashboards
- Error taxonomy and incident runbooks

## 2) Core execution pipeline

1. Ingest data
- Stream account/tx/orderbook updates and oracle prices.

2. Build state
- Normalize into a local state model (positions, balances, market context).

3. Decide
- Generate candidate actions under policy constraints.

4. Validate
- Simulate transaction; verify slippage/fees/risk limits.

5. Execute
- Submit with retries/backoff and idempotency keys.

6. Reconcile
- Confirm chain finality, update state, emit metrics.

## 3) Security controls (minimum baseline)

Wallet and signing
- Separate hot execution keys from treasury keys.
- Use scoped/signing policies (allowlists, spend ceilings, time windows).
- Rotate keys and monitor signer usage.

Transaction safety
- Mandatory preflight simulation for state-changing txs.
- Max slippage and price impact checks.
- Protocol allowlist and instruction schema validation.

Risk management
- Per-market and global notional caps.
- Drawdown and volatility-based circuit breakers.
- Cooldown after consecutive failed executions.

Operational safety
- Kill switch command path tested weekly.
- Explicit incident severity levels and rollback playbook.

## 4) Reliability and performance checklist

- [ ] Deterministic config and version pinning
- [ ] Retry strategy with jitter and bounded attempts
- [ ] Exactly-once style reconciliation/idempotency logic
- [ ] Latency budget per stage (ingest/decide/execute/reconcile)
- [ ] Backpressure handling for data spikes
- [ ] Post-failure state repair routines

## 5) Evaluation and regression gates

Build benchmark suites for:
- normal market conditions
- volatile markets
- oracle lag/divergence
- RPC degradation
- protocol-specific failure modes

Release gates example
- success rate >= prior baseline - 1%
- zero policy violations on safety suite
- p95 execution latency within agreed budget
- no unresolved reconciliation errors

## 6) Solana-focused tool map

Infra and data
- Helius SDK
- Yellowstone gRPC
- Solana Kit / web3.js

Execution and routing
- Jupiter Swap API
- Drift Protocol + DriftPy
- Phoenix v1
- Orca / Raydium
- Kamino KLend SDK

Identity and auth
- Sign-In With Solana
- UCAN-style delegation patterns
- Multisig/smart-account controls (Squads)

## 7) Day-2 operations runbook

Daily
- Check failed txs and reconciliation drift.
- Review risk limit breaches and near-miss events.
- Verify oracle health and stale feed alerts.

Weekly
- Re-run regression benchmark suite.
- Review policy exceptions and update allowlists.
- Test kill-switch and recovery drills.

Monthly
- Rotate credentials/signing keys.
- Audit dependency and protocol upgrade compatibility.
- Rebaseline latency/cost/performance targets.

## 8) Common failure modes

- Stale oracle data -> bad fills
- RPC instability -> duplicate or dropped actions
- Slippage spikes -> unbounded execution loss
- State desync -> incorrect position sizing
- Policy drift -> unintended protocol access

Mitigation: explicit pre-trade validation, bounded retries, strict reconciliation, and tested emergency stop paths.
