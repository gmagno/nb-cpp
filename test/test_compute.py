
import numpy as np

import nb_cpp

def test_compute_defaultargs():
    expected_rounded_hsv = np.array([
        [[0.000, 1., 0.533], [0.333, 1., 0.567], [0.333, 1., 0.567]],
        [[0.000, 1., 0.600], [0.000, 1., 0.733], [0.667, 1., 0.733]],
        [[0.167, 1., 0.600], [0.167, 1., 0.733], [0.833, 1., 0.733]],
    ])
    hsv = np.round(nb_cpp.compute(
        imw=3, imh=3,
        coefs=np.array([1, 0, 0, 0, 0, 0, 1], dtype=np.float),
        crmin=-5.0, crmax=5.0,
        cimin=-5.0, cimax=5.0,
        itmax=30, tol=1e-6
    ), decimals=3)
    assert np.allclose(hsv, expected_rounded_hsv), \
        'Computed array and expected array are different.'

def test_compute_nullsize():
    hsv = np.round(nb_cpp.compute(
        imw=0, imh=0,
        coefs=np.array([1, 0, 0, 0, 0, 0, 1], dtype=np.float),
        crmin=-5.0, crmax=5.0,
        cimin=-5.0, cimax=5.0,
        itmax=30, tol=1e-6
    ), decimals=3)
    assert hsv.size == 0, \
        'Expected and empty array.'
