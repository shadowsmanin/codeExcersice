//Program to find all substrings of numbers in a string of numbers, and then find the product of those substrings.
//It also informs the user if the products are unique.
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
  string testDigit = "24593";  //change to any positive integer for testing
  bool uniqueOrNah = true;
  int counter = 0;
  
  for(string::size_type x = 0; x < testDigit.length(); x++)
  {
    counter ++;   
  }
  int size = counter * counter - (counter * (counter - 1))/2;

  string allDigs[size + 1];
  int counter1;
  counter1 = 0;
  
  for(int x = 0; x < counter; x++)
  {
      //cout << "x:" << x << " ";
       for(int y = 0; y < (counter - x); y++)
        {
               allDigs[counter1] = testDigit.substr(x, y + 1);
               counter1 += 1;
        }
  }
  int tryMe;
  int nums[counter1];
  tryMe = 0;
  for(int x = 0; x < counter1; x++)
  {
      tryMe = 1;
      for(string::size_type y = 0; y < allDigs[x].length(); y++)
      {
          tryMe = tryMe * (int(allDigs[x][y]) - 48);
      }
      nums[x] = tryMe;
  }
  
  sort(nums, nums + counter1);
  
  for(int x = 1; x < counter1 - 1; x++)
  {
     cout << nums[x] << " ";
     if(nums[x] == nums[x-1])
     {
        uniqueOrNah = false;  
     }
  }
  
  if(uniqueOrNah == true)
    {
        cout << "Unique" << endl;   
    }
    else
    {
        cout << "Not unique" << endl;   
    }
  
}
