#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
class Snail{
public:
    int x_orig;
    int y_orig;
    int x;
    int y;
    int ring;
    Snail(int x_, int y_) : x(x_), y(y_),x_orig(x_), y_orig(y_){
        ring = (x+y)-1;
    }
    void move(int step){
        x = ((x - step - 1) % ring + ring) % ring + 1;
    }
    void restore(){
        x = x_orig;
        y = y_orig;
    }
};

long long modInverse(long long A, long long M)
{
    for (int X = 1; X < M; X++)
        if (((A % M) * (X % M)) % M == 1)
            return X;
    return -1;
    
}

vector<int> find_loops (vector<Snail> &v){
    vector<int> ans;
    for(int i = 0; i < v.size(); i++){
        int days = 0;
        while(true){
            v[i].move(1);
            days++;
            if(v[i].x == v[i].x_orig){
                ans.push_back(days); 
                break;
            }
        }
    }
    return ans;
}

long long reminder(vector<int> &loops, vector<int> &a){
    long long M = 1;
    int N = loops.size();
    for(int i = 0; i < N; i++){
        M = M * (loops[i]);
    }
    vector<long long> ms;
    for(int i = 0; i < N; i++){
        ms.push_back(M/loops[i]);
    }
    vector<long long> y;
    for(int i = 0; i <N;i++){
        cout<<ms[i]<<" "<<a[i]<<endl;
        long long val = modInverse(ms[i], loops[i]);
        y.push_back(val);
    }
    long long ans = 0;
    for(int i = 0; i < N; i++){
        ans += (ms[i] * y[i]*a[i]);
    }
    return ans%M;
}

int main(int argc, char **argv){
    char c;
    vector<Snail> v;
    while((c = getchar()) != EOF){
        int x, y;
        scanf("=%d y=%d\n", &y, &x); 
        v.emplace_back(x,y);
    }
    vector<int> loops = find_loops(v);
    vector<int> a;
    for(int i = 0; i < loops.size(); i++){
        a.push_back(v[i].x_orig-1);
    }
    cout<<reminder(loops, a)<<endl; 
    return 0;
}
