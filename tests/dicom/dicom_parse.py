import json
from pathlib import Path

from skylers_cli.cli import main


class TestParseSingleDICOMFile:
    def test_parse_single_file_to_pprint(self, cli_runner):
        test_file_path = Path(__file__).parent / "SC_rgb_jpeg.dcm"
        result = cli_runner.invoke(main.app, ["dicom", str(test_file_path)])
        print(result.stdout)
        assert result.exit_code == 0
        assert "File Meta Information Group Length" in result.stdout

    def test_parse_single_file_to_json(self, cli_runner):
        test_file_path = Path(__file__).parent / "SC_rgb_jpeg.dcm"
        result = cli_runner.invoke(
            main.app, ["dicom", str(test_file_path), "--fmt", "json"]
        )
        assert result.exit_code == 0

        result_json = json.loads(result.stdout)
        assert result_json["00080018"] == {
            "Value": [
                "1.2.826.0.1.3680043.8.498.13002811185086637637347356263722492924"
            ],
            "vr": "UI",
        }
