#include <iostream>
#include <list>
#include <vector>
using namespace std;

const int CHAIN_TABLE_SIZE = 100;

class HashMapSeparateChaining {
private:
    vector<list<pair<int, int>>> table;

    int hash(int key) {
        return key % CHAIN_TABLE_SIZE;
    }

public:
    HashMapSeparateChaining() {
        table.resize(CHAIN_TABLE_SIZE);
    }

    bool find(int key) {
        int index = hash(key);
        for (auto& it : table[index]) {
            if (it.first == key)
                return true;
        }
        return false;
    }

    void insert(int key, int value) {
        int index = hash(key);
        for (auto& it : table[index]) {
            if (it.first == key) {
                it.second = value;
                return;
            }
        }
        table[index].emplace_back(key, value);
    }

    void remove(int key) {
        int index = hash(key);
        table[index].remove_if([key](const pair<int, int>& p) { return p.first == key; });
    }
};

int main() {
    HashMapSeparateChaining map;

    map.insert(1, 10);
    map.insert(2, 20);
    map.insert(3, 30);

    cout << "Find 2: " << map.find(2) << endl;
    cout << "Find 4: " << map.find(4) << endl;

    map.remove(2);

    cout << "Find 2 after removal: " << map.find(2) << endl;

    return 0;
}
