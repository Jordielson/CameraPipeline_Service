import os
import sys
from typing import List
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_named_modules() -> List[str]:
    """ Get module name
    Create an environment variable in your .env file with the name MODULE_PATH 
    that specifies the module path in project.
    """
    modules: List[str] = os.listdir(f'{sys.path[0]}{os.environ["MODULE_PATH"]}')
    directories: List[str] = []

    for module in modules:
        if not module in ('__init__.py', '__pycache__'):
            directories.append(module)

    return directories


__all__ = get_named_modules()