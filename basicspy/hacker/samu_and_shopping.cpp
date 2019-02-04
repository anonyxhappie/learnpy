// Sample code to perform I/O:
/*

Samu is in super market and in a mood to do a lot of shopping. She needs to buy shirts, pants and shoes for herself and her family. There are N different shops. Each shop contains all these three items but at different prices. Now Samu has a strategy that she won't buy the same item from the current shop if she had already bought that item from the shop adjacent to the current shop.

Now Samu is confused, because although she want to follow her strategy strictly but at the same time she want to minimize the total money she spends on shopping. Being a good programmer, she asks for your help.

You are provided description about all N shops i.e costs of all three items in each shop. You need to help Samu find minimum money that she needs to spend such that she buys exactly one item from every shop.

Input Format: 
First line contain number of test cases T. Each test case in its first line contain N denoting the number of shops in Super Market. Then each of next N lines contains three space separated integers denoting cost of shirts, pants and shoes in that particular shop.

Output Format:
For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.

Constraints :
1 ≤ T ≤ 10 
1 ≤ N ≤ 105
Cost of each item (shirt/pant/shoe) does not exceed 104

SAMPLE INPUT 
1
3
1 50 50
50 50 50
1 50 50
SAMPLE OUTPUT 
52
Explanation
There are two ways, each one gives 52 as minimum cost. One way is buy shirt from first shop, pant from second shop and shirt from third shop or she can buy shirt from first shop, shoe from second shop and shirt from third shop.

Both ways , cost comes up to 1 + 50 + 1 = 52
*/
#include <iostream>

using namespace std;

void minOfThree(int*);
int shopping(int**, int, int);

struct Minwithindex {
    int min;
    int index;
};

Minwithindex mi;
 
 int main() {
	int num, t;
	cin >> t;										
	for (int i=0; i<t; i++){
	    cin >> num;
	    int** a = new int*[num];
	    for(int i = 0; i < num; ++i)
            a[i] = new int[3];

	    for (int j=0; j<num; j++){
	        cin >> a[j][0] >> a[j][1] >> a[j][2];
	    }
	    cout << shopping(a, num, 3) << endl;
	}
	return 0;
}

int shopping(int **a, int rows, int cols) {
    int total = 0;
    for (int i=0; i<rows; i++){
        minOfThree(a[i]);
        total += mi.min;
        if(i<rows-1) a[i+1][mi.index] = 999999;
    }
    return total;
}

void minOfThree(int *a) {
    int x = a[0], y = a[1], z = a[2];
    if (x < y){
        if (x < z) {
            mi.min = x;
            mi.index = 0;
        } else {
            mi.min = z;
            mi.index = 2;
        }
    } else {
        if (y < z) {
            mi.min = y;
            mi.index = 1;
        } else {
            mi.min = z;
            mi.index = 2;
        }
    }
    // return x < y ? (x < z ? x : z) : (y < z ? y : z);
}


// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

// Write your code here

