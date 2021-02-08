#include <iostream>
#include <cstdlib>


#include <string>
using namespace std;


#include <string>

using namespace std;

int getCount(const string& inputStr)
{
  int num_vowels = 0;
  string m_task = "aeiou";
  int i_length = inputStr.length()-1;
  int m_length = m_task.length()-1;

  for (int i = i_length; i >= 0; --i)
  	for (int j = 0; j <= m_length; ++j)
  	{	
  		cout << inputStr[i] << " - " << m_task[j];
  		if (inputStr[i] == m_task[j]) 
  		{
  			num_vowels++;
  		  	  		cout << "--  +  --" << endl;
  	  	}
  	  	else
  	  		cout << "--  -  --" << endl;
  	}
  return num_vowels;
}

int main()
{
	string tmp_txt = "abracadabra?"; 
	cout << getCount(tmp_txt) << endl;
	return 0;
}
