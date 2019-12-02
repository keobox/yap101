"Example of application main using from."

from mymodule import fun
from mypkg import pkg_mod
from mypkg import f1

print(__doc__)
print(fun())
print(f1())
print(pkg_mod.f2())