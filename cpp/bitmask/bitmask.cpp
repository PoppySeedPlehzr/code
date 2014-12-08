// A program built for testing bitmasks.  This program
// is the basis for my compilers hash map, as I needed
// to bitmask the values of the strings so that case 
// would no longer matter.

// All that this program does is to convert a given
// string into it's decimal representation.  Case insensitive.

#include <iostream>
#include <string>
#include <stdlib.h>


using std::string;
using std::cout;
using std::endl;
using std::cin;


int symHash(string id){
	int val = 0;
	int size = id.size();
	
	for(unsigned t = 0; t < id.size(); t++){
		val += static_cast<int>(id[t] & 0x5F);
	}
	return val;
}


int main(){
	string s;

	cout << "Enter a string: ";
	while(cin >> s){
		cout << endl;
		cout << "Hash function returned: " << symHash(s) << endl;
		cout << "Enter a string: ";
	}
	return 0;
}


