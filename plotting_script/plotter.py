from pathlib import Path
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from plotting_script.excel_reader import PlotData


def create_plot(data: PlotData):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    dataframe = data.dataframe

    x = list(dataframe.index)
    for tag in dataframe.columns:
        is_secondary = tag in data.right_axis_tags
        y = list(dataframe[tag].values)

        fig.add_trace(
            go.Scatter(x=x, y=y, name=tag, mode="lines"),
            secondary_y=is_secondary,
        )

    fig.update_layout(title_text=data.plot_name)

    return fig


def save_plot(fig: go.Figure, path: Path):
    fig.write_html(path)
