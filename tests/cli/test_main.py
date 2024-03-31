from skyler_cli.cli import main


class TestNoArgs:
    def test_no_args_exit_code(self, cli_runner):
        result = cli_runner.invoke(main.app, [])
        assert result.exit_code == 0

    def test_no_args_prints_help(self, cli_runner):
        result = cli_runner.invoke(main.app, [])
        assert main.help_msg in result.stdout
