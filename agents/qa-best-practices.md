# QA Best Practices — ProdutoVivo

Company-wide quality and deployment controls. All agents must follow these policies.

## Deployment Rules

1. **No deploy without testing.** Every change must be verified on :8082 first.
2. **CTO sign-off required.** Mantiqueira reviews all code before production.
3. **CMO sign-off required.** Araguaia reviews all customer-facing content before publish.
4. **No direct server edits.** All changes go through the GitHub repo.

## Health Monitoring

- **Daily Health Check:** Fires at 07:45 UTC — verifies :8082 up, pages load, Stripe webhooks respond, email works.
- **Weekly Tech Review:** Mantiqueira reviews open tech debt and infra issues every Wednesday at 14:00 UTC.
- **Weekly QA Audit:** Reviews QA controls and policy compliance every Monday at 10:00 UTC (Vigia, when hired).

## Testing Requirements

- Test all backend changes against :8082 before deploy
- Verify Stripe webhook handling after payment-related changes
- Confirm email delivery after Resend changes
- Check Meta Pixel (4520253334926563) presence after frontend changes

## Incident Response

- Document all deploys as issue comments
- Escalate critical issues to Iguaçu (CEO) immediately
- Roll back immediately if :8082 shows errors post-deploy
