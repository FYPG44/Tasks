#include <bits/stdc++.h>
using namespace std; 
#define OFFSET 15

int r1 = 6, r2 = 10; 
int k = -r2; 
int i_10 = 0, i_20 = 0; 
int s_10 = k*k, s_20 = k*k; 
int R1 = r1*r1; 
int R2 = r2*r2; 
int i1=0, i2=0, s1=0, s2=0, j=0, j_1=0, j2=0, d=0, u = 0, v = 0, q = 0, f = 0;
unordered_set<string> S; 

void display(int x, int y, int z) {
    S.insert(to_string(x + OFFSET) + "," + to_string(y + OFFSET) + "," + to_string(z + OFFSET));
}

void update(int& a1, int& a2, int p) {
    a1 += p;
    a2 += p*2*a1 + 1; 
     

}

void update4(int& a1, int& a2, int& a3, int p) {
    a1 += p; 
    a2 += p*2*a1 + 1; 
    a3 += p*2*a1 + 1; 

}

void findXRangeLayer(){
    if (k <= 0) {
        while (s_10 < u) {
            update(i_10, s_10, 1); 
            u = R1 - max(i_10, abs(k)); 
        }
        while (s_20 < v) {
            update(i_20, s_20, 1); 
            v = R2 + max(i_20, abs(k)); 
        }
        update(i_20, s_20, -1); 
    } else {
        while ((s_10 >= u) && (i_10 >= 0)) {
            update(i_10, s_10, -1); 
            u = R1 - max(i_10, k); 
        }
        update(i_10, s_10, 1); 
        while (s_20 >= v) {
            update(i_20, s_20, -1); 
            v = R2 + max(i_20, k); 
        }

    }

    
}

void initializeLayerQuad() {
    if (q == 1) {
        i1 = i_10; 
        i2 = i_20; 
        s1 = s_10; 
        s2 = s_20;
        j = 0, j_1 = 0; 
        j2 = s_20; 
        d = s_20%2; 
    }
    else if (q == 2) {
        i1 = 0; 
        i2 = -i2; 
        s1 = s1 - 1; 
        update4(j, s1, s2, -1); 
        j_1 = 1; 
        j = s_20; 
        j2 = s_20; 
        d = 1; 
    }
    else if (q == 3) {
        i1 = -i_10; 
        i2 = -i_20; 
        s1 = s_10; 
        s2 = s_20; 
        j_1 = -s_20; 
        j = 0; j2 = 0; 
        d = s_20%2; 
    }
    else if (q == 4) {
        i1 = 0; 
        i2 = -i2; 
        s1 = s1 - 1; 
        update4(j, s1, s2, 1); 
        j = -s_20; 
        j_1 = -s_20; 
        j2 = -1; 
        d = 1; 
    }
}

void findXRangeRun() {
    int maxjk = max(abs(j), abs(k)); 
    if (q == 1) {
        while ((s1 >= u) && (i1 > 0)) {
            update(i1, s1, -1); u = R1 - max(i1, maxjk); 
        }
        update(i1, s1, 1); 
        while (s2 >= v) {
            update(i2, s2, -1); v = R2 + max(i2, maxjk); 
        }
    } else if (q == 2) {
        while (s1 < u) {
            update(i1, s1, -1); u = R1 - max(abs(i1), maxjk); 
        }
        while (s2 < v) {
            update(i2, s2, -1); v = R2 + max(abs(i2), maxjk); 
        }
        update(i2, s2, 1); 
    } else if (q == 3) {
        while ((s1 >= u) && (i1 < 0)) {
            update(i1, s1, 1); u = R1 - max(abs(i1), maxjk); 
        }
        update(i1, s1, -1); 
        while (s2 > v) {
            update(i2, s2, 1); v = R2 + max(abs(i2), maxjk); 
        }
    } else if (q == 4) {
        while (s1 < u) {
            update(i1, s1, 1); u = R1 - max(i1, maxjk); 
        }
        while (s2 < v) {
            update(i2, s2, 1); v = R2 + max(i2, maxjk); 
        }
        update(i2, s2, -1); 
    }
}

void printRun(int start, int end, int j, int k) {
    for (int i = start; i <= end; i++) {
        display(i, j, k); 
    }
}


void layerTheSphere() {
    cout << "LTS: started" << endl; 
    while (k <= r2) {
        u = R1 - max(i_10, abs(k)); 
        v = R2 + max(i_20, abs(k)); 
        findXRangeLayer(); 
        if (i_10 == 0) display(0, 0, k); 
        for (q = 1; q <= 4; q++) {
            f = abs(2*q-5)-2; 
            initializeLayerQuad(); 
            while ((j_1 <= j) && (j <= j2)) {
                u = R1 - max(max(abs(i1), abs(j)), abs(k)); 
                v = R2 + max(max(abs(i2), abs(j)), abs(k)); 
                findXRangeRun(); 
                if (d == 1) printRun(i1, i2, j, k); 
                else printRun(i2, i1, j, k); 
                d = (d + 1)%2; 
                update4(j, s1, s2, f); 
                cout << "IWL ended" << endl; 
            } 
        }
        update4(k, s_10, s_20, 1);
        cout << "OWL ended" << endl;
    } 
    cout << "ended call" << endl;
}

void writeToFile() {
    ofstream Output("output_layer.txt");
    for (string point : S) {
        Output << point << endl;
        
    }
    Output.close(); 

}


int main()
{
        cout << "Started" << endl; 
        layerTheSphere(); 
        writeToFile();
        cout << "Done";
        

    return 0;

}