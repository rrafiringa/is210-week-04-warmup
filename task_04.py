#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Evaluation of resources for kittens. """


def too_many_kittens(kittens, litterboxes, catfood):
    """ Check if there are too many kitten per litterbox.

    Args:
        kittens (int): The number of kittens.
        litterboxes (int): The number of available litterboxes.
        catfood (bool): Boolean representing whether catfood exists.

    Returns:
        bool: Returns True, False or None

    Examples:
        >>> task_04.too_many_kittens(12, 12, False)
        True

        >>> task_04.too_many_kittens(13, 12, True)
        True

        >>> task_04.too_many_kittens(12, 13, True)
        False
    """

    return not (litterboxes >= kittens and catfood)
