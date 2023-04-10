#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;

void bubblesort(vector <unsigned long long> &v){
    bool ok = 0;
    do{
        ok = 1;
        for(int i = 0; i < v.size() - 1; i++){
            if(v[i] > v[i+1]){
                swap(v[i], v[i+1]);
                ok = 0;
            }
        }

    }while(!ok);
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
    /*for(auto i:v){
        cout<<i<<"\n";
    }*/
    g.open(gfile);
    g<<"err";
    g.close();
    auto start = high_resolution_clock::now();
    bubblesort(v);
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
