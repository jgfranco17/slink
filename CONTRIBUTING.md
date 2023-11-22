# How to develop on this project

project_template welcomes contributions from the community.

**You need PYTHON3!**

This instructions are for linux base systems. (Linux, MacOS, BSD, etc.)

## Setting up your own fork of this repo

- On github interface click on `Fork` button.
- Clone your fork of this repo. `git clone git@github.com:YOUR_GIT_USERNAME/slink.git`
- Enter the directory `cd slink`
- Add upstream repo `git remote add upstream https://github.com/jgfranco17/slink`

### Setting up your own virtual environment

Run `make virtualenv` to create a virtual environment.
then activate it with `source .venv/bin/activate`.

### Install the project in develop mode

Run `make install` to install the project in develop mode, then run `make test` to run the tests.

### Create a new branch to work on your contribution

Checkout this branch by running the following command.

```bash
git checkout -b <branch_name>
```

Please ensure to use logical and proper naming for your branch.

## Make your changes

Edit the files using your preferred editor (we recommend VIM or VSCode). Save and check that everything still works.

## Pre-commit checks

This project strives to follow PEP8 guidelines. Use `black` as a formatter for ease of formatting.

For convenience, the following Makefile commands may come in handy.

```bash
make lint  # Run black, flake8, and pylint on package files
make test  # Run pytest and coverage tests
```

## Commit your changes

This project uses [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

Example: `fix(package): update setup.py arguments 🎉` (emojis are fine too)

## Push your changes to your fork

Run `git push origin my_contribution`

## Submit a pull request

On github interface, click on `Pull Request` button. Wait CI to run and one of the developers will review your PR. Please be descriptive in your PR descriptions.
