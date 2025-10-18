# Shards | Commands

This project provides a lightweight and extensible framework for building modular command-line interfaces (CLI) in Python. It allows easily define commands as separate modules and automatically discover and execute them without manually editing the main script.

## Features

* Dynamic command discovery: Automatically loads all command modules from a given package.
* Clean architecture: Define each command as a class that inherits from a shared `Command` base class.
* Built-in argument parsing: Uses Python’s standard `argparse` module.
* Extensible: Add new commands just by creating new Python files, no need to change main CLI logic.

## How to install

```sh
pip install https://github.com/dev4dojo/shards-commands.git@<versios>
```

## Requirements

* Python 3.8+
* No external dependencies (uses only standard library)

## Project Structure Example

```
sample_project/
│
├── cli.py                     # Main CLI entry point (contains cli_handler)
├── commands/                  # Package with command definitions
│   ├── greet.py               # Example command
│   └── math_ops.py            # Another command
└── pyproject.toml / setup.py  # (optional) project configuration
```

## How It Works

1. Each command module in the `commands/` package defines a class inheriting from `Command`.
2. The framework automatically imports all command modules.
3. Each command registers its arguments and implements its execution logic.
4. The CLI handler (`cli_handler`) builds a parser, loads commands, and dispatches the selected one.

## Defining a Command

Here’s how to define a new command:

```python
# commands/greet.py
from shards.commands.base import Command

class GreetCommand(Command):
    name = "greet"
    description = "Print a friendly greeting."

    def add_arguments(self, parser):
        parser.add_argument("--name", required=True, help="Name to greet")

    def execute(self, args):
        print(f"Hello, {args.name}!")
```

## Running the CLI

You can invoke the CLI from your main script (e.g., `cli.py`):

```python
from shards.commands.base import cli_handler

if __name__ == "__main__":
    cli_handler(
        description="Sample Project CLI",
        commands_package="sample_project.commands"
    )
```

Then run it from the terminal:

```bash
python cli.py greet --name John
# Output: Hello, John!
```

## Adding More Commands

Simply create a new file in the `commands/` directory (e.g., `math_ops.py`) and define a class extending `Command`.
The framework will automatically detect and load it.

Example:

```python
# commands/math_ops.py
from shards.commands.base import Command

class AddCommand(Command):
    name = "add"
    description = "Add two numbers."

    def add_arguments(self, parser):
        parser.add_argument("a", type=int)
        parser.add_argument("b", type=int)

    def execute(self, args):
        print(args.a + args.b)
```

Run:

```bash
python cli.py add 3 5
# Output: 8
```

## API Overview

### `class Command(ABC)`

Abstract base class for defining commands.

* `add_arguments(parser)` → define command-line arguments.
* `execute(args)` → define logic executed when command runs.

### `load_commands(commands_package: str) -> list[Command]`

Dynamically imports all command modules from the specified package and instantiates them.

### `cli_handler(description: str, commands_package: str)`

Creates and runs the CLI parser, automatically wiring up all available commands.

## Example Test Run

```bash
python cli.py --help
python cli.py greet --help
python cli.py add 2 7
```

## License

MIT License — feel free to use and modify for your own projects.

