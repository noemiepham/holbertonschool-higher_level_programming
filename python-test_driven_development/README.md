Python - Test-driven development

General
## Why Python programming is awesome
## What’s an interactive test
## Why tests are important

Goal of python unit testing is to detect as many bugs and inconsistencies in the infancy of the application development as possible. This is achieved by designing and scripting accurate and quality unit tests that can also serve as detailed documentation for the development process. This ensures that bugs and other problems we catch in the first stages of the development, can be fixed by the development team.

## How to write Docstrings to create tests

There are several common ways to use doctest:

- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.

- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.

- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

## How to write documentation for each module and function

A Python doctest is written as though it is a comment, with a series of three quotation marks in a row — """ — at the top and bottom of the doctest.

To document functions in Python, use docstrings (triple quotation marks).

```
def greet(name):
    """ Greets a person with their name. """
    print(f"Hello, {name}")
```

A documentation string or docstring is a triple-quote string. It can be added to the first line of a function, class, or module. It acts as the documentation of that piece of code.

## What are the basic option flags to create tests


## How to find edge cases

Basically, testers use creativity and critical thinking to find edge case defects during any test cycle — regression, functional, or at any point in the development cycle. Testers try to find edge cases all the time, or as much as they can spend the time on — that’s the reality.

