# Introduction to Computing for High Energy Physics at MIT

An introduction to the basic tools and software you will need for doing research in High Energy Physics (HEP). Some of this is MIT-specific, as we rely on our in-house cluster, subMIT. Please go through all the *Exercises* to make sure you understand the material.

## Setting up your access to the subMIT cluster

We use the subMIT cluster to run our code. To access the cluster, follow the steps outlined in the ["Getting started" section](https://submit.mit.edu/submit-users-guide/starting.html) of the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/index.html).

You can now access the subMIT cluster using the terminal.

```sh
ssh <your_username>@submit.mit.edu
```

You will do your work here from now on, rather than on your laptop (unless your laptop has 100 cores and TBs of memory).

> *Exercise*: Log in to the subMIT cluster.

> *Exercise*: Did you read the section "Login and basic areas"? This is important. Understand the difference between the home, work, and ceph directories.

## The command line

We are ready to use the terminal. Finally, you can be just like Mr. Robot, and impress all your family and friends. Covering the full of use of the command line is far outside the scope of this tutorial, but we will cover the basics. A more comprehensive guide can be found [here](https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal).

Basic commands:

- `ls`: List the contents of the current directory.
- `cd`: Change the current directory.
- `pwd`: Print the current directory.
- `mkdir`: Create a new directory.
- `rm`: Remove a file (warning: there is no Trash, it will be forever deleted).
- `cp`: Copy a file.
- `mv`: Move a file.
- `cat`: Print the contents of a file.
- `vim`: Open a file in the vim text editor.
- `history`: Show a list of previous commands.

Basic shortcuts:
- `tab`: Autocomplete a command or file name.
- `up arrow`: Scroll through previous commands.
- `ctrl + c`: Stop a running command.
- `ctrl + d`: Exit the terminal.
- `ctrl + l`: Clear the terminal.
- `ctrl + r`: Search through previous commands.

> *Exercise*: In your home space, create a new directory called `fcc-ee`, and navigate to it. Print the full path of your current directory.

## VS Code

We suggest to use Visual Studio Code (VS Code) as a text editor. It is a powerful and user-friendly editor that is widely used in the scientific community. You can download it [here](https://code.visualstudio.com/).

> *Exercise:* Set up VS Code on the subMIT cluster; instructions can be found on the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/access.html#vscode).

> *Tip*: You can use your MIT account to download GitHub Copilot as an extension to VS Code. This is really neat. If you already have programming experience, we suggest you use this. If this is your first time programming, we suggest you don't use it, as you should learn the basics first.

## Python

Python is a high-level programming language that is widely used in scientific computing. It is known for its readability and ease of use. We will use (mostly) Python to write our code.

Two important things:
1. Various versions of Python exist. A basic one is already installed on the subMIT cluster, which we will use for now. Later, we will use the one determined by the FCC-ee software. Different versions can be installed, for example, with`conda`, a package manager for Python.
2. Python works with packages, which are downloadable libraries that extend the functionality of Python. These can be installed with `pip`, the Python package installer, or with `conda`, a package manager for Python.

> *Exercise*: A very simple tutorial for Python can be found in the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/tutorials/tutorial_1.html). A more in-depth tutorial for python for HEP is provided by the LHCb collaboration [here](https://hsf-training.github.io/analysis-essentials/python/README.html). If you've never worked with Python, go through these tutorials.

## Git

Git is a version control system that allows you to track changes in your code. It is widely used in the scientific community and is essential for collaborative work. We will use Git to manage our code. In particular, we will use GitHub, a platform that hosts Git repositories.

A tutorial for Git can be found in the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/tutorials/tutorial_4.html).

> *Exercise*: Make a GitHub account. Setup your GitHub keys on subMIT. Fork this repository (https://github.com/mit-fcc/tutorials). Navigate to the directory you created earlier, `fcc-ee`, and clone the repository in there. Edit the README file by adding your name and the project you are working on, and push the changes to your fork. Navigate to the repository on GitHub's website and check that the changes are there.

## Personal Website on subMIT

As documented in the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/starting.html#creating-a-personal-webpage), you can create a directory called `public_html` in your home directory on the subMIT cluster. Any files you put in this directory will be accessible on the web at `hhttp://submit08.mit.edu/~<username>/`. This is a great way to share your scripts, plots, etc. with others.

> *Exercise*: Add a file in your `public_html` directory and navigate to it in your browser.

You can add your own .php files to your `public_html` directory to edit the style of your webpage.

## Conclusion

If you've gone through everything here, you are now ready to start learning about the basics of 