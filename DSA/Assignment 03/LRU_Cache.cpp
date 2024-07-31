/*Implement LRU Cache with following functionalities : (2 Marks)
LRUCache(capacity) : Initialize the LRU cache with positive size capacity.
get(key) : Return the value of the key if the key exists, otherwise return -1.
put(key, value) : Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
*/

#include <iostream>
#include<list>
#include<unordered_map>
using namespace std;

class LRUCache {
private:
    int capacity;
    list<pair<int, int>> cache; // stores the key-value pairs
    unordered_map<int, list<pair<int, int>>::iterator> map; // maps keys to their positions in the list

    void moveToFront(int key, int value) {
        // Move the accessed item to the front of the list
        cache.erase(map[key]);
        cache.push_front({key, value});
        map[key] = cache.begin();
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        if (map.find(key) == map.end())
            return -1; // key does not exist
        int value = map[key]->second;
        moveToFront(key, value);
        return value;
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            moveToFront(key, value);
        } else {
            if (cache.size() == capacity) {
                // evict the least recently used item
                int lruKey = cache.back().first;
                cache.pop_back();
                map.erase(lruKey);
            }
            // insert the new item at the front of the list
            cache.push_front({key, value});
            map[key] = cache.begin();
        }
    }
};

int main() {
    LRUCache cache(2); // capacity of 2

    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1) << endl; // returns 1

    cache.put(3, 3); // evicts key 2
    cout << cache.get(2) << endl; // returns -1 (not found)

    cache.put(4, 4); // evicts key 1
    cout << cache.get(1) << endl; // returns -1 (not found)
    cout << cache.get(3) << endl; // returns 3
    cout << cache.get(4) << endl; // returns 4

    return 0;
}
