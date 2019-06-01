
import time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import nb_cpp

def main():
    crmin = -10.0
    crmax = 10.0
    cimin = -5.0
    cimax = 5.0
    ratio = (crmax - crmin) / (cimax - cimin)

    # imw = 2048
    # imw = 4096
    # imw = 8192
    imw = 1024

    t = time.time()
    hsv = nb_cpp.compute(
        imw=imw, imh=int(imw/ratio),
        coefs=np.array([1, 0, 0, 0, 0, 0, 1], dtype=np.float),
        crmin=crmin, crmax=crmax,
        cimin=cimin, cimax=cimax,
        itmax=30, tol=1e-6
    )
    e = time.time() - t
    print('Elapsed time: %.2f' % (e,))

    rgb = mpl.colors.hsv_to_rgb(hsv)
    plt.figure('Example: Newton Basins 6th order poly.')
    plt.imshow(rgb)
    plt.show()

if __name__ == '__main__':
    main()
