//https://leetcode.com/submissions/detail/1336494109/

//Implementing Queues Using Satck
#include<iostream>
#include<queue>
#include<stack>
using namespace std;

class MyQueue {
public:
    stack<int> input;
    stack<int> output;

    MyQueue() {}

    void push(int x) {
        input.push(x);
    }

    int pop() {
        if (output.empty()) {
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        int val = output.top();
        output.pop();
        return val;
    }

    int peek() {
        if (output.empty()) {
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();
    }

    bool empty() {
        return input.empty() && output.empty();
    }
};

int main() {
    MyQueue* obj = new MyQueue();
    obj->push(1);
    obj->push(2);
    cout << "Peek: " << obj->peek() << endl; // should return 1
    cout << "Pop: " << obj->pop() << endl; // should return 1
    cout << "Empty: " << obj->empty() << endl; // should return false
    cout << "Pop: " << obj->pop() << endl; // should return 2
    cout << "Empty: " << obj->empty() << endl; // should return true
    delete obj;
    return 0;
}

// Peek: 1
// Pop: 1
// Empty: 0
// Pop: 2
// Empty: 1