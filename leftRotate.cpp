//2 solutions to the same problem.
//The problem asked me to write a function that would rotate a vector left d times
//for example, rotating the vector [1,2,3,4,5] left 2 times would yeild [3,4,5,1,2]

//----------------------------------------------------------------------------------
//First solution is easy to read but could take too long to run if d is very large
//simple function to rotate a vector left d times
//----------------------------------------------------------------------------------
vector<int> rotLeft(vector<int> a, int d) {
    vector<int> b = a;
    for(int a = 0; a < d; a++)
    {
      for (int x = b.size() - 1; x > 0; x--) {
        b[0] += b[x];
        b[x] = b[0] - b[x];
        b[0] = b[0] - b[x];
      }
    }

    return b;    
}
//---------------------------------------------------------------------------------

//My second solution is much longer, but solves the problem in O(n) time
//I was able to shorten it some, but found this version much easier to follow,
//So I am putting it here as my optimal solution.
//---------------------------------------------------------------------------------
vector<int> rotLeft(vector<int> a, int d) {
    vector<int> b = a; //initialize b as a so it will have the correct size

    for(int z = 0; z < b.size(); z++)
    {
        b[z] = 0; //make all values in b 0
    }

    int location = 0;

    for(int x = b.size() - 1; x >= 0; x--)
    {
        if((x - d) < 0)
        {
            location = b.size() - (d - x);
        }
        else
        {
            location = x - d;
        }
        b[location] = a[x];
    }

    return b;
}
