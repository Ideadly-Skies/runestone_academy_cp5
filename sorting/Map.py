class HashTable:
    def __init__(self):
        """init hash table"""
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """
        hash_function implements the simple remainder method. The collision resolution
        technique is linear probing with a "plus 1" rehash value. The put function assumes
        that there will eventually be an empty slot unless the key is already present in the
        self.slots. It computes the original hash value and if that slot is not empty, iterates
        the rehash function until an empty slot occurs. If a nonempty slot already contains the key,
        the old data value is replaced with the new data value. 
        """
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        """hash function which returns the mapping"""
        return key % size

    def rehash(self, old_hash, size):
        """rehash map"""
        return (old_hash + 1) % size

    def get(self, key):
        """
            begins by computing the initial hash value. If the value is not in the initial
            slot, rehash is used to locate the next possible location. Notice that line 14 
            guarantees that the search will terminate by checking to make sure that we have
            not returned to the initial slot. If that happens, we have exhausted all possible slots
            and the item must not be present. 
        """
        start_slot = self.hash_function(key, len(self.slots))

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    return None

    def __getitem__(self, key):
        """overload __getitem__ to allow access using [] without explicitly needing to use the getter setter"""  
        return self.get(key)
    
    def __setitem__(self, key, data):
        """overload __setitem__ to allow access using [] without explicitly needing to use the getter setter"""
        self.put(key, data)

if __name__ == "__main__":
    h = HashTable()
    h[54] = "cat" # why are we inserting it manually   
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    print(h.slots)

    # access and modify items in the hash table
    print(h[20])
    print(h[17])
    h[20] = "duck"
    print(h[20])

    print(h.data)
    print(h[99])