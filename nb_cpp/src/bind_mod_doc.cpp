
#include "bind_mod_doc.h"

void bind_doc(py::module &m)
{
    m.doc() = R"pbdoc(Newton Basins (nb_cpp) plugin)pbdoc";
}
