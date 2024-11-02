from icecream import ic
from pathlib import Path
import os
import sys

def debug_environment():
    # Print Python path
    ic(sys.path)
    
    # Print environment variables
    ic(dict(os.environ))
    
    # Print current working directory
    ic(os.getcwd())
    
    # Print directory contents
    ic(list(Path('.').rglob('*')))
    
    # Print Poetry environment
    ic(os.system('poetry env info'))
    
    # Try importing key packages
    try:
        import fastapi
        ic("FastAPI imported successfully", fastapi.__version__)
    except ImportError as e:
        ic("FastAPI import failed", str(e))
        
    try:
        import sqlalchemy
        ic("SQLAlchemy imported successfully", sqlalchemy.__version__)
    except ImportError as e:
        ic("SQLAlchemy import failed", str(e))

if __name__ == "__main__":
    debug_environment()