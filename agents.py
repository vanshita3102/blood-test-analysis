# Safe 'agent' placeholder module.
# The original code depended on CrewAI and contained unsafe instructions.
# This module provides a simple wrapper name 'doctor' used by main.py for compatibility.

from typing import Callable

def doctor_analyze(text: str) -> str:
    """Placeholder doctor analysis - not used directly in current flow."""
    return "This is a safe mock doctor. Use tools.analyze_metrics instead."

# expose a callable named 'doctor'
doctor = doctor_analyze