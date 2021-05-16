#include <iostream>
#include <cstdlib>


#include <string>
using namespace std;


int getCount(const string& inputStr){
  int num_vowels = 0;
  cout << inputStr << endl;

  //your code here
  return num_vowels;
}


int main()
{
	string tmp_txt = "My first attempt!"; 
	getCount(tmp_txt);
	return 0;
}
