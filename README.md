<h1 align="center">SLINK</h1>

<h3 align="center">A Python Package for Classic Data Structures</h3>

<div align="center">
<br />

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

---

## Table of Contents
* [About](#about)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Authors](#authors)

## About <a name="about"></a>

Slink is a Python package library for classic data structures such as linked lists, trees, hash tables, queues, and stacks. These data structures are essential components in computer science, used to store, manage, and manipulate data efficiently. Slink provides a clean, reusable, and object-oriented interface for these data structures, making it easy to integrate them into your Python programs. We hope that Slink serves as a valuable resource for your Python programming needs!

If you'd like to contribute to Slink, you can submit bug reports, feature requests, or pull requests on the GitHub repository. Slink follows the Python Software Foundation's code of conduct and encourages contributions from all members of the community.

## Prerequisites <a name="prerequisites"></a>
The following must be installed on the host machine:

- [Python 3.9](https://github.com/pyenv/pyenv) or above

It is highly recommended to use `pyenv` to manage Python versions. This project is built in Ubuntu 22.04, but should also work on MacOS, as well as other Linux distros.

## Usage <a name="usage"></a>

To use Slink in your Python programs, simply import the desired data structure and create an instance of it:

```python
from slink.lists import LinkedList

# create a new singly linked list
my_list = LinkedList()

# add elements to the list
my_list.add(1)
my_list.add(2)
my_list.add(3)
```

Slink's data structures all have similar interfaces, making it easy to switch between them as needed. The package also includes detailed documentation and examples for each data structure.

## Authors <a name = "authors"></a>

- [Chino Franco](https://github.com/jgfranco17)