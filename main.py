"Example of application main using import."

import mymodule
import mypkg
from mypkg import pkg_mod

print(__doc__)
print(mymodule.fun())
print(mypkg.f1())
print(pkg_mod.f2())