import parser
filename = input("enter file")
source =  open(filename,"r")
asm = source.readlines()
parser.parse(asm,'Add')
