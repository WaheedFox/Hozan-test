# ADR-001 — Hozan is built on Titan

## Status

Accepted

## Context

Hozan is a no-code platform for creating configurable Telegram bots.

The platform will contain many capabilities and may eventually support a
large number of independent bot roles and features.

Reimplementing Telegram transport, update dispatch, context handling, and
polling inside Hozan would duplicate functionality already provided by Titan.

## Decision

Hozan uses Titan as its Telegram application runtime.

Hozan builds domain behavior above Titan rather than replacing Titan's core
execution model.

The boundary is:

```text
Titan
  └── Telegram execution

Hozan
  └── Bot-building domain
```

Hozan may use Titan's public APIs directly.

Hozan may add domain-specific abstractions when those abstractions represent
Hozan concepts rather than duplicated Telegram framework behavior.

Consequences

Positive

- Hozan inherits Titan's stable Telegram execution model.
- Telegram transport logic is not duplicated.
- Hozan can focus on accounts, instances, roles, features, and policies.
- Titan improvements can benefit Hozan without rewriting the application
  runtime.

Negative

- Hozan depends on Titan's supported public contract.
- Requirements that cannot be expressed cleanly through Titan must be
  evaluated before implementation.
- Hozan must avoid depending on Titan implementation details.

Rejected Alternatives

Reimplement Telegram runtime inside Hozan

Rejected because it duplicates Titan and creates two execution models.

Fork Titan into Hozan

Rejected because Hozan would inherit a permanently divergent framework.

Make Hozan a collection of Titan plugins

Rejected because Hozan is an application platform, not merely an extension
package for Titan.

Rule

If a Hozan feature appears to require a Titan core modification, first ask:

«Would this Titan change be justified for Titan independently of Hozan?»

If yes, the Titan change may be evaluated separately.

If no, Hozan must solve the requirement above the Titan boundary.