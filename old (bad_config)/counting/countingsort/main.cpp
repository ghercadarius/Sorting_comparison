#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
#include <map>
#include <bitset>
using namespace std;
using namespace std::chrono;

void count_sort(vector <unsigned long long> &v){
    unsigned long long maxi = 0;
    for(auto i:v){
        if(i > maxi)
            maxi = i;
    }
    vector<unsigned long long> a;
    a.reserve(maxi+1);
    for(int i = 0;i <= maxi; i++)
        a[i] = 0;
    int cap = v.size();
    for(auto i:v){
        a[i]++;
    }
    v.clear();
    for(unsigned long long i = 0; i <= maxi;i++){
        while(a[i] > 0){
            v.push_back(i);
            a[i]--;
        }
    }
}


bool verif(vector <unsigned long long> v){
    unsigned long long i = 1;
    while(i < v.size() && v[i-1] <= v[i]){
        i++;
    }
    if(i == v.size())
        return true;
    return false;
}

int main()
{
    string ffile, gfile;
    ifstream r("file_name.in");
    r >> ffile >> gfile;
    vector <unsigned long long> v;
    ofstream g(gfile);
    g<<"alocat";
    g.close();
    ifstream f(ffile);
    long long seconds;
    f>>seconds;
    srand(seconds);
    long long n;
    f>>n;
    long long max_number;
    f>>max_number;
    f.close();
    for(long long i = 1; i <= n; i++){
        v.push_back(rand() % max_number);
    }
    g.open(gfile);
    g<<"err";
    g.close();
    auto start = high_resolution_clock::now();
    count_sort(v);
    auto stop = high_resolution_clock::now();
    g.open(gfile);
    if(!verif(v)){
        g<<"inf";
        g.close();
    }
    else{
        auto duration = duration_cast <microseconds> (stop - start);
        g<<duration.count();
        g.close();
    }
    v.clear();
    return 0;
}
