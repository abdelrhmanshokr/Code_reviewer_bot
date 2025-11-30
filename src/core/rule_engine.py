from typing import Dict, List, Any
from .standards.authority_rules import AUTHORITY_RULES
from .standards.custom_rules import CUSTOM_RULES

class RuleEngine:
    def __init__(self):
        self.authority_rules = AUTHORITY_RULES
        self.custom_rules = CUSTOM_RULES
        self.rule_weights = self._initialize_weights()
    
    def _initialize_weights(self) -> Dict[str, float]:
        return {
            "critical": 1.0,
            "high": 0.7, 
            "medium": 0.4,
            "low": 0.2
        }
    
    def get_all_rules(self) -> Dict[str, Any]:
        return {
            "authority_rules": self.authority_rules,
            "custom_rules": self.custom_rules
        }