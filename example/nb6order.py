
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import nb_cpp

def main():
    hsv = nb_cpp.compute(
        imw=128, imh=128,
        coefs=np.array([1, 0, 0, 0, 0, 0, 1], dtype=np.float),
        crmin=-5.0, crmax=5.0,
        cimin=-5.0, cimax=5.0,
        itmax=30, tol=1e-6
    )
    rgb = mpl.colors.hsv_to_rgb(hsv)
    plt.figure('Example: Newton Basins 6th order poly.')
    plt.imshow(rgb)
    plt.show()

if __name__ == '__main__':
    main()
