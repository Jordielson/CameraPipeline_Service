import importlib
import traceback
from types import ModuleType
from camerapipeline.modules import __all__

def init_routes(app):
    for named_module in __all__:
        try:
            module: ModuleType = importlib.import_module(
                f'.modules.{named_module}.controller', package='camerapipeline')
            app.register_blueprint(getattr(module, 'blueprint'))
        except ModuleNotFoundError as exception:
            print(exception.msg)
            pass
        except Exception as exception:
            print(traceback.format_exc())
            pass