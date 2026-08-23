# ADR-002: Account and Hozan Identity

## Status

Accepted

## Context

Hozan needs a stable account identity that can later own multiple Hozan IDs,
assets, roles and bot instances.

## Decision

An account is identified internally by the Telegram user ID.

A Hozan ID is a separate domain resource owned by an account. Each account
may reserve one free Hozan ID. Additional identities can be added later.

Hozan IDs are globally unique and begin with `#`. Persistence must enforce
that uniqueness atomically.

The free identity is immutable through the normal account settings flow.

Telegram transport and Titan remain outside the identity domain.
