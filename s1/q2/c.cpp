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
    Node* parent = nullptr;
    Node(int id_, char c_):id(id_), c(c_){}
};
void insert_node(Node* root, int id, char c, map<int, vector<Node*>> &m, int lineid){
    if (id > root->id){
        if (root->right){
            insert_node(root->right, id, c, m, lineid);
        }
        else{
            root->right = new Node(id, c);
            root->right->parent = root;
            m[lineid].push_back(root->right);
        }
    }
    else{
        if(root->left){
            insert_node(root->left, id, c, m, lineid);
        }
        else{
            root->left = new Node(id, c);
            root->left->parent = root;
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
    Node* right_root = new Node(-1, 'e');
    Node* left_root = new Node(-1, 'e');
    map<int, vector<Node*>> m;
    int id;
    while((x = getchar()) != EOF){
        int l_id, r_id;
        char l_char, r_char;
        if (x == 'A'){
            scanf("DD id=%d left=[%d,%c] right=[%d,%c]\n", &id, &l_id, &l_char, &r_id, &r_char);
            m[id] = vector<Node*>();
            insert_node(right_root, r_id, r_char, m, id);
            insert_node(left_root, l_id, l_char, m, id);
        }
        else{
            // parse SWAP
            scanf("WAP %d\n", &id);
            Node* p1 = m[id][0]->parent;
            Node *p2 = m[id][1]->parent;
            cout<<p1<<" "<<p2<<endl;
            cout<<"Swapping"<<endl;
            if (p1->right == m[id][0]){
                if(p2->right == m[id][1]){
                    swap(p1->right, p2->right);
                }
                else{
                    swap(p1->right, p2->left);
                }
            }
            else{
                if(p2->right == m[id][1]){
                     swap(p1->left, p2->right);
                }
                else{
                    swap(p1->left, p2->left);
                }               
            }
            swap(m[id][0]->parent, m[id][1]->parent);
        }
    }
    cout<<bfs(right_root)<<endl;
    cout<<bfs(left_root)<<endl;
    return 0;
}
