# Newton Basins C++ Implementation (pybind11)

A Python/C++ (pybind11) package to generate newton basins images.


## Installation

### From PyPI
```
pip install nb-cpp
```

### From source code

```
pip install git+https://github.com/gmagno/nb-cpp.git
```

or

```
git clone git@github.com:gmagno/nb-cpp.git
cd nb-cpp/
make install
```

## Example Usage

Just run:

```python
import matplotlib as mpl  # don't forget to `pip install matplotlib` first
import matplotlib.pyplot as plt
import nb_cpp
hsv = nb_cpp.compute(
    imw=32, imh=32, # for more details, run: help(nb_py.compute)
)
rgb = mpl.colors.hsv_to_rgb(hsv)
plt.figure()
plt.imshow(rgb)
plt.show()
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
