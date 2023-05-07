<h1 align="center">SLINK</h1>

<h3 align="center">A Python Package for Classic Data Structures</h3>

<div align="center">
<br />

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/license-BSD3Clause-blue?style=for-the-badge)

</div>

---

## Table of Contents
* [About](#about)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Authors](#authors)

## About <a name="about"></a>

### Overview

Slink is a Python package library for [classic data structures](https://www.geeksforgeeks.org/data-structures/). These data structures are essential components in computer science, used to store, manage, and manipulate data efficiently. Slink provides a clean, reusable, and object-oriented interface for these data structures, making it easy to integrate them into your Python programs. We hope that Slink serves as a valuable resource for your Python programming needs!

We welcome contributions from the open source community. If you find a bug or have a feature request, please open an issue on the GitHub repository. If you'd like to contribute code, please fork the repository and submit a [pull request](.github/PULL_REQUEST_TEMPLATE.md) with your changes. Slink follows the Python Software Foundation's [code of conduct](https://www.python.org/psf/conduct/) and encourages contributions from all members of the community. Before contributing, please review the contribution guidelines and code of conduct to ensure that your contributions are in line with our standards and values.

### Motivation
Data structures are an essential part of computer science and software engineering. They are used to store and organize data efficiently and provide fast access and manipulation of data. A solid understanding of data structures is crucial for building efficient algorithms and scalable software systems. Oftentimes, these data structures and algorithms are used when preparing for programming interviews. However, implementing data structures from scratch can be time-consuming and error-prone. This is where Slink comes in - it provides a pre-built implementation of popular data structures, allowing developers to focus on solving the problem at hand rather than the underlying data structures.

### Technologies Used
Slink is built entirely in Python, a popular general-purpose programming language known for its simplicity, readability, and versatility. The library uses object-oriented programming (OOP) principles to provide a clean and reusable implementation of data structures.

All data structures are implemented as classes, with methods for common operations such as insertion, deletion, and traversal. In addition, Slink includes a set of common algorithms for working with graphs, such as breadth-first and depth-first traversal.

## Prerequisites <a name="prerequisites"></a>
The following must be installed on the host machine:

- [Python 3.9](https://github.com/pyenv/pyenv) or above

It is highly recommended to use `pyenv` to manage Python versions. This project is built in Ubuntu 22.04, but should also work on MacOS, as well as other Linux distros.

### Python dependencies

To get started with this project for development purposes, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/slink.git
cd slink
pip install -r requirements.txt
```

## Usage <a name="usage"></a>

To use Slink in your Python programs, simply import the desired data structure and create an instance of it:

```python
from slink.lists import LinkedList

# Create a new singly linked list
my_list = LinkedList()

# Add elements to the list
my_list.add(1)
my_list.add(2)
my_list.add(3)

# Print out the linked list
my_list.display()
```

The Slink repository also includes detailed documentation and examples for each data structure. Please check the [documentation directory](https://github.com/jgfranco17/slink/tree/main/docs) for further references.

## Testing <a name = "testing"></a>

### Running unittest suite

In order to run diagnostics and unittests, first install the testing dependencies. This will allow you to utilize the full capacity of the test modules we have built.

```bash
pip install -r requirements-test.txt
```

To run the full test suite, run the Makefile command as follows:

```bash
cd slink
make test
```

### Using PyTest

You can run these tests using the [PyTest](https://docs.pytest.org/en/7.3.x/) CLI tool. To run all tests in the directory containing the test files, navigate to the directory and enter `pytest` in the command line; for added verbosity, add the `-vv` flag after. To run a specific test file, enter `pytest <filename>`.

```bash
# Run all tests in the testing module with verbose detail
cd slink
pytest -vv

# Or, run a specific test file
cd slink/tests
pytest -v <filename>.py
```

This will run the specified test module and generates a detailed result report in the terminal.

### Why these tests are important

Running these unittests is necessary to ensure that the code is functioning as expected and meeting the requirements of the design specification. The unittests are designed to test each function and method of the code and to identify any errors or unexpected behavior. By testing the code using these PyTest unittests, we can ensure that the code meets the specified requirements and that any changes made to the code do not introduce new bugs or errors.

In addition, these tests can be automated to run on every code change, allowing us to quickly identify any issues that may arise and enabling us to maintain a high level of code quality. 

In essence, running these PyTest unittests is a critical part of the software QA process and helps to ensure that our code is robust, reliable, and meets the needs of our end-users before the product hits deployment.

## Authors <a name = "authors"></a>

- [Chino Franco](https://github.com/jgfranco17)