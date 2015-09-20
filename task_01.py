#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """ Prints "Know what I mean?" with a variable number of winks.
    Args:
        wink (mixed): Represents a wink.
        numwink (int): Wink multiplier. Defaults to 2.
    Returns:
        str: Arguments are contatenated in a sentence.
    Examples:
        >>> know_what_i_mean('wink')
       'Know what I mean? winkwink, nudge nudge'
        >>> know_what_i_mean('wink', 3)
       'Know what I mean? winkwinkwink, nudge nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
