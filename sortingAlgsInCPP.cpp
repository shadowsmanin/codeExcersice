 //Easy to write, easy to understand, but slow. Bubble sort may be the quickest to write,
 //but it's far from the quickest to sort things. Basically it keeps swapping elements
 //up if they are bigger than the element to the right of them until the biggest value rises
 //to the top like a "bubble", then  repeates until ever element has been sorted this way
 //average case and worst case are both O(n^2)
void bubbleSort(vector<int> unsorted)
{
    int mySize = unsorted.size();
    for (int x = 0; x < mySize; x++) 
    {
        for (int y = 0; y < mySize - 1; y++) 
        {
            if (unsorted[y] > unsorted[y + 1]) 
            {
                swap(unsorted[y], unsorted[y + 1]);
            }
        }
    }
    for(int z = 0; z < mySize; z++)
    {
        cout << unsorted[z] << " ";
    }
    cout << endl;
}

//Counting sort! This is my own slightly modified version, but it works the same.
//1. Create an array with a number of elements equal to the highest value of any element in your unsorted array
//2. Go through the unsorted array, and add one to an index for every time that index appears in the unsorted array
//3. create a new array of length equal to the unsorted array
//4. go through the "count" array from 0 to the end, and add an element equal to the current index if the
//       value at that index > 0, then subtract one at that index and repeat until it's value is 0
//My favorite sorting alg, because while it can be memory intensive, it is possible to solve in O(n) time.
void countingSort(vector<int> unsorted)
{
  int mySize = unsorted.size();
  vector<int> sorted(mySize, 0);
  int min = unsorted[0];
  int max = unsorted[0];
  
  for(int x = 0; x < mySize; x++) //this loop is just in case we don't have access to the min() or max() functions
  {
    if(unsorted[x] > max)
    {
      max = unsorted[x];
    }
    
    if(unsorted[x] < min)
    {
      min = unsorted[x];
    }
  }
  
  int range = max - min;
  vector<int> countVec(range + 1, 0);
  
  for(int x = 0; x < mySize; x++)
  {
    countVec[unsorted[x]]++;
  }
  for(int x = 0; x < range; x++)
  {
      countVec[x+1] += countVec[x];
  }
  for(int x = 0; x < mySize; x++)
  {
    sorted[countVec[unsorted[x]] - 1] = unsorted[x];
    countVec[unsorted[x]]--;
  }
  for(int x = 0; x < mySize; x++)
  {
      cout << sorted[x] << " ";
  } 
}

//Quick sort, while not actually being the quickest sort, has an average run time of O(nLogn)
//this makes its average run time very good, and since it isn't too terribly memory intensive, it
//has become the go to sort for a lot of programmers.
//Below is my take on the quickSort algorithm.
void quickSort(vector<int> &unsorted, int lower, int higher)
{
    int l = lower;
    int h = higher;
    int temp;
    int pivot = unsorted[(lower + higher)/2];
    
    while(l <= h) //pivot
    {
        
        while(unsorted[l] < pivot)
            l++;
        while(unsorted[h] > pivot)
            h--;
        if(l <= h)
        {
            int temp = unsorted[l];
            unsorted[l] = unsorted[h];
            unsorted[h] = temp;
            l++;
            h--;
        }
    };
    
    if(lower < h)
    {
        quickSort(unsorted, lower, h);
    }
    if(l < higher)
    {
        quickSort(unsorted, l, higher);
    }
}

int main()
{
   vector<int> unsArray = {1,4,0,34,19,43,2,35,11,10,8,4,6};
   
   bubbleSort(unsArray);
   countingSort(unsArray);
   quickSort(unsArray, 0, 12);
   for(int x = 0; x < unsArray.size(); x++)
   {
      cout << unsArray[x] << " ";
   }
}
