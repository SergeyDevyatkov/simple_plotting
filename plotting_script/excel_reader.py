from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from plotting_script.config import SPREADSHEET_CONFIG


@dataclass
class PlotData:
    plot_name: str
    dataframe: pd.DataFrame
    conclusion: str | None
    right_axis_tags: list[str] = field(default_factory=list)

    @classmethod
    def from_config(cls, config: dict, dataframe: pd.DataFrame):
        plot_name: str = config["spreadheet"].split(".")[0]
        right_axis_tags = config.get("right_axis", [])
        conclusion = config.get("conclusion", None)

        return cls(
            plot_name=plot_name,
            dataframe=dataframe,
            right_axis_tags=right_axis_tags,
            conclusion=conclusion,
        )

    @property
    def plot_filename(self) -> str:
        return self.plot_name + ".html"


def read_excel(folder: Path):
    data: list[PlotData] = []

    for config in SPREADSHEET_CONFIG:
        file_name: str = config["spreadheet"]
        sheet: str = config["sheet"]
        dataframe = pd.read_excel(
            folder / file_name,
            sheet_name=sheet,
            header=0,
            index_col=0,
            parse_dates=True,
        )

        data.append(PlotData.from_config(config, dataframe))

    return data
