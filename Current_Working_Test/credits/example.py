#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from credit import credit

display.set_mode((512, 448))

text = """CREDITS
_                                                 _

_Programming_\\John Taylor


_Artwork_\\Aaron Guishard
\\John Taylor


_Game Idea_\\NES Punch Out!

_Reddit Pygame_\\metulburr
\\iminurnamez
\\Mekire

_Special Thanks_\\ Jonathan Taylor
\\Christian Taylor

Visit Our Website for more on Python Gaming.
http://www.pythongaming.com
_                                                 _

No © Copyright 2015"""

font = font.Font("Roboto-MediumItalic.ttf",20)
color = 0xa0a0a000

credit(text,font,color)
