import unittest

# Given two strings, write a method to decide if one is a permutation of the
# other.

def normalize(s: str) -> str:
    return s.lower()

def is_perm_1(s1: str, s2: str) -> bool:
    s1 = normalize(s1)
    s2 = normalize(s2)
    if len(s1) != len(s2):
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    return True

def is_perm_hashtable(s1: str, s2: str) -> bool: 
    s1 = normalize(s1)
    s2 = normalize(s2)
    if len(s1) != len(s2):
        return False
    d = dict()
    for i in s1: 
        d[i] = 1
    for i in s2: 
        if i in d: 
            d[i] = 0
        else: 
            d[i] = 1

    print(d)

    for i in d: 
        if d[i] != 0:
            return False
    return True

class Test(unittest.TestCase):
    test_cases = [
        ("abc", "bca", True),
        ("abc", "cba", True),
        ("abc", "acb", True),
        ("abc", "bac", True),
        ("abc", "cab", True),
        ("abc", "abc", True),
        ("abc", "", False),
        ("abc", "ab", False),
        ("abc", "abd", False)
    ]

    def test_is_perm_1(self):
        for s1, s2, expected in self.test_cases: 
            assert (is_perm_1(s1, s2) == expected)

    def test_is_perm_hashtable(self):
        for s1, s2, expected in self.test_cases:
            is_perm_hashtable(s1, s2)

if __name__ == "__main__": 
    unittest.main()
