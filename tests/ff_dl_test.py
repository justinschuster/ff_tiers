"""
Written by Justin Schuster
This file tests the functions found in
ff_dl.py.
"""
import unittest
import os, sys, inspect

# Hacked this up so I could import ff_dl 
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import ff_dl 

ff_dl.test()