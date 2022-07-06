# icli

## Development set up
### Without Docker
- You need to install [poetry](https://python-poetry.org/docs/#installation)
- Run `poetry install`
- Run `poetry run python src/main.py`


## Decisions taken
- Origin of the name: 
    - i(si) + cli
    - or the typical iAnything :-)
- Library used: **Click**
    - The examples of code seen look simpler
    - Good opinions in several posts with comparisons with Docopts or Argparse
    - Looks like a "modern" way of creating a CLI in 2022
    - Used by AWS
- Dependencies with [**poetry**](https://python-poetry.org/)