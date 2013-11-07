1. How to run the file?
	Compile basic.cpp 
	run the executable with an argument that is the input filename
	Ex: ./a.out "input1.txt"

2. Format of Input file
	The first line should contain the total number of nodes in the circuit
	The subsequent lines would be in the format
	typeOfGate OutputNode InputNodes (all space separated)

3. Inputs to circuit
	As the program is running it asks the values of input nodes.

4. Gate value association
	value | GATE
	-------------
	  0   | INPUT
	  1   |  AND
	  2   |  OR
	  3   | NAND
	  4   |  NOR
	  5   |  NOT
	  6   |  XOR
	  7   | NXOR
	  -----------
