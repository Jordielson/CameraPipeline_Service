import importlib
import traceback
from types import ModuleType
from camerapipeline.modules import get_named_modules

def init_routes(app):
    for named_module in get_named_modules():
        try:
            module: ModuleType = importlib.import_module(
                f'.modules.{named_module}.controller', package='camerapipeline')
            app.register_blueprint(getattr(module, 'blueprint'))
        except ModuleNotFoundError as exception:
            pass
        except Exception as exception:
            print(traceback.format_exc())
            pass