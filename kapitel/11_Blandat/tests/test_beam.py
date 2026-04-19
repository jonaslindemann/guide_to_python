#!/usr/bin/env python3
# --- coding: utf-8 -*-

from pytest import approx

import beam

def test_bending_stiffness():
    assert beam.bending_stiffness(210e9, 1e-4) == 21e6

def test_bending_stiffness_zero():
    assert beam.bending_stiffness(0, 1e-4) == 0.0

def test_bending_stiffness_greater_than_zero():
    assert beam.bending_stiffness(210e9, 1e-4) > 0.0

def test_bending_stiffness_approx():
    assert beam.bending_stiffness(210e9, 1e-4) == approx(21e6, rel=1e-6)
