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
#define f cin
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
    int opc = 0;
    for(unsigned long long i = 0; i <= maxi;i++){
        while(a[i] > 0){
            v.push_back(i);
            opc++;
            if(opc % 100000 == 0)
                cout<<"!";
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
    //string ffile, gfile;
    //ifstream r("file_name.in");
    //r >> ffile >> gfile;
    //string ffile = "bubble_in.in", gfile = "bubble_out.txt";
    vector <unsigned long long> v;
    //ofstream g(gfile);
    //g<<"alocat";
    //g.close();
    //ifstream f(ffile);
    //cout<<"fopen\n";
    long long seconds;
    f>>seconds;
    srand(seconds);
    long long n;
    f>>n;
    long long max_number;
    f>>max_number;
    //f.close();
    for(long long i = 1; i <= n; i++){
        if(i % 1000000 == 0)
        cout<<".";
        v.push_back(rand() % max_number);
    }
    cout<<"gen\n";
    /*for(auto i:v){
        cout<<i<<"\n";
    }*/
    //g.open(gfile);
    //g<<"err";
    //g.close();
    auto start = high_resolution_clock::now();
    count_sort(v);
    auto stop = high_resolution_clock::now();
    ofstream g("counting.txt", ios::app);
    while(!g.is_open()){
        g.open("counting.txt", ios::app);
    }
    g<<"\n"<<"N: "<<n<<"\nX: "<<max_number<<"\nREZ: ";
    if(!verif(v)){
        g<<"inf";
        //g.close();
    }
    else{
        auto duration = duration_cast <microseconds> (stop - start);
        g<<duration.count();
        //g.close();
    }
    g<<"\n";
    g.close();
    v.clear();
    return 0;
}
