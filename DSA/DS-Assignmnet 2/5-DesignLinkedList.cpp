//https://leetcode.com/problems/design-linked-list/

#include <iostream>
using namespace std;

class node {
public:
    int val;
    node *next;
    node(int data) {
        val = data;
        next = NULL;
    }
};

class MyLinkedList {
public:
    node *head;
    MyLinkedList() {
        head = NULL;
    }

    int length() {
        int count = 0;
        node *temp = head;
        while (temp != NULL) {
            count++;
            temp = temp->next;
        }
        return count;
    }

    int get(int k) {
        int len = length();
        if (head == NULL || k >= len) return -1;
        node *temp = head;
        for (int count = 0; count < k; count++) {
            temp = temp->next;
        }
        return temp->val;
    }

    void addAtHead(int value) {
        node *new_node = new node(value);
        new_node->next = head;
        head = new_node;
    }

    void addAtTail(int value) {
        node *new_node = new node(value);
        if (head == NULL) {
            head = new_node;
        } else {
            node *temp = head;
            while (temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = new_node;
        }
    }

    void addAtIndex(int k, int value) {
        if (k == 0) {
            addAtHead(value);
            return;
        }
        node *new_node = new node(value);
        node *temp = head;
        for (int count = 0; temp != NULL && count < k - 1; count++) {
            temp = temp->next;
        }
        if (temp == NULL) return;
        new_node->next = temp->next;
        temp->next = new_node;
    }

    void deleteAtIndex(int k) {
        if (head == NULL) return;
        if (k == 0) {
            node *del = head;
            head = head->next;
            delete del;
            return;
        }
        node *temp = head;
        for (int count = 0; temp != NULL && count < k - 1; count++) {
            temp = temp->next;
        }
        if (temp == NULL || temp->next == NULL) return;
        node *del = temp->next;
        temp->next = temp->next->next;
        delete del;
    }
};

int main() {
    MyLinkedList* obj = new MyLinkedList();
    obj->addAtHead(1);
    obj->addAtTail(3);
    obj->addAtIndex(1, 2); 
    cout << "Get(1): " << obj->get(1) << endl; 
    obj->deleteAtIndex(1); 
    cout << "Get(1): " << obj->get(1) << endl; 
    delete obj;
    return 0;
}
