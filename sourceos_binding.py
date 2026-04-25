"""SourceOS / SociOS keymap-profile binding helper for kinto.

This module intentionally stays small. It exposes the canonical keymap profile
metadata so kinto-side tooling or future runtime code can consume the shared
keyboard-navigation canon without making `kinto` the owner of that canon.
"""

from __future__ import annotations

from typing import Any

_KEYMAP_PROFILE: dict[str, Any] = {
    'id': 'urn:srcos:keymap-profile:mac-linux-primary',
    'name': 'Mac/Linux Primary Profile',
    'platform': 'socios-linux',
    'primaryModifierStrategy': 'mac-linux-primary',
    'guiProfile': {
        'physicalCtrl': 'Super',
        'physicalAlt': 'Alt',
        'physicalSuper': 'Ctrl',
    },
    'terminalProfile': {
        'physicalCtrl': 'Ctrl',
        'physicalAlt': 'Alt',
        'physicalSuper': 'RightCtrl',
    },
    'launcherRefs': [],
    'overlayRefs': ['urn:srcos:interaction-surface:shortcut-overlay'],
    'remapEngineRef': 'urn:srcos:remap-engine:kinto',
    'protectedNamespaces': ['terminal.pass-through', 'editor.insert', 'browser.text-field', 'accessibility'],
    'evidenceRefs': [],
}


def get_sourceos_keymap_profile() -> dict[str, Any]:
    """Return the SourceOS keymap profile binding for kinto.

    The returned object is a copy so callers can enrich it locally without
    mutating the module-level canonical binding payload.
    """
    return {
        **_KEYMAP_PROFILE,
        'guiProfile': dict(_KEYMAP_PROFILE['guiProfile']),
        'terminalProfile': dict(_KEYMAP_PROFILE['terminalProfile']),
        'launcherRefs': list(_KEYMAP_PROFILE['launcherRefs']),
        'overlayRefs': list(_KEYMAP_PROFILE['overlayRefs']),
        'protectedNamespaces': list(_KEYMAP_PROFILE['protectedNamespaces']),
        'evidenceRefs': list(_KEYMAP_PROFILE['evidenceRefs']),
    }
