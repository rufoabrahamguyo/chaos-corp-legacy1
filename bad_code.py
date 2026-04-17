#!/usr/bin/env python3
"""Module docstring: This is a properly formatted Python module."""

import os
import json
import random


def good_function(param1: str, param2: int) -> str:
    """Function docstring explaining what this function does.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Description of return value
    """
    result = param1 * param2
    return str(result)


class MyClass:
    """Class docstring explaining the purpose of this class."""
    
    def __init__(self, name: str):
        """Initialize the class with a name."""
        self.name = name
    
    def get_name(self) -> str:
        """Return the name attribute."""
        return self.name


def safe_division(a: float, b: float) -> float:
    """Safely divide two numbers with error handling.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        Division result or 0 if division by zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0


def main() -> None:
    """Main function to demonstrate proper code."""
    my_instance = MyClass("test")
    print(my_instance.get_name())
    print(safe_division(10, 2))


if __name__ == "__main__":
    main()
