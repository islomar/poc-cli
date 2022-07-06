# icli

## Development set up
### Without Docker
- You need to install [poetry](https://python-poetry.org/docs/#installation)
- Run `poetry install`
- Run `poetry run python src/main.py`
- Run `poetry run python src/main.py --name=Batman --count=2`
- Run `poetry run python src/main.py --help`

## With Docker
- `docker build -t icli .`
- `docker run --entrypoint=ls icli`
- `docker run icli`

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
- The [ENTRYPOINT](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint) is the execution of the main file.

## Resources
- [Video tutorial: Building Command Line Applications with Click](https://www.youtube.com/watch?v=kNke39OZ2k0) - 18 minutes
- [Click examples](https://click.palletsprojects.com/en/7.x/quickstart/#screencast-and-examples)
- https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker

## TO DO
- Run it locally with Docker
- Package it to be installed from pypi, e.g. `pip install icli`
- Make possible to run it 