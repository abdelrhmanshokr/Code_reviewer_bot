from typing import Dict, Any, Optional


class CodeAnalyzer:
    """Small helper to compute simple metrics used by the review stub.

    Accepts an optional RuleEngine (or similar) so callers can pass context.
    """

    def __init__(self, rule_engine: Optional[Any] = None):
        self.rule_engine = rule_engine

    def count_lines(self, code: str) -> int:
        return len([l for l in code.splitlines() if l.strip() != ""])

    def max_indentation_depth(self, code: str) -> int:
        """Estimate nesting by counting indentation levels (works for Python-like code).

        It's a heuristic, good enough for giving simple guidance in the stub.
        """
        max_depth = 0
        for line in code.splitlines():
            if not line.strip():
                continue
            # count leading spaces
            leading = len(line) - len(line.lstrip(" "))
            # assume 4 spaces per indent level
            depth = leading // 4
            if depth > max_depth:
                max_depth = depth
        return max_depth

    def contains_toplevel_docstring(self, code: str) -> bool:
        s = code.strip()
        return s.startswith('"""') or s.startswith("'''")

    def analyze(self, code: str) -> Dict[str, int]:
        return {
            "lines": self.count_lines(code),
            "max_nesting": self.max_indentation_depth(code),
            "has_docstring": int(self.contains_toplevel_docstring(code)),
        }
