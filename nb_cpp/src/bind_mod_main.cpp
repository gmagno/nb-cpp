
#include "bind_mod_main.h"

PYBIND11_MODULE(nb_cpp, m)
{
    bind_compute(m);
    bind_doc(m);

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
