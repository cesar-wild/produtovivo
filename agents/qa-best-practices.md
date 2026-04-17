# QA Best Practices — ProdutoVivo (Company Policy)

**Authority:** Board directive (PRO-47, 2026-04-16). Mandatory for all agents.
**Owner:** Iguaçu (CEO) enforces; QA agent (Vigia, when hired) operates.

This policy exists because the prior QA system failed: agents marked tasks done
without verifying, the same errors repeated (41 deploy-failure emails, broken
Action reported "disabled" while still running, model gibberish from a free
model). No more.

## 1. Self-verification (every agent, every task)

Before marking ANY task `done`, the agent MUST post evidence in the closing
comment. **No evidence = not done.**

Acceptable evidence (pick what fits the change):

- Code change: commit SHA + link, file paths touched, test output.
- Infra/CI: API response showing the new state (`gh api`, DNS dig, curl, secret
  presence). For GitHub Actions: check `actions/workflows` (state) AND
  `contents/.github/workflows` (file presence).
- Deploy: HTTP response from the deployed endpoint, run timestamp.
- Data/migration: row counts, sample query results, before/after.
- Content publish: live URL + screenshot OR fetched HTML excerpt.

**Closing comment template:**

```
## Done

<one-line summary>

### Evidence
- <link / API response / SHA>
- <link / API response / SHA>

### Follow-ups (if any)
- <issue link>
```

## 2. Anti-loop (stop and escalate)

- Same command failing **2 times** → STOP, escalate to your manager (or CEO).
- **3 times** → QA forces a pause on the agent.
- No silent retry loops. If you change approach mid-task, log the change in a
  comment.

## 3. Model validation (use of free/external models)

- Sanity-check output before acting on it. Mixed languages, random Unicode,
  off-topic content = gibberish → switch model.
- Known broken: `opencode/nemotron-3-super-free`. **Never use it.**

## 4. QA agent duties (Vigia)

Daily scan of all runs in the last 24h for: failed runs, gibberish output,
stuck agents, repeat failures. Check external signals: GitHub Actions, deploy
endpoints, email deliverability, backups.

Report severities:
- **CRITICAL** — outage, data loss risk, compliance break. Trigger CEO
  heartbeat immediately, do not wait for the daily report.
- **WARNING** — degradation, repeat failures under threshold, unverified
  closes. Include in daily QA report.
- **INFO** — observations, trends.

## 5. CEO duties (Iguaçu)

- Acknowledge every escalation within one heartbeat.
- Group related issues — 3 agents reporting the same root cause = 1
  investigation, not 3 tickets.
- Do NOT close `CRITICAL` issues without verified evidence.
- Post-mortem on every CRITICAL: root cause, detection gap, prevention added.
  File the post-mortem as an issue with label `incident`.

## 6. Mandatory routines

| Routine                | Cadence                  | Owner |
|------------------------|--------------------------|-------|
| Daily Health Check     | 07:45 UTC daily          | Vigia |
| Daily QA Report        | 08:00 UTC daily          | Vigia |
| Weekly Audit           | Mondays 10:00 UTC        | Vigia |
| Monthly Retro          | 1st of month             | Iguaçu |

Until Vigia is hired, Iguaçu owns the QA routines and triages outputs manually.

## 7. References in AGENTS.md

Every agent's `AGENTS.md` MUST link to this file under a `## QA Policy` section.
New agents adopt this policy on day one.
