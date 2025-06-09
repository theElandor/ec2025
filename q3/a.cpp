#include <iostream>
#include <vector>
using namespace std;
class Snail{
public:
    int x;
    int y;
    int ring;
    Snail(int x_, int y_) : x(x_), y(y_){
        ring = (x+y)-1;
    }
    void move(int step){
        for(int i = 0; i < step; i++){
            x--;
            y++;
            if(x == 0){
                y = 1;
                x = ring;
            }
        }
    }
};
int main(int argc, char **argv){
    char c;
    int days = stoi(argv[1]);
    if(argc != 2){
        cout<<"Provide number of days"<<endl;
        return 1;
    }
    vector<Snail> v;
    while((c = getchar()) != EOF){
        int x, y;
        scanf("=%d y=%d\n", &y, &x); 
        v.emplace_back(x,y);
    }
    int total =0;
    for(int i = 0; i < v.size(); i++){
        v[i].move(days);
        total += (v[i].y + 100*v[i].x);
        cout<<v[i].x<<" "<<v[i].y<<endl;
    }
    cout<<total<<endl;
    return 0;
}
