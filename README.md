# Description

A simple tool for the support team that allows to manage incidents.

##
Resources:
- [Django](https://www.djangoproject.com/)
- [Skeleton (CSS)](https://getskeleton.com/)
- [HTMX](https://htmx.org/)

# Installation

## Requirements

- `python-3.12.x`
- `uv` ([documentation](https://astral.sh/blog/uv))
- `docker`, `docker compose`

## Run locally

> NOTE: It's better to follow best practice and create virtual environment

- Install dependencies for better dev experience (go to definition, autocomplete, etc) or running the project without `Docker`
  - Using `Makefile`
    ```
    make deps
    ```
  - using `pip`
    ```
    pip install -r req requirements.txt requirements-dev.txt
    ```
- Run the project
  - using `Docker`
    ```
    docker compose up -d
    ```
  - using `manage.py` (requires installed dependencies)
    ```
    python src/manage.py runserver
    ```
