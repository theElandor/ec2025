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
    long long days = stoll(argv[1]);
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
    for(int t=0; t < days; t++){
        for(int i = 0; i < v.size(); i++){
            v[i].move(1);
        }
        bool valid = true;
        for(int i = 0; i < v.size(); i++){
            if (v[i].x != 1){
                valid = false;
                break;
            }
        }
        if (valid){
            cout<<t+1<<endl;
            break;
        }
    }
    cout<<"ended days"<<endl;
    return 0;
}
