#!/usr/bin/env python3
# --- coding: utf-8 -*-

def bending_stiffness(E, I):
    """Beräknar böjstyvhet EI."""
    return E * I

# Felaktig implementation av böjstyvhet, den ska inte vara negativ

# def bending_stiffness(E, I):
#     """Beräknar böjstyvhet EI."""
#     return -(E * I)


