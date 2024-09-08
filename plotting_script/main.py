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


def main():
    make_plots_savefolder()
    data = read_excel(SPREADHEETS_PATH)

    for data_to_plot in data:
        log_plotting_status(data_to_plot.plot_name)

        fig = create_plot(data_to_plot)
        save_plot(fig, PATH_TO_SAVE_PLOTS / data_to_plot.plot_filename)


if __name__ == "__main__":
    main()
