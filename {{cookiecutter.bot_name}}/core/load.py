from core import misc


def load_modules():
    try:
        # We're using this if you don't wont to open source some stuff
        misc.loader.load_package('private_modules')
    except (ImportError, ModuleNotFoundError):
        pass
    misc.loader.load_packages(f"modules.{item}" for item in [
        'base',  # User management and base Middlewares
        'tail',  # Handle all unhandled actions
    ])
