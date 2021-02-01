#include <iostream>
#include <cstdlib>
using namespace std;

#include <vector>

int arrayPlusArray(std::vector<int> a, std::vector<int> b)
{
  int arrSum = 0;
  
  for (int &i : a) { arrSum += i; }
  for (int &i : b) { arrSum += i; }
  
  return arrSum;
}

int main(int argc, char const *argv[])
{
	cout << arrayPlusArray({1,2,3},{4,5,6});
	return 0;
}