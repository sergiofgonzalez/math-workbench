# 00 &mdash; Setting Up Shop with Python
> Python setup and summary notes for Math related examples

## Introduction
We will be using Python 3. The easiest way to start for Python beginners is to download and install Anaconda from https://anaconda.com.

The Anaconda packages will be installed under `home/<username>/anaconda3`.

Once installed, you can do:

```bash
$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Typing *CTRL+D* or `exit()` will let you exit the REPL interactive session.

The *REPL* will also allow you to enter multi-line inputs, like the canonical hello world:

```python
>>> def sayHelloWorld():
...   print("Hello, world!")
...
>>> sayHelloWorld()
Hello, world!
>>>
```

Or simple mathematical functions:

```python
>>> def f(x):
...   return x * x
...
>>> f(5)
25
>>>
```

## Creating and Running Script Files
Installed Python extension in VSCode typying *CTRL+P* and then: `ext install ms-python.python`. Then I had to click on the status line at the bottom to switch from the default Python environment to the Python *conda* distribution.

Also, wanted to remove the `"(base)"` from the prompt, so I did: `conda config --set auto_activate_base false`

## Running Jupyter Notebooks
A Jupyter Notebook is a graphical interface for coding in Python.

To open the Jupyter Notebook interface type `python -m notebook`.

## Configuring Pylance
If you are using Pylance for linting your code, the tool will be reporting missing imports such as:

![Pylance missing import](images/pylance_missing_import.png)

You can fix this by configuring your user setting with a few additional paths:

Python > Analysis > Extra Paths

+ `./lib`   <- for your local libraries
+ `/home/<your-user>/anaconda3/bin`   <- anaconda bin packages
+ `/home/ubuntu/anaconda3/lib/python3.8/site-packages`   <- additional packages

## FAQs

### 1. When I type `python --version` I get 2.x.y instead of 3.x.y, how do I fix this?
Type `conda activate` to activate the Python version from the Conda distribution

### 2. How do update the Anaconda distribution?
Type `conda update conda`

## Useful References

+ [Anaconda Individual Distribution User's Guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)
