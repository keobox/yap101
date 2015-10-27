
"optparse example"

import optparse

usage = "usage: %prog [options] [args]"
parser = optparse.OptionParser(usage)
parser.add_option("-b", "--bool", action="store_true", dest="bool",
                  default=False, help="A boolean option (default=false)")
parser.add_option("-f", "--float", dest="float", type="float", default=10.0,
        help="A Float option (default=10.0)")
parser.add_option("-s", "--string", dest="string", default="defaultstr",
                 help="A string option (default=defaultstr)")
parser.add_option("-i", "--int", dest="int", type="int", default=51,
                  help="An Integer option (default=51)")
(options, args) = parser.parse_args()

print(options)
print(args)
