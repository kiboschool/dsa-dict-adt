# Dictionary ADT

As a general concept, data *dictionaries* associate keys with values and provide the ability to perform lookups based on those keys. This is the idea that Python dictionaries are based on; they allow you to map keys to values:

```python
my_dict = {}
my_dict["key_1"] = 10
my_dict["key_2"] = 5
my_dict["foo"] = "bar"
```

Python dictionaries are implemented using *hash tables*, a topic that we will cover later this term.

For now, we can think about how we would implement a dictionary ADT. Your task in this exercise is to implement the dictionary ADT using Python lists.

## Dictionary ADT

Let's define a dictionary ADT has the following behavior:

* Dictionaries map keys to values
* Each key can only be associated with one value (i.e., there can't be duplicates)
* Dictionaries are unordered

An implementation should have the following methods:

* `insert(key, value)`: insert a (key, value) pair into the dictionary. If `key` already exists in the dictionary, overwrite its `value`. Returns `True` if the value already existed; `False` otherwise.
* `remove(key)`: remove the (key, value) pair from the dictionary identified by `key`, if present. Returns `True` if a key was successfully removed; `False` otherwise.
* `contains(key)`: returns `True` if the dictionary contains a mapping for `key`; otherwise, it returns False
* `lookup(key)`: if a (key, value) pair exists for the given `key`, then return the associated `value`; otherwise, return `None`
* `get_keys()`: returns a list of only the keys in the dictionary
* `get_values()`: returns a list of only the values in the dictionary
* `size()`: returns the number of (key, value) pairs in the dictionary

## Your Task

In `listdict.py`, define a class named `ListDictionary` that implements the dictionary ADT using one or more lists. Exactly how you implement the dictionary is up to you -- you should make use of at least one list, but can also make use of other Python built-in data structures, such as tuples or sets. You should *not* use Python dictionaries in your implementation.

Define each of the seven methods above as efficiently as possible. For example, you should not make any extra loops over lists than what is strictly necessary. Your implementation should also respect the expected behavior of a data dictionary as defined above.

## Test Cases

In `test_listdict.py`, add unit tests that test the functionality of your `ListDictionary`. Try to think of edge cases for each method -- in other words, cases that probe the potentially undefined behavior of your implementation. For example, does your code gracefully return silently if `remove()` is called when the dictionary is empty, or does it cause an error?

## Extra Challenge

Remove the restriction that each key can only map to one value. This would allow each key to be associated with a list of values.

Making this modification requires making changes in multiple methods. For example, `insert()` should no longer overwrite the value if a key is found in the dictionary; instead, it should add the new value to the list of values for that key. The `values()` method will need to be able to include in its results all of the values for each key.
