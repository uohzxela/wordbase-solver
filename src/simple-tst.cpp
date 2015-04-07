#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <sstream>
#define MAX 50

using namespace std;

struct Node
{
    char data;
    unsigned isEndOfString: 1;
    Node *left, *eq, *right;
};

Node* newNode(char data) 
{
    Node* temp = new Node();
    temp->data = data;
    temp->isEndOfString = 0;
    temp->left = temp->eq = temp->right = NULL;
    return temp;
}

void insert(Node** root, const char *word) {
    if(!(*root))
        *root = newNode(*word);
    if((*word) < (*root)->data)
        insert(&((*root)->left), word);
    else if ((*word) > (*root)->data)
        insert(&((*root)->right), word);
    else {
        if(*(word+1))
            insert(&((*root)->eq), word+1);
        else
            (*root)->isEndOfString=1;
    }
}

int search(Node *root, const char *word) {
    if(!root)
        return 0;
    if (*word < (root)->data)
        return search(root->left, word);
    else if(*word > (root)->data)
        return search(root->right, word);
    else {
        if(*(word+1) == '\0')
            return root->isEndOfString;
        return search(root->eq, word+1);
    }
}

int main() {
    Node *root = NULL;
    string s;
    ifstream infile("Word-List.txt");
    string word;
    while(getline(infile, word)) {
        istringstream iss(word);
        iss >> word;
        insert(&root, word.c_str());
    }
    cout << "Enter string to search: ";
    cin >> s;
    if(search(root, s.c_str()))
        cout << s << " found in TST\n";
    else
        cout << s << " not found in TST\n";
    return 0;
}
