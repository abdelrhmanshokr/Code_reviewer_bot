AUTHORITY_RULES = {
    "clean_code": {
        "source": "Robert C. Martin - Clean Code",
        "rules": {
            "function_size": {
                "description": "Functions should be small (under 20 lines)",
                "category": "readability",
                "priority": "high",
                "validation": "function_line_count <= 20"
            },
            "meaningful_names": {
                "description": "Variable and function names should reveal intent",
                "category": "readability", 
                "priority": "critical",
                "validation": "name_meaningfulness_check"
            }
        }
    },
    "google_python": {
        "source": "Google Python Style Guide",
        "rules": {
            "naming_conventions": {
                "description": "Follow PEP 8 naming conventions",
                "category": "structure",
                "priority": "high",
                "validation": "pep8_naming_check"
            }
        }
    }
}