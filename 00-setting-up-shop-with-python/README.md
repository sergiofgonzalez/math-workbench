# 00 &mdash; Setting Up Shop with Python
> Python setup and summary notes for Math related examples

## Introduction
We will be using Python 3. The easiest way to start for Python beginners is to download and install Anaconda from https://anaconda.com.

The Anaconda packages will be installed under `home/ubuntu/anaconda3`.

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