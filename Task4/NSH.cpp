#include <bits/stdc++.h>
using namespace std; 
#define OFFSET 15
int r = 10; 
unordered_set<string> S; 

vector<vector<int>> findPermutations(vector<int>& nums) {
    vector<vector<int>> perms;
    do 
    {
        perms.push_back(nums); 
        
    } while (next_permutation(nums.begin(), nums.end())); 

    return perms; 
}

void insertToSphereSet(vector<int>& nums) {
    int x = nums[0], y = nums[1], z = nums[2]; 
    S.insert(to_string(x + OFFSET) + "," + to_string(y + OFFSET) + "," + to_string(z + OFFSET)); 
    S.insert(to_string(-x + OFFSET) + "," + to_string(y + OFFSET) + "," + to_string(z + OFFSET)); 
    S.insert(to_string(-x + OFFSET) + "," + to_string(-y + OFFSET) + "," + to_string(z + OFFSET)); 
    S.insert(to_string(-x + OFFSET) + "," + to_string(y + OFFSET) + "," + to_string(-z + OFFSET)); 
    S.insert(to_string(-x + OFFSET) + "," + to_string(-y + OFFSET) + "," + to_string(-z + OFFSET)); 
    S.insert(to_string(x + OFFSET) + "," + to_string(-y + OFFSET) + "," + to_string(z + OFFSET)); 
    S.insert(to_string(x + OFFSET) + "," + to_string(-y + OFFSET) + "," + to_string(-z + OFFSET)); 
    S.insert(to_string(-x + OFFSET) + "," + to_string(-y + OFFSET) + "," + to_string(z + OFFSET)); 
    S.insert(to_string(x + OFFSET) + "," + to_string(y + OFFSET) + "," + to_string(-z + OFFSET)); 

} 



void include48Sym(int x, int y, int z) {
    vector<int> temp{x, y, z}; 
    vector<vector<int>> perms = findPermutations(temp); 
    for (vector<int> perm : perms) {
        insertToSphereSet(perm); 
    }
}

void NSH(){
    int i = 0, j = 0; 
    int k = r, k0 = r; 
    int s = 0, s0 = 0; 
    int v = r-1, v0 = r-1; 
    int l = 2*v0, l0 = 2*v0; 
    int h = r*r; 
    while (3*s < h) {
        
        while (i <= j) {
            //Snippet1
            include48Sym(i, j, k); 
            s = s + 2*i + 1; 
            i = i + 1; 

            //Snippet2
            if (s > v) {
                k = k-1; 
                v = v + 1; 
                l = l - 2; 
            }

        }
        //Snippet 3
        s0 = s0 + 2*j + 1; 
        j = j + 1; 
        if (s0 > v0) {
            k0 = k0 - 1; 
            v0 = v0 + l0; 
            l0 = l0 - 2; 
        }
        i = 0; k = k0; v = v0; l = l0; s = s0; 
    }

    while (j <= k) {
        while (j < k) {
            //Snippet1
            include48Sym(i, j, k); 
            s = s + 2*i + 1; 
            i = i + 1; 

            //Snippet2
            if (s > v) {
                k = k-1; 
                v = v + 1; 
                l = l - 2; 
            }

        }
        while ((j == k) && (s < v)) {
            //Snippet1
            include48Sym(i, j, k); 
            s = s + 2*i + 1; 
            i = i + 1; 
        }
        //Snippet 3
        s0 = s0 + 2*j + 1; 
        j = j + 1; 
        if (s0 > v0) {
            k0 = k0 - 1; 
            v0 = v0 + l0; 
            l0 = l0 - 2; 
        }
        i = 0; k = k0; v = v0; l = l0; s = s0; 

    }
}


void writeToFile() {
    ofstream Output("output_nsh.txt");
    for (string point : S) {
        Output << point << endl;
        
    }
    Output.close(); 

}


int main()
{
        cout << "Started" << endl; 
        NSH(); 
        writeToFile();
        cout << "Done";
        

    return 0;

}