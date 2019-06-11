//Java excercise to find the first missing element in an array from 1 to n
//All numbers in the array must be between 1 and n, including 1 and n
//numbers do not have to be given in order

import java.util.Arrays;

class Solution {
    public int solution(int[] A) {
    
        boolean flag = false;
        int missingInt = 0;
        
        Arrays.sort(A);
        if(A.length > 0)
        {
            if(A[0] > 1)
            {
                return 1;
            }
            else if(A[0] == 2)
            {
                return 1;
            }
            else if(A[0] == 1 && A.length == 1)
            {
                return 2;
            }
            else
            {
                for(int x = 1; x < A.length; x++)
                {
                    if(A[x] > (A[x - 1] + 1))
                    {
                        missingInt = A[x] - 1;
                        flag = true;
                    }
                }
                if(flag)
                {
                    return missingInt;
                }
                else
                {
                    return (A[A.length - 1] + 1);
                }
            }
        }
        else
        {
            return 1;
        }
    }
}
