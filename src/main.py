import uvicorn
from .api.server import app
from .core.rule_engine import RuleEngine
from .core.code_analyzer import CodeAnalyzer

def main():
    """Main entry point for the Smart Code Reviewer"""
    print("🚀 Smart Code Reviewer Starting...")
    
    # Initialize components
    rule_engine = RuleEngine()
    analyzer = CodeAnalyzer(rule_engine)
    
    # Start API server
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()