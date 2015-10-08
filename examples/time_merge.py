
"Merge two log files"

import re
import heapq
# select lines w/ timestamp
timestamped_lines = re.compile(r'^(\d+\-\d+\-\d+\s+\d+:\d+:\d+,\d+)')
with open('inventory.log') as inventory:
    with open('ifm_inventory.log') as ifm_inventory:
        inventory_lines = (line for line in inventory if timestamped_lines.match(line))
        ifm_inventory_lines = (line for line in ifm_inventory if timestamped_lines.match(line))
        for n, line in enumerate(heapq.merge(inventory_lines, ifm_inventory_lines)):
            print n, line.strip()
