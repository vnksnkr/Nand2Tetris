comp = {"0":"0101010","1":"0111111","-1":"01110101","D":"0001100","A":"0110000","!D":"0001101",
	   "!A":"0110001","-D":"0001111","-A":"0110011","D+1":"0011111","A+1":"0110111","D-1":"0001110"
	   ,"A-1":"0110010","D+A":"0000010","D-A":"0010011","A-D":"0000111","D&A":"0000000","D|A":"0010101",
	   "M":"1110000","!M":"1110001","-M":"1110011","M+1":"1110111","M-1":"1110010","D+M":"1000010","D-M":"1010011"
	   ,"M-D":"1000111","D&M":"1000000","D|M":"1010101"}

dest = {"null":"000","M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"}
jump = {"null":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}



def compute_c(instruction):
	instruction = instruction.strip()
	default = "111"
	if instruction.find('=')+1:
		if instruction.find(';')+1:
			print(instruction.find(';'))
			comp_i = instruction.split('=')[1].split(';')[0]
			jump_i = instruction.split('=')[1].split(';')[1]
			dest_i = instruction.split('=')[0]
		else:
			comp_i = instruction.split('=')[1]
			jump_i = "null"
			dest_i = instruction.split('=')[0]
	elif instruction.find(';')+1:
		comp_i = instruction.split(';')[0]
		jump_i = instruction.split(';')[1]
		dest_i = "null"	
	else:
		comp_i = instruction
		jump_i = "null"
		dest_i = "null"	
	print(f"comp_i :{comp_i}")
	print(f"jump_i : {jump_i}")
	print(f"dest_i : {dest_i}")	
	comp_bin = comp.get(comp_i)
	jump_bin = jump.get(jump_i)
	dest_bin = dest.get(dest_i)
	print(comp_bin)
	print(jump_bin)
	print(dest_bin)
	return default+comp_bin+dest_bin+jump_bin

def parse(asm,filename):
	fh = open(f'{filename}.hack',"w")
	linecount = 0
	for instruction in asm:
		print(f"parsing {instruction}..")
		if instruction.startswith("/"):
			continue	
		elif instruction.startswith("@"):
			dec = instruction.split('@')[1].split('/')[0].strip()
			bin_no  = (bin(int(dec))).split('b')[1]
			bin_is = "0" * (16-len(bin_no))
			bin_is = bin_is + bin_no
		elif instruction[0].isalpha():
			bin_is = compute_c(instruction)
		else:
			continue
		print(f"entering value {bin_is}...")	
		fh.write(bin_is)
		fh.write('\n')	
	fh.close()		
		