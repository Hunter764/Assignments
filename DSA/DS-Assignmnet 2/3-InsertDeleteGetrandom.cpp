#include<iostream>
#include <unordered_set>
using namespace std;

class RandomizedSet {
    unordered_set<int> s;
public:
    RandomizedSet() {
        srand(time(0)); // Seed the random number generator
    }
    
    bool insert(int val) {
        auto a = s.insert(val);
        return a.second;
    }
    
    bool remove(int val) {
        return s.erase(val) > 0;
    }
    
    int getRandom() {
        auto it = s.begin();
        advance(it, rand() % s.size());
        return *it;
    }
};

