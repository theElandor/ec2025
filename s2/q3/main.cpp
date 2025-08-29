#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <numeric>
#include <utility>
#include <set>
#define BOUND 10000
using namespace std;
using ll = long long;
using pp = pair<short, short>;
using mat = vector<vector<int>>;
set<pp> POSITIONS;
vector<pp> directions = {{0,1},{0,-1},{1,0},{-1,0}};
set<pair<int, pp>> VISITED;
struct Entry{
    ll id;
    vector<ll> faces;
    ll current_face = 0;
    ll seed;
    ll pulse;
    ll track_pos =0;
};
void print(vector<int> &v){
    for(ll i = 0; i < v.size(); i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}
void print_grid(vector<vector<int>> &g){
    for(int i = 0; i < g.size(); i++){
        for(int  j = 0; j < g[0].size(); j++){
            cout<<g[i][j]<<" ";
        }
        cout<<endl;
    }
}
ll roll(Entry &d, ll roll_number){
    ll spin = d.pulse * roll_number;
    d.current_face = (d.current_face + spin)%d.faces.size();
    d.pulse = (d.pulse + spin)%d.seed;
    d.pulse = d.pulse + 1 + roll_number + d.seed;
    return d.faces[d.current_face];
}
void dfs(pp pos, mat &grid, vector<short> &sequence, int current_roll){
    // Check result
    if(current_roll == sequence.size()-2){return;}
    auto [x,y] = pos; 
    int result = sequence[current_roll];
    int M = grid.size();
    int N = grid[0].size();
    POSITIONS.insert({x,y});
    for(int i = 0; i < directions.size(); i++){
        auto [dx,dy] = directions[i];
        int nx = x+dx;
        int ny = y+dy;
        if(nx >= 0 && nx < M && ny >= 0 && ny < N){ // if in bounds
            if(sequence[current_roll+1] == grid[nx][ny]) // if seq is correct
                if(VISITED.find({current_roll+1,{nx,ny}}) == VISITED.end())
                // if havent visited this state yet
                {
                    VISITED.insert({current_roll+1, {nx,ny}});
                    dfs({nx,ny}, grid, sequence, current_roll+1);
                }
        }
    }
    if(sequence[current_roll+1] == grid[x][y])
    {
        if(VISITED.find({current_roll+1,{x,y}}) == VISITED.end())
        {
            VISITED.insert({current_roll+1, {x,y}});
            dfs({x,y}, grid, sequence, current_roll+1);
        }
    }
}
int main(int argc, char **argv){
    ifstream is(argv[1]);
    ifstream gs(argv[2]);
    if(!is || !gs){
        cout<<"No file provided"<<endl;
        return 1;
    } 
    string line;
    vector<Entry> dice;
    while(getline(is, line)){
        Entry e;
        stringstream ss(line);
        char c;
        ss>>e.id>>c;
        ss.ignore(7);
        ss>>c;
        ll val;
        while(ss>>val){
            e.faces.push_back(val);
            if(ss.peek() == ',') ss.ignore(1);
            else if (ss.peek() == ']'){ss.ignore(1); break;}
        }
        ss.ignore(6);
        ss>>e.seed;
        e.pulse = e.seed;
        dice.push_back(e);
    }
    vector<vector<int>> grid;
    while(getline(gs, line)){
        vector<int> row;
        for(char c : line){
            row.push_back(c-'0');
        }
        grid.push_back(row);
    }
    int M = grid.size();
    int N = grid[0].size();
    vector<vector<short>> sequences;
    for(auto &d:dice){
        vector<short> sequence;
        for(int cr = 1; cr < BOUND; cr++){
            sequence.push_back(roll(d, cr));
        }
        sequences.push_back(sequence);
    }
    for(int s = 0; s < sequences.size(); s++){
        VISITED.clear();
        for(int i = 0; i < M; i++){
            for(int j = 0; j<N; j++){
                if(grid[i][j] == sequences[s][0]){
                    dfs({i,j}, grid, sequences[s], 0);
                }
            }
        }
    }
    cout<<POSITIONS.size()<<endl;
    return 0;
}