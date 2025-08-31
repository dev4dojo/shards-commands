import argparse
import importlib
import pkgutil
import typing as t
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract base class for defining command-line commands.

    Methods
    -------
    add_arguments(parser)
        Abstract method to add arguments to the command-line parser.

    execute(args)
        Abstract method to execute the command with the parsed arguments.
    """

    @abstractmethod
    def add_arguments(self, parser):  # pragma: no cover
        """Add arguments for the command."""
        pass

    @abstractmethod
    def execute(self, args):  # pragma: no cover
        """Execute the command with parsed arguments."""
        pass


def load_commands(commands_package: str = None) -> t.List[Command]:
    """
    Dynamically import all modules in the 'commands' package
    """
    # Validate that the commands package is provided and valid
    assert commands_package is not None, "The commands package must be provided"
    assert isinstance(commands_package, str), "The commands package must be a string"
    assert commands_package.strip() != "", (
        "The commands package must not be an empty string"
    )

    commands = []
    IGNORED_MODULES = ["__init__", "base"]

    # Dynamically import commands from all modules in the 'file_storage.commands' package
    package = importlib.import_module(commands_package)
    modules = [
        importlib.import_module(commands_package + "." + module.name)
        for module in pkgutil.iter_modules(package.__path__)
        if module.name not in IGNORED_MODULES
    ]
    for module in modules:
        # Find all classes in the module that inherit from Command
        for obj in vars(module).values():
            if (
                isinstance(obj, type)
                and issubclass(obj, Command)
                and obj is not Command
            ):
                commands.append(obj())
    return commands


def cli_handler(
    description: str = "Default CLI handler for commands", commands_package: str = None
) -> None:
    parser = argparse.ArgumentParser(description=description)
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    commands = {}
    for command in load_commands(commands_package=commands_package):
        commands[command.name] = command
        subparser = subparsers.add_parser(command.name, help=command.description)
        command.add_arguments(subparser)

    args = parser.parse_args()

    command = commands[args.command]
    command.execute(args)
