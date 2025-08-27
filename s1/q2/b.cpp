#include <iostream>
#include <map>
#include <utility>
#include <queue>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
class Node{
public:
    int id;
    char c;
    Node *right = nullptr;
    Node *left = nullptr;
    Node(int id_, char c_):id(id_), c(c_){}
};
void insert_node(Node* root, int id, char c, map<int, vector<Node*>> &m, int lineid){
    if (id > root->id){
        if (root->right){
            insert_node(root->right, id, c, m, lineid);
        }
        else{
            root->right = new Node(id, c);
            m[lineid].push_back(root->right);
        }
    }
    else{
        if(root->left){
            insert_node(root->left, id, c, m, lineid);
        }
        else{
            root->left = new Node(id, c);
            m[lineid].push_back(root->left);
        }
    }
}
string bfs(Node* root){
    queue<Node*> q;
    int prev = 1;
    int next = 0;
    int max_next = 0;
    string current_s = "";
    string best = "";
    q.push(root);
    while(q.size() != 0){
        Node* current = q.front();
        q.pop();
        prev--;
        if(current->left){q.push(current->left);next++;current_s += current->left->c;}
        if(current->right){q.push(current->right);next++;current_s += current->right->c;}
        if(prev == 0){
            prev = next;
            if(next > max_next){
                best = current_s;
                max_next = next;
            }
            next = 0;
            current_s = "";
        }
    }
    return best;
}
int main(int argc, char **argv){
    char x;
    Node* right_root = nullptr;
    Node* left_root = nullptr;
    map<int, vector<Node*>> m;
    int id;
    while((x = getchar()) != EOF){
        int l_id, r_id;
        char l_char, r_char;
        if (x == 'A'){
            scanf("DD id=%d left=[%d,%c] right=[%d,%c]\n", &id, &l_id, &l_char, &r_id, &r_char);
            m[id] = vector<Node*>();
            if (right_root){
                insert_node(right_root, r_id, r_char, m, id);
            }
            else{
              right_root = new Node(r_id, r_char); 
              m[id].push_back(right_root);
            }
            if (left_root){
                insert_node(left_root, l_id, l_char, m, id);
            }
            else{
                left_root = new Node(l_id, l_char);
                m[id].push_back(left_root);
            }
        }
        else{
            // parse SWAP
            scanf("WAP %d\n", &id);
            swap(m[id][0]->c, m[id][1]->c);
            swap(m[id][0]->id, m[id][1]->id);
        }
    }
    cout<<bfs(right_root)<<endl;
    cout<<bfs(left_root)<<endl;
    return 0;
}
