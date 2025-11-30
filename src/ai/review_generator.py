from typing import List, Dict
from ..core.code_analyzer import CodeAnalyzer


def _make_improvement(title: str, explanation: str, suggestion: str, priority: str) -> Dict:
    return {
        "title": title,
        "explanation": explanation,
        "suggested_change": suggestion,
        "priority": priority,
    }


def generate_review(code: str, language: str = "python") -> Dict:
    """Create a deterministic, heuristic-based review: 3 improvements + 1 positive note.

    This stub is intentionally small so the app works without external APIs.
    """
    analyzer = CodeAnalyzer()
    metrics = analyzer.analyze(code)

    improvements: List[Dict] = []

    # Improvement 1: long functions / many lines
    if metrics["lines"] > 40:
        improvements.append(_make_improvement(
            "Reduce function/module size",
            f"The snippet has {metrics['lines']} non-empty lines which can make it hard to read and test.",
            "Split large functions into smaller, single-responsibility functions.",
            "high"
        ))
    else:
        improvements.append(_make_improvement(
            "Keep functions small",
            "Functions shorter than ~20 lines are easier to test and understand.",
            "Consider extracting helper functions if a function grows.",
            "medium"
        ))

    # Improvement 2: nesting
    if metrics["max_nesting"] > 3:
        improvements.append(_make_improvement(
            "Reduce nesting depth",
            f"Estimated max nesting depth is {metrics['max_nesting']} which reduces readability.",
            "Refactor nested conditionals into early returns or helper functions.",
            "high"
        ))
    else:
        improvements.append(_make_improvement(
            "Avoid deep nesting",
            "Current nesting looks reasonable but watch for future growth.",
            None,
            "low"
        ))

    # Improvement 3: docstring / naming heuristic
    if not metrics["has_docstring"]:
        improvements.append(_make_improvement(
            "Add a top-level docstring or function docstrings",
            "Docstrings clarify intent for other developers and for tools.",
            "Add a short module or function docstring describing behavior and inputs/outputs.",
            "medium"
        ))
    else:
        improvements.append(_make_improvement(
            "Keep docstrings concise",
            "Good docstring present; ensure it stays up to date with code changes.",
            None,
            "low"
        ))

    positive = "Clear structure — the logic is straightforward and easy to follow."

    return {
        "improvements": improvements[:3],
        "positive_note": positive
    }
