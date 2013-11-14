The folder contains codes in 3 languages:
	Python (project.py)
	C++    (project.cpp)
	Scilab (project.sce)

Python:
	Run project.py
	It will ask for an input file name
	Give input as pyinput.txt or pyinput1.txt
	Then it will ask for the bool values of input nodes depending no the file chosen
	Give the values and it will display the simulation results
	
	While execution this also generates sciinput.txt which is the input for 
	scilab code
Scilab:
	Execute project.sce
	It takes the circuit from sciinput.txt by default
	It will ask for the bool values of input nodes
	Give the values and it will display the simulation results
C++   :
	compile project.cpp
	and the run a.out with input argument as cppinput.txt
	$ ./a.out cppinput.txt
	Then give the boolean inputs when prompted.