### Plotting script for HTML plots


## Install poetry

In powershell run (detailed instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer)):
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Usage

1. In `PowerShell` cd to project folder:
```
cd path/to/plotting-script/folder
```
2. Install project
```
poetry install
```
3. Copy excel files to spreadsheets folder
4. Adjust `plotting_script/config.py` file
5. In PowerShell run 
```
poetry run main
```
