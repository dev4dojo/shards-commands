# Commands

The library for building command line interface

## Example

How to use Command class

```python
import pathlib
import sys

from commands.base import Command
from logger import get_logger

logger = get_logger(__name__)


class IndexCommand(Command):
    name = "index"
    description = "Index Command"

    def add_arguments(self, parser):
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update the index with the latest data.",
        )

    def execute(self, args):
        """
        Execute the command to index latest data.
        Args:
            args: Parsed command-line arguments.
        """
        try:
            pass
        except KeyboardInterrupt:
            print("\nUpdate interrupted by user.")
        finally:
            pass
```
