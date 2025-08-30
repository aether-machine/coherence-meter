#!/usr/bin/env python3
"""
sim_double_slit.py
Simulate electron double-slit interference with partial coherence.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi
import csv
import os
from scipy.constants import h, m_e, e as q_e

# ============== parameters ==============
energies_eV = [50, 100, 1000]   # eV
d = 1.0e-6      # slit separation (m)
a = 100e-9      # slit width (m)
L = 1.0         # screen distance (m)

Lc_values = [np.inf, 1e-6, 1e-7, 1e-8]  # coherence lengths (m)

# output folder
out_dir = "figs"
os.makedirs(out_dir, exist_ok=True)

def de_broglie_wavelength(E_eV):
    E_J = E_eV * q_e
    p = np.sqrt(2 * m_e * E_J)
    return h / p

def envelope(a, lam, x, L):
    beta = pi * a * x / (lam * L)
    # np.sinc expects normalized argument: sin(pi x)/(pi x)
    return (np.sinc(beta/pi))**2

def visibility(delta, Lc):
    if np.isinf(Lc):
        return np.ones_like(delta)
    return np.exp(-(delta / Lc)**2)

# iterate energies
for E in energies_eV:
    lam = de_broglie_wavelength(E)
    fringe_spacing = lam * L / d
    num_fringes = 40
    x_max = num_fringes * fringe_spacing
    x = np.linspace(-x_max, x_max, 4001)
    delta = d * x / L
    env = envelope(a, lam, x, L)

    for Lc in Lc_values:
        V = visibility(delta, Lc)
        I = env * (1 + V * np.cos(2 * pi * delta / lam))
        I = I / I.max()

        # plot
        plt.figure(figsize=(8,4))
        plt.plot(x*1e3, I, lw=1)
        plt.title(f"E={E} eV, lambda={lam*1e9:.3f} nm, Lc={'inf' if np.isinf(Lc) else f'{Lc*1e6:.3f} um'}")
        plt.xlabel("screen x (mm)")
        plt.ylabel("Normalized intensity")
        plt.grid(True, ls=':')
        fname = f"E{E}eV_Lc_{('inf' if np.isinf(Lc) else str(int(Lc*1e9))+'nm')}.png"
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, fname), dpi=200)
        plt.close()
