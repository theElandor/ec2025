#include <iostream>
#include <map>
#include <utility>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
class Node{
public:
    int id;
    char c;
    Node *right = nullptr;
    Node *left = nullptr;
    Node(int id_, char c_):id(id_), c(c_){}
};
void insert_node(Node* root, int id, char c){
    if (id > root->id){
        if (root->right){
            insert_node(root->right, id, c);
        }
        else{
            root->right = new Node(id, c);
        }
    }
    else{
        if(root->left){
            insert_node(root->left, id, c);
        }
        else{
            root->left = new Node(id, c);
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
    while((x = getchar()) != EOF){
        int id;
        int l_id, r_id;
        char l_char, r_char;
        scanf("DD id=%d left=[%d,%c] right=[%d,%c]\n", &id, &l_id, &l_char, &r_id, &r_char);
        if (right_root){
            insert_node(right_root, r_id, r_char);
        }
        else{
          right_root = new Node(r_id, r_char); 
        }
        if (left_root){
            insert_node(left_root, l_id, l_char);
        }
        else{
            left_root = new Node(l_id, l_char);
        }
    }
    cout<<bfs(right_root)<<endl;
    cout<<bfs(left_root)<<endl;
    return 0;
}
