
"Change a string recursively."

import sys
import os

current, new = sys.argv[1:3]
print current, new

for current_dir, dirs, files in os.walk('.'):
    for fn in files:
        filename = os.path.join(current_dir, fn)
        with open(filename, 'rb') as f:
            text = f.read()
        if current in text:
            print(filename)
            print text
            text.replace(current, new)
            print text
            with open(filename + '.new', 'wb') as f:
                f.write(text)
            os.rename(filename, filename + '.bak')
            os.rename(filename + '.new', filename)
