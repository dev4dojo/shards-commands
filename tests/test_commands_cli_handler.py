import json
import sys

from shards.commands.base import cli_handler


def test_commands_cli_handler_no_inputs():
    """
    Test the CLI handler with no inputs.
    """
    sys.argv = ["cli_handler"]
    try:
        cli_handler(commands_package="_commands")
    except SystemExit as e:
        assert str(e) == "2", "Should raise SystemExit 2 for no command"


def test_commands_cli_handler_help():
    """
    Test the CLI handler with help argument.
    """
    sys.argv = ["cli_handler", "--help"]
    try:
        cli_handler(commands_package="_commands")
    except SystemExit as e:
        assert str(e) == "0", "Should raise SystemExit 0 for help command"


def test_commands_cli_handler_unknown_command():
    """
    Test the CLI handler with an unknown command.
    """
    sys.argv = ["cli_handler", "unknown_command"]
    try:
        cli_handler(commands_package="_commands")
    except SystemExit as e:
        assert str(e) == "2", "Should raise SystemExit 2 for unknown command"


def test_commands_cli_handler_index_help():
    """
    Test the CLI handler with index help command.
    """

    sys.argv = ["cli_handler", "index"]
    try:
        cli_handler(commands_package="_commands")
    except SystemExit as e:
        assert str(e) == "2", "Should raise SystemExit 0 for help command"

    sys.argv = ["cli_handler", "index", "--help"]
    try:
        cli_handler(commands_package="_commands")
    except SystemExit as e:
        assert str(e) == "0", "Should raise SystemExit 0 for help command"


def test_commands_cli_handler_index_with_source_and_default_target(capsys):
    """
    Test the CLI handler with index command with source argument and default target.
    """
    sys.argv = ["cli_handler", "index", "--source", "SOURCE"]

    cli_handler(commands_package="_commands")
    captured_data = json.loads(capsys.readouterr().out.strip())
    assert captured_data["source"] == "SOURCE", "Source should match the input"
    assert captured_data["target"] == "DEFAULT_TARGET", (
        "Target should default to 'DEFAULT_TARGET'"
    )
    assert captured_data["message"] == "Index command executed successfully", (
        "Message should match the expected output"
    )


def test_commands_cli_handler_index_with_source_and_target(capsys):
    """
    Test the CLI handler with index command with source argument and target.
    """
    sys.argv = ["cli_handler", "index", "--source", "SOURCE", "--target", "TARGET"]

    cli_handler(commands_package="_commands")
    captured_data = json.loads(capsys.readouterr().out.strip())
    assert captured_data["source"] == "SOURCE", "Source should match the input"
    assert captured_data["target"] == "TARGET", "Target should default to 'target'"
    assert captured_data["message"] == "Index command executed successfully", (
        "Message should match the expected output"
    )


def test_commands_cli_handler_invalid_commands_package():
    # Test with an invalid commands package
    try:
        cli_handler(commands_package="invalid_package")
    except ImportError as e:
        assert str(e) == "No module named 'invalid_package'", (
            "Should raise ImportError for invalid package"
        )


def test_commands_cli_handler_no_commands_package():
    try:
        cli_handler()
    except AssertionError as e:
        assert str(e) == "The commands package must be provided", (
            "Should raise AssertionError for missing commands package"
        )

    try:
        cli_handler(commands_package="")
    except AssertionError as e:
        assert str(e) == "The commands package must not be an empty string", (
            "Should raise AssertionError for missing commands package"
        )

    try:
        cli_handler(commands_package=b"commands")
    except AssertionError as e:
        assert str(e) == "The commands package must be a string", (
            "Should raise AssertionError for missing commands package"
        )


def test_commands_cli_handler_non_existent_commands_package():
    try:
        cli_handler(commands_package="non_existent_package")
    except ImportError as e:
        assert str(e) == "No module named 'non_existent_package'", (
            "Should raise ImportError for non-existent package"
        )
