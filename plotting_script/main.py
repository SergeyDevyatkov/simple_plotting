from pathlib import Path

from plotting_script.excel_reader import read_excel
from plotting_script.plotter import create_plot, save_plot

SPREADHEETS_PATH = Path().absolute() / "spreadsheets"
PATH_TO_SAVE_PLOTS = Path().absolute() / "plots"


def make_plots_savefolder():
    if not PATH_TO_SAVE_PLOTS.exists():
        PATH_TO_SAVE_PLOTS.mkdir()


def log_plotting_status(plot_name):
    print(f"Plotting {plot_name}...")


def add_conclusion(path: Path, conclusion: str | None):
    if conclusion is None:
        return

    conclusion_tag = f"<div style='text-align: left; font-size: 18px; font-family: monospace; position: relative; bottom: 20px'>{conclusion}</div>\n"
    with open(path, "r") as f:
        lines = f.readlines()

    lines.insert(-2, conclusion_tag)
    with open(path, "wt") as f:
        f.writelines(lines)


def main():
    make_plots_savefolder()
    data = read_excel(SPREADHEETS_PATH)

    for data_to_plot in data:
        log_plotting_status(data_to_plot.plot_name)

        fig = create_plot(data_to_plot)
        save_plot(fig, PATH_TO_SAVE_PLOTS / data_to_plot.plot_filename)
        add_conclusion(
            PATH_TO_SAVE_PLOTS / data_to_plot.plot_filename, data_to_plot.conclusion
        )


if __name__ == "__main__":
    main()
