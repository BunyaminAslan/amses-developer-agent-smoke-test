"""Simple Selam greeting utility.

Provides a small function `selam` that returns a Turkish greeting for a name.
"""
from typing import Any


def selam(name: Any) -> str:
    """Return a Selam greeting for the given name.

    - If `name` is not a string, it will be converted using `str()`.
    - Leading/trailing whitespace is stripped. If the resulting name is empty,
      the function returns just "Selam".

    Examples:
        selam('Ahmet') -> 'Selam, Ahmet!'
        selam('  ') -> 'Selam'
        selam(123) -> 'Selam, 123!'
    """
    if name is None:
        return "Selam"
    s = str(name).strip()
    if not s:
        return "Selam"
    return f"Selam, {s}!"
