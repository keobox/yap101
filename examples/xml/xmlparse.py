
"Parse xml file."

import xml.etree.ElementTree as ET

ns = 'http://www.cisco.com/nxos:7.2.0.D1.1.:lcmcli'
nf = "urn:ietf:params:xml:ns:netconf:base:1.0"

mod = ET.parse('show_output.xml').getroot()
rows = mod.findall('{%s}data/{%s}show/{%s}module/{%s}__readonly__/{%s}TABLE_modinfo/{%s}ROW_modinfo' %
                  (nf, ns, ns, ns, ns, ns))
for row in rows:
    modtype = row.find('{%s}modtype' % ns)
    status = row.find('{%s}status' % ns)
    print(modtype.text, status.text)
