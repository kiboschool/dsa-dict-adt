class ListDictionary:
    def __init__(self):
        self.keys = []
        self.values = []

    def insert(self, key, value):
        if key in self.keys:
            # overwrite existing value
            self.values[self.keys.index(key)] = value
            return True

        # add new key and value
        self.keys.append(key)
        self.values.append(value)
        return False

    def remove(self, key):
        if key not in self.keys:
            return False

        idx = self.keys.index(key)
        self.keys = self.keys[:idx] + self.keys[idx + 1:]
        self.values = self.values[:idx] + self.values[idx + 1:]
        return True

    def contains(self, key):
        return key in self.keys

    def lookup(self, key):
        if key in self.keys:
            return self.values[self.keys.index(key)]

        # key not in dictionary
        return None

    def get_keys(self):
        return self.keys

    def get_values(self):
        return self.values

    def size(self):
        return len(self.keys)
