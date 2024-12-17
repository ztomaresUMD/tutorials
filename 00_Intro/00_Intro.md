# Introduction to Computing for High Energy Physics, at MIT

An introduction to the basic tools and software you will need for doing research in High Energy Physics (HEP). Some of this is MIT-specific, as we rely on our in-house cluster, subMIT. Please go through all the *Exercises* to make sure you are read to use all the tools you need to do physics!

## Setting up your access to the subMIT cluster

We use the subMIT cluster to run our code. To access the cluster, follow the steps outlined in the ["Getting started" section](https://submit.mit.edu/submit-users-guide/starting.html) of the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/index.html).

You can now access the subMIT cluster using the terminal.

```sh
ssh <your_username>@submit.mit.edu
```

You will do your work here from now on, rather than on your laptop (unless your laptop has 100 cores and TBs of memory).

> *Exercise*: Log in to the subMIT cluster.

> *Exercise*: Please read the ["Getting started"](https://submit.mit.edu/submit-users-guide/starting.html) section, and any other sections you may find useful.

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

## JupyterHub

You can also access subMIT via JupyterHub, which provides a web-based interface to the cluster. You can access JupyterHub [https://submit.mit.edu/jupyter](https://submit.mit.edu/jupyter). Documentation for this can be found [in the subMIT User's Guide](https://submit.mit.edu/submit-users-guide/access.html#jupyterhub).

## VS Code

We suggest to use Visual Studio Code (VS Code) as a text editor. It is a powerful and user-friendly editor that is widely used in the scientific community. You can download it [here](https://code.visualstudio.com/).

> *Exercise:* Set up VS Code on the subMIT cluster; instructions can be found on the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/access.html#vscode).

## Python

Python is a high-level programming language that is widely used in scientific computing. It is known for its readability and ease of use. We will use (mostly) Python to write our code.

Two important things:
1. Various versions of Python exist. A basic one is already installed on the subMIT cluster, which we will use for now. Later, we will use the one determined by the FCC-ee software. Different versions can be installed, for example, with`conda`, a package manager for Python.
2. Python works with packages, which are downloadable libraries that extend the functionality of Python. These can be installed with `pip`, the Python package installer, or with `conda`, a package manager for Python.

> *Exercise*: A very simple tutorial for Python can be found in the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/tutorials/tutorial_1.html). A more in-depth tutorial for python for HEP is provided by the LHCb collaboration [here](https://hsf-training.github.io/analysis-essentials/python/README.html). If you've never worked with Python, go through these tutorials.

## Git

Git is a version control system that allows you to track changes in your code. It is widely used in the scientific community and is essential for collaborative work. We will use Git to manage our code. In particular, we will use GitHub, a platform that hosts Git repositories.

> *Exercise*: Make a GitHub account. Setup your GitHub keys on subMIT. Fork this repository (https://github.com/mit-fcc/tutorials). Navigate to the directory you created earlier, `fcc-ee`, and clone the repository in there. Edit the README file by adding your name and the project you are working on, and push the changes to your fork. Navigate to the repository on GitHub's website and check that the changes are there.

## Personal Website on subMIT

As documented in the [subMIT User's Guide](https://submit.mit.edu/submit-users-guide/starting.html#creating-a-personal-webpage), you can create a directory called `public_html` in your home directory on the subMIT cluster. Any files you put in this directory will be accessible on the web at `http://submit08.mit.edu/~<username>/`. This is a great way to share your scripts, plots, etc. with others.

> *Exercise*: Add a file in your `public_html` directory and navigate to it in your browser.

You can add your own .php files to your `public_html` directory to edit the style of your webpage.

## FCCAnalyses Software

The FCC collaboration has put together a common framework for analyses. You can find more information, tutorials, and documentation on their website [https://hep-fcc.github.io/FCCAnalyses/](https://hep-fcc.github.io/FCCAnalyses/). The code itself lives on GitHub, in the [FCCAnalyses repository](https://github.com/HEP-FCC/FCCAnalyses). 

> *Exercise*: These are MIT-specific instructions for setting this up. Jan (MIT email: jaeyserm) has modified some of the software to work best on our subMIT cluster; you can find it in [his fork of the main repo](https://github.com/jeyserma/FCCAnalyses). You don't need to clone this yourself, as he has already cloned it on subMIT, so we can just use it from there. The way to do this is, upon logging in to subMIT, run the following command:
    
    source /work/submit/jaeyserm/software/FCCAnalyses/setup.sh

>  What this does is to set up an environment for you. Namely, your shell now "knows" about the FCCAnalyses software, and you can use it. You can check that this worked by running the following command:

    which python

> This should return the path to the python executable that is part of the FCCAnalyses software. Something like `/cvmfs/sw.hsf.org/key4hep/releases/2024-03-10/x86_64-almalinux9-gcc11.3.1-opt/python/3.10.13-od343s/bin/python`. If it does, you are good to go.

## Conclusion

If you've gone through everything here, you are now ready to start learning about the basics of analysis and computing for HEP.