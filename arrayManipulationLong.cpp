//This is an interesting problem in array manipulation I found on Hackerrank
//The question is very long, so I will link the page below 
//https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
//This solution gives the "correct" answer, but it is too slow. I will come back to it and try to speed it up sometime soon!

long arrayManipulation(int n, vector<vector<int>> queries) {
    vector<long> a;
    long max = 0;
    long mySize = queries.size();

    for(long x = 0; x < n; x++)
    {
        a.push_back(0);
    }

    for(long x = 0; x < mySize; x++) 
    {
        for(long y = queries[x][0]; y <= queries[x][1]; y++)
        {
            a[y - 1] += queries[x][2];
            if(a[y - 1] > max)
            {
                max = a[y - 1];
            }
        }
    }
    
    return max;
}
