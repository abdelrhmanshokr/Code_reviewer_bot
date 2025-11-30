CUSTOM_RULES = {
    "practical_maintainability": {
        "category": "Custom - Practical Experience",
        "rules": {
            "max_nesting": {
                "description": "Avoid nested conditionals deeper than 3 levels",
                "category": "maintainability",
                "priority": "medium", 
                "validation": "max_nesting_depth <= 3"
            },
            "explicit_error_handling": {
                "description": "Error handling should be explicit, not silent",
                "category": "structure",
                "priority": "high",
                "validation": "explicit_error_handling_check"
            }
        }
    }
}