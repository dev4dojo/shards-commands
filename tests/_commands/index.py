import json

from shards.commands.base import Command


class IndexCommand(Command):
    """
    Test Index Command
    """

    name = "index"
    description = "Test command for indexing"

    def add_arguments(self, parser):
        """
        Add arguments for the index command.
        """
        parser.add_argument("--source", type=str, help="The source", required=True)
        parser.add_argument(
            "--target", type=str, help="The target", default="DEFAULT_TARGET"
        )

    def execute(self, args) -> dict:
        """
        Execute the index command with the provided arguments.
        """
        print(
            json.dumps(
                {
                    "source": args.source,
                    "target": args.target,
                    "message": "Index command executed successfully",
                }
            )
        )
