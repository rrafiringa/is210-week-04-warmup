#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Function with default parameter values. """


def defaults(my_required, my_optional=True):
    """ Function with default param values defined.
    Args:
        my_required (mixed): Variable defaulting to None.
        my_optional (bool): Boolean variable defaulting to True.
    Returns:
        bool: Returns True or False
    Examples:
        >>> task_05.defaults(True)
        True
        >>> task_05.defaults(True, False)
        False
        >>> task_05.defaults(False, False)
        True
    """

    return my_optional is my_required
