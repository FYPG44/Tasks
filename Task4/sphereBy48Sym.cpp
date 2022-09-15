#include <bits/stdc++.h>
using namespace std; 
#define OFFSET 15

void update(int& j, int& s, int p) {
    s = s + p*2*j + 1; 
    j = j + p; 

}

vector<vector<int>> findPermutations(vector<int>& nums) {
    vector<vector<int>> perms;
    do 
    {
        perms.push_back(nums); 
        
    } while (next_permutation(nums.begin(), nums.end())); 

    return perms; 
}

void insertToSphereSet(vector<int>& nums, unordered_set<string>& S) {
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


void include48Sym(unordered_set<string>& S, int x, int y, int z) {
    vector<int> temp{x, y, z}; 
    vector<vector<int>> perms = findPermutations(temp); 
    for (vector<int> perm : perms) {
        insertToSphereSet(perm, S); 
    }
}

unordered_set<string> SphereBy48Sym(int r1, int r2) {
    int i = 0, j = 0, k = r2, k0 = r2, R1 = r1*r1, R2 = r2*r2; 
    int s = 0, s0 = 0; 
    int v0 = R2 + k; 
    int v = v0; 
    int k1, u;
    unordered_set<string> S; 
    while (i <= k) {
        while (j <= k) {
            if (s > v) {
                update(k, s, -1); 
                v = v - 1; 

            }
            k1 = k; 
            u = R1-k; 
            while ((s > u) && (j <= k1)) {
                include48Sym(S, i, j, k1); 
                update(k1, s, -1); 
                u = u + 1; 
            }
            update(j, s, 1); 
        }
        j = i; 
        update(i, s0, 1); 
        update(j, s0, 1); 
        while ((s0 > v0) && (i <= k0)) {
            update(k0, s0, -1); 
            v0 = v0 - 1; 
        }
        k = k0; 
        v = v0; 
        s = s0; 
    }

    return S; 

} 

void writeToFile(unordered_set<string>& S) {
    ofstream Output("output.txt");
    for (string point : S) {
        Output << point << endl;
        
    }
    Output.close(); 

}


int main()
{
   
        unordered_set<string> points = SphereBy48Sym(7, 10); 
        writeToFile(points);
        

    return 0;

}