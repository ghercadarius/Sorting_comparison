#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;
#define f cin
void quicks(vector<unsigned long long> &v, long long st, long long dr){
    cout<<"!";
    if(st<dr){
        long long i = st - 1, j = st, piv = v[dr];
        while(j < dr){
            if(v[j] < piv){
                i++;
                swap(v[i], v[j]);
            }
            j++;
        }
        swap(v[dr], v[i+1]);
        quicks(v, st, i);
        quicks(v, i+2, dr);
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
    quicks(v, 0, n-1);
    auto stop = high_resolution_clock::now();
    ofstream g("quick.txt", ios::app);
    while(!g.is_open()){
        g.open("quick.txt", ios::app);
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
