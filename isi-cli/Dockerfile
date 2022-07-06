FROM python:3.8-slim

RUN pip3 install --no-cache-dir poetry==1.1.12

WORKDIR /icli

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

ENTRYPOINT [ "poetry", "run", "python", "/icli/isi-cli/main.py" ]
