from typer.testing import CliRunner
from skyler_cli import main

runner = CliRunner()


class TestNoArgs:
    def test_no_args_exit_code(self):
        result = runner.invoke(main.app, [])
        assert result.exit_code == 0

    def test_no_args_prints_help(self):
        result = runner.invoke(main.app, [])
        assert main.help_msg in result.stdout
