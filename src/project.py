import sys

def inputconv(ifile):
	### Opening file and reading lines ###
	ifile = open(str(ifile), 'r')
	lines = ifile.readlines()

	### Gates get converted to integers ###
	gateDict = {
	"AND" : 1,
	"OR"  : 2,
	"NAND": 3,
	"NOR" : 4,
	"NOT" : 5,
	"XOR" : 6,
	"NXOR": 7
	}

	### Parsing the file ###
	m = 0
	outstr = ''
	k = 0
	while (lines[k][0].isdigit() != 1):
		k = k + 1
	
	for i in range(0, k):
		if lines[i][0:2] == 'IN':
			outstr = outstr + lines[i][lines[i].find('(')+1: lines[i].find(')')] + ' '

	outstr = outstr + '\n'
	
	for i in range(0, k):
		if lines[i][0:2] == 'OU':
			outstr = outstr + lines[i][lines[i].find('(')+1: lines[i].find(')')] + ' '
	
	outstr = outstr + '\n'
	
	for j in range(k,len(lines)):
		splt = lines[j].find(" = ");
		out = str(lines[j][0:splt]);
		if m<int(out):
			m = int(out);
		ob = lines[j].find("(");
		cb = lines[j].find(")");

		gate = str(gateDict[str(lines[j][splt+3:ob])]);
		
		ipts = lines[j][ob+1:cb].split(", ");
		outstr = outstr + gate + ' ' + out;
		for s in ipts:
			outstr = outstr + ' ' + s;
			if m<int(s):
				m = int(s);
		outstr = outstr + '\n';

	outstr = str(m) + '\n' + outstr;
	ofile = open('output.txt', 'w')
	ofile.write(outstr)
	ifile.close()
	ofile.close()

def main():
	### Defining a class for building Node object ###
	class Node:
		"""docstring for Node"""
		def __init__(self):
			self.gate = "N"
			self.value = 0
			self.inputs = []

	### Asking for the circuit input file ###
	print 'Give the name of input file'
	ifile = raw_input()
	inputconv(ifile)

	rfile = open('output.txt', 'r')
	lines = rfile.readlines()

	nwires = int(lines[0].replace('\n',''))
	circuit = []
	for i in range(0,nwires+1):
		circuit.append(Node())
	inarrays = lines[1].replace('\n', '').split(' ')
	inarrays.remove('')
	inarrayi = []
	for x in inarrays:
		inarrayi.append(int(x))
	for i in inarrayi:
		circuit[i].gate = 0

	oarrays = lines[2].replace('\n', '').split(' ')
	oarrays.remove('')
	oarrayi = []
	for x in oarrays:
		oarrayi.append(int(x))
	lines.pop(0)
	lines.pop(0)	
	lines.pop(0)

	for line in lines:
		xs = line.replace('\n','').split(' ')
		xi = []
		for x in xs: 
			xi.append(int(x))
		circuit[xi[1]].gate = xi[0];
		circuit[xi[1]].inputs = xi[2:]

	### Breadth first search ###
	bfs = oarrayi
	count = 0
	while len(bfs)!=count:
		temp = bfs[count]
		for i in circuit[temp].inputs:
			if bfs.count(i) != 0:
				bfs.remove(i)
			bfs.append(i)
		count = count + 1	
	bfs.reverse()
	
	while 1:
		for n in bfs:
			if circuit[n].gate == 0:
				print 'Give input for node', n
				circuit[n].value = input()
			elif circuit[n].gate == 1:
				circuit[n].value = 1
				for b in circuit[n].inputs:
					circuit[n].value = circuit[n].value & circuit[b].value
			elif circuit[n].gate == 2:
				circuit[n].value = 0
				for b in circuit[n].inputs:
					circuit[n].value = circuit[n].value | circuit[b].value
			elif circuit[n].gate == 3:
				circuit[n].value = 1
				for b in circuit[n].inputs:
					circuit[n].value = circuit[n].value & circuit[b].value
				circuit[n].value = 1-circuit[n].value
			elif circuit[n].gate == 4:
				circuit[n].value = 0
				for b in circuit[n].inputs:
					circuit[n].value = circuit[n].value | circuit[b].value
				circuit[n].value = 1-circuit[n].value
			elif circuit[n].gate == 5:
				for b in circuit[n].inputs:
					circuit[n].value = 1-circuit[b].value
			elif circuit[n].gate == 6:
				circuit[n].value = 0
				for b in circuit[n].inputs:
					if circuit[n].value==1:
						circuit[n].value = 1-circuit[b].value
					else:
						circuit[n].value = circuit[b].value
			elif circuit[n].gate == 7:
				circuit[n].value = 0
				for b in circuit[n].inputs:
					if circuit[n].value==1:
						circuit[n].value = 1-circuit[b].value
					else:
						circuit[n].value = circuit[b].value
				circuit[n].value = 1- circuit[n].value

			print 'Computed output at node', n, '=', circuit[n].value
		print ''
		print '#################################################'
		print '############## Next Round of inputs #############'
		print '#################################################'

if __name__ == '__main__':
	main()


