import unittest

# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def normalize(s: str) -> str:
    s = s.replace(" ", "")
    return s.lower()

def is_literal(s: str) -> bool: 
    s = normalize(s)
    for i in s: 
        if i not in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True

def is_unique_hashmap(s: str) -> bool:
    d = dict()
    s = normalize(s)
    for i in s:
        if i in d: 
            return False
        d[i] = 1
    return True

def is_unique_set(s: str) -> bool: 
    s = normalize(s)
    return len(s) == len(set(s))

def is_unique_alphabet(s: str) -> bool: 
    s = normalize(s)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i in alphabet: 
            alphabet.replace(i, "")
        else: 
            return False
    return True

class Test(unittest.TestCase):
    test_cases = [
            ("abcd", True, "abcd", True),
            ("s4fad", True, "s4fad", False),
            ("", True, "", True),
            ("23ds2", False, "23ds2", False),
            ("hb 627jh=j", False, "hb627jh=j", False),
            ("ABCD", True, "abcd", True),
            ("AB CD", True, "abcd", True),
            (" A B C d", True, "abcd", True)
    ]

    def test_normalize(self): 
        for text, expected, normalized, literal in self.test_cases: 
            assert (normalize(text) == normalized)

    def test_is_unique_hashmap(self):
        for text, expected, normalized, literal in self.test_cases: 
            assert (is_unique_hashmap(text) == expected)

    def test_is_unique_set(self):
        for text, expected, normalized, literal in self.test_cases: 
            assert(is_unique_set(text) == expected)

    def test_is_literal(self):
        for text, expected, normalized, literal in self.test_cases:
            assert(is_literal(text) == literal)
            
    def test_is_unique_alphabet(self):
        for text, expected, normalized, literal in self.test_cases: 
            assert(is_unique_alphabet(text) == literal)


if __name__ == "__main__": 
    unittest.main()
    

