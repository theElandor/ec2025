#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main(int argc, char **argv){
    ifstream is(argv[1]);
    if(!is){
        cout<<"Error opening file"<<endl;
        return 1;
    }
    int id, face, seed;
    while(true){
        if(is.peek() == EOF){break;}
        is>>id;
        cout<<id<<endl;
        is.ignore(9);
        while(is.peek() != ' '){
            is>>face;
            cout<<face<<endl;
            is.ignore(1);
        }
        is.ignore(6);
        is>>seed; 
        cout<<seed<<endl;
    }


    return 0;
}