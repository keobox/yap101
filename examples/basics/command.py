
"Launch an external command."

import subprocess

p = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
out = p.stdout.read()
print(out)
