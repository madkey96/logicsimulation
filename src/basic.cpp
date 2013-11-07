#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
int N, i, j, k, temp, a[100] = {0}, b[100]={0};
int circuit, root; 
string input;
const char* filename;
vector<int> bfs;

/*
Each gate in the circuit is represented by a node object.
node contains the type of gate in the in gate.
node contains inputs to the gate as a vector inputs.
node contains the evaluated output in the bool value.
value | GATE
-------------
  0   | INPUT
  1   | AND
  2   | OR
  3   | NAND
  4   | NOR
  5   | NOT
  6   | XOR
  7   | NXOR
  -----------
*/

class node
{
public:
	node();
	void initialize(vector<int> v);
	vector<int> inputs;
	int gate;
	bool value;
};
node::node(){
	gate=0;
    value=0;
};
void node::initialize (vector<int> v) {
	gate = v[0];
	for (k = 2; k < v.size(); ++k)
	{
		inputs.push_back(v[k]);
	}
};


int main(int argc, char** argv)
{
	// reading input from a file
    fstream file(argv[1], ios::in);
    getline(file,input,'\n');
    istringstream (input)>>N;
    vector <node> signal;
    signal.reserve(N+1);
    vector <int> values;
    // as each line is read, a new object is created 
    while(getline(file, input, '\n')) {
    	// converting input from file to char array
    	char * temp = new char [input.length()+1];
    	strcpy (temp, input.c_str());
    	// splitting char array at spaces
    	char * current = strtok(temp, " ");
    	while(current!=NULL){
    		int k = atoi(current);
    		values.push_back(k);

    		current = strtok(NULL," ");
    		}
    signal[values[1]].initialize(values);

    values.erase(values.begin(),values.end());
    }

    // breadth first to levelize
    // finding the root node
    int isnode[100] = {0};
    for (int i = 1; i < N+1; ++i)
    {
        for (int j = 0; j < signal[i].inputs.size(); ++j)
        {
            isnode[signal[i].inputs[j]] = 1;
        }
    }

    for (int i = 1; i < N+1; ++i)
    {
        if (isnode[i]==0 && signal[i].gate!=0)
        {
            bfs.push_back(i);
        }
    }

    int count = 0;
    while(bfs.size()!=count)
    {
        for (int j = 0; j < signal[bfs[count]].inputs.size(); ++j)
        {
            for (int k = 0; k < bfs.size(); ++k)
            {
                if(bfs[k]==signal[bfs[count]].inputs[j])
                {
                    bfs.erase(bfs.begin()+k);
                }
            }
            bfs.push_back(signal[bfs[count]].inputs[j]);
        }
        count++;
    }

    // taking the input values from user and evaluating the circuit
    for (int i = 0; i < bfs.size(); ++i)
    {
        temp = bfs[bfs.size()-i-1];
        switch(signal[temp].gate)
        {
            case 0:
                cout<<"give input for node "<<temp<<endl;
                cin>>signal[temp].value;
                break;
            case 1:
                signal[temp].value = 1;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    signal[temp].value = (signal[signal[temp].inputs[j]].value && signal[temp].value);
                }
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
                break;
            case 2:
                signal[temp].value = 0;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    signal[temp].value = (signal[signal[temp].inputs[j]].value || signal[temp].value);
                }
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
            break;
            case 3:
                signal[temp].value = 1;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    signal[temp].value = (signal[signal[temp].inputs[j]].value && signal[temp].value);
                }
                signal[temp].value = !(signal[temp].value);
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
            break;
            case 4:
                signal[temp].value = 0;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    signal[temp].value = (signal[signal[temp].inputs[j]].value || signal[temp].value);
                }
                signal[temp].value = !(signal[temp].value);
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
            break;
            case 5:
                signal[temp].value = 0;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    signal[temp].value = (signal[signal[temp].inputs[j]].value || signal[temp].value);
                }
                signal[temp].value = !(signal[temp].value);
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
            break;
            case 6:
                signal[temp].value = 0;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    if(signal[temp].value)
                    {
                        signal[temp].value = !(signal[signal[temp].inputs[j]].value);
                    }
                    else
                    {
                        signal[temp].value = (signal[signal[temp].inputs[j]].value);   
                    }
                }
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
            break;
            case 7:
                signal[temp].value = 0;
                for (int j = 0; j < signal[temp].inputs.size(); ++j)
                {
                    if(signal[temp].value)
                    {
                        signal[temp].value = !(signal[signal[temp].inputs[j]].value);
                    }
                    else
                    {
                        signal[temp].value = (signal[signal[temp].inputs[j]].value);   
                    }
                }
                signal[temp].value = !(signal[temp].value);
                cout<<"computed output at "<<temp<<" is "<<signal[temp].value<<endl;
            break;
        }
    }
	return 0;
}