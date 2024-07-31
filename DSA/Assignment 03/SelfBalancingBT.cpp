#include <iostream>
#include <stdexcept>
using namespace std;

struct Node {
    int key;
    int height;
    int size;
    Node* left;
    Node* right;

    Node(int key) {
        this->key = key;
        height = 1;
        size = 1;
        left = nullptr;
        right = nullptr;
    }
};

int height(Node* node) {
    if (node == nullptr)
        return 0;
    return node->height;
}

int size(Node* node) {
    if (node == nullptr)
        return 0;
    return node->size;
}

Node* rightRotate(Node* y) {
    Node* x = y->left;
    Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    y->size = size(y->left) + size(y->right) + 1;
    x->size = size(x->left) + size(x->right) + 1;

    return x;
}

Node* leftRotate(Node* x) {
    Node* y = x->right;
    Node* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    x->size = size(x->left) + size(x->right) + 1;
    y->size = size(y->left) + size(y->right) + 1;

    return y;
}

int getBalance(Node* node) {
    if (node == nullptr)
        return 0;
    return height(node->left) - height(node->right);
}

Node* insert(Node* node, int key) {
    if (node == nullptr)
        return new Node(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else
        return node;

    node->height = 1 + max(height(node->left), height(node->right));
    node->size = 1 + size(node->left) + size(node->right);

    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

Node* minValueNode(Node* node) {
    Node* current = node;
    while (current->left != nullptr)
        current = current->left;
    return current;
}

Node* remove(Node* root, int key) {
    if (root == nullptr)
        return root;

    if (key < root->key)
        root->left = remove(root->left, key);
    else if (key > root->key)
        root->right = remove(root->right, key);
    else {
        if ((root->left == nullptr) || (root->right == nullptr)) {
            Node* temp = root->left ? root->left : root->right;

            if (temp == nullptr) {
                temp = root;
                root = nullptr;
            } else {
                *root = *temp;
            }
            delete temp;
        } else {
            Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = remove(root->right, temp->key);
        }
    }

    if (root == nullptr)
        return root;

    root->height = 1 + max(height(root->left), height(root->right));
    root->size = 1 + size(root->left) + size(root->right);

    int balance = getBalance(root);

    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);

    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);

    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

bool find(Node* root, int key) {
    if (root == nullptr)
        return false;

    if (root->key == key)
        return true;
    else if (root->key < key)
        return find(root->right, key);
    else
        return find(root->left, key);
}

int order_of_key(Node* root, int key) {
    if (root == nullptr)
        return 0;

    if (root->key < key)
        return 1 + size(root->left) + order_of_key(root->right, key);
    else
        return order_of_key(root->left, key);
}

Node* get_by_order(Node* root, int order) {
    if (root == nullptr)
        return nullptr;

    int leftSize = size(root->left);

    if (leftSize == order)
        return root;
    else if (leftSize > order)
        return get_by_order(root->left, order);
    else
        return get_by_order(root->right, order - leftSize - 1);
}

class AVLTree {
public:
    Node* root;

    AVLTree() {
        root = nullptr;
    }

    bool find(int key) {
        return ::find(root, key);
    }

    void insert(int key) {
        root = ::insert(root, key);
    }

    void remove(int key) {
        root = ::remove(root, key);
    }

    int order_of_key(int key) {
        return ::order_of_key(root, key);
    }

    int get_by_order(int order) {
        Node* node = ::get_by_order(root, order);
        if (node != nullptr)
            return node->key;
        throw out_of_range("Order is out of range");
    }
};

int main() {
    AVLTree tree;

    tree.insert(10);
    tree.insert(20);
    tree.insert(30);
    tree.insert(40);
    tree.insert(50);
    tree.insert(25);

    cout << "Find 20: " << tree.find(20) << endl;
    cout << "Find 60: " << tree.find(60) << endl;

    cout << "Order of key 25: " << tree.order_of_key(25) << endl;
    cout << "3rd key: " << tree.get_by_order(3) << endl;

    tree.remove(25);
    cout << "Order of key 30 after removing 25: " << tree.order_of_key(30) << endl;

    return 0;
}
