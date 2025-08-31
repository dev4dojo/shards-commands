from _commands.index import IndexCommand

from shards.commands.base import Command


def test_commands_base():
    assert Command is not None, "BaseCommand should be imported successfully"


def test_commands_import_commands():
    index_cmd = IndexCommand()
    assert index_cmd is not None, "IndexCommand should be instantiated successfully"
    assert index_cmd.name == "index", "IndexCommand name should be 'index'"
    assert index_cmd.description == "Test command for indexing", (
        "IndexCommand description should match"
    )
