import sys

i = open(str(sys.argv[1]), 'r');
o = open('input.txt', 'w');
outstr = '';
t = i.readlines();
ngates = t[4];
# outstr = outstr + t[4][2:ngates.find(" gates")] + '\n';
m = 0;
garray = {
	"AND" : 1,
	"OR"  : 2,
	"NAND": 3,
	"NOR" : 4,
	"NOT" : 5,
	"XOR" : 6,
	"NXOR": 7
}

k = 0;
while (t[k][0].isdigit() != 1):
	k = k + 1;

for j in range(k,len(t)):
	splt = t[j].find(" = ");
	out = str(t[j][0:splt]);
	if m<int(out):
		m = int(out);
	ob = t[j].find("(");
	cb = t[j].find(")");

	gate = str(garray[str(t[j][splt+3:ob])]);
	
	ipts = t[j][ob+1:cb].split(", ");
	outstr = outstr + gate + ' ' + out;
	for s in ipts:
		outstr = outstr + ' ' + s;
		if m<int(s):
			m = int(s);
	outstr = outstr + '\n';

outstr = str(m) + '\n' + outstr;
o.write(outstr);
