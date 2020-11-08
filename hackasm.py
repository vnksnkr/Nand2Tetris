import parser



source =  open("Pong.asm","r")
asm = source.readlines()
parser.parse(asm,'Add')