//This is a C++ program that will prompt a user to enter two words with the same letters, and will then swap the letters until
//the first word is the same as the second word.
//Even though there is a while statement, it only runs for the length of the word.
//Thus, the worst case scenario for this algorithm is still O(nlog(n))

#include <iostream>
#include <string>

using namespace std;

int reworkString(int x, string wordOne, string wordTwo)
{
    //errorcatching
    int arrayOne[26] = {0};
    int arrayTwo[26] = {0};
    
    for(int a = 0; a < int(wordOne.length()); a++)
    {
        arrayOne[int(wordOne[a]) - 97]++;
        arrayTwo[int(wordTwo[a]) - 97]++;
    }
    for(int a = 0; a < 26; a++)
    {
        if(arrayOne[a] != arrayTwo[a])
        {
            cout << "Words do not contain all the same letters" << endl;
            return 0;
        }
    }
    
    
    int y = x;
    
    while(wordOne[x] != wordTwo[x])
    {
        if(wordOne[y] != wordTwo[x])
        {
            y--;
        }
        else
        {
            cout << "Word 2: " << wordTwo << endl;
            cout << "Word 1: " << wordOne << endl;
            char temp = wordOne[y];
            wordOne[y] = wordOne[y+1];
            wordOne[y+1] = temp;
            cout << "Swap " << wordOne[y+1] << " with " << wordOne[y] << endl;
            cout << endl;
            y++;
        }
        
    }
          
      if(wordOne != wordTwo)
      {
        //cout << y << " ";
        reworkString(y - 1, wordOne, wordTwo);
      }
      else
      {
        cout << "Word 2: " << wordTwo << endl;
        cout << "Word 1: " << wordOne << endl;
        return 0;   
      }
    
}

int main()
{
    string word1 = "";
    string word2 = "";
    cout << "enter word one: ";
    cin >> word1;
    cout << endl << "enter word two: ";
    cin >> word2;
    cout << endl;
    
    reworkString(word1.length() - 1, word1, word2);
}
