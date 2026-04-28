# SourceOS / SociOS keymap-profile binding

This directory records the downstream keymap-profile binding for `kinto`.

## Purpose

`kinto` consumes the shared SourceOS / SociOS keyboard-navigation canon.
It does not own the canonical interaction model.

## Current binding

- `kinto.keymap-profile.json` — downstream `KeymapProfile` binding for the Mac/Linux primary modifier strategy.
- `sourceos_binding.py` — small Python helper exposing the same keymap-profile metadata to runtime or installer code.

## Placement rule

Canonical schema ownership remains in `SourceOS-Linux/sourceos-spec`.
`kinto` binds to that canon downstream.
