# BeeKeeper Datascience Baseline

This is a very simple tutorial that can be containerized, but does not need to be.

## Prerequisite

Install [Python 3](https://www.python.org/downloads/)!

Install the VirtualEnv package by running:
```bash
pip install virtualenv
```

You're set! If you have any questions about these prerequisites or run into trouble, contact Pavan and Lu!

## Installation

You need to simply run:

```bash
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Lets keep it as simple as possible, just run:

```bash
python3 app.py
```

## Modfying this

Everything is contained in one file `app.py` and you can safely edit that file to change things and add things. This can serve as a start to your code modification.

## FAQ:

### What is Virtualenv?
Technically, this is not required, and if you run into trouble with this, you can simply skip the steps and run:

```bash
pip install -r requirements.txt
python3 app.py
```

The virtualenv module keeps libraries away from the rest of your system and is seen as an almost universal pre-requisite to keep your environment clean. If you have trouble with this, contact Pavan and Lu!

### Why is there a Dockerfile here?
This tutorial can include an advanced step of creating a container for this practice code, but for now, you can safely ignore it. If you happen to want to experiment with it to learn a more advanced topic, you can run:

```bash
docker build . -t bkexample:latest
docker run bkexample:latest
```

### I need help!
You're in good hands. Find Pavan and Lu and we can pair up and help you learn!
