import pkgutil
import importlib


def collect_commands():
    commands = []

    for importer, modname, ispkg in pkgutil.iter_modules(__path__):
        if not ispkg:
            continue

        try:
            commands_module = importlib.import_module(__name__ + '.' + modname + '.commands')

            for importer, modname, ispkg in pkgutil.iter_modules(commands_module.__path__):
                if ispkg:
                    continue

                commands.append(importlib.import_module(commands_module.__name__ + '.' + modname))

        except ModuleNotFoundError:
            pass

    return commands
