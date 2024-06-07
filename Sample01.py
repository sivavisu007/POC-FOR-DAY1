import unittest

def count_vowels():
    letter = "aeiou"
    s = "hello world"
    s = s.casefold()
    count = {}.fromkeys(letter, 0)
    for char in s:
        if char in count:
            count[char] += 1
    return count

class TestCountVowels(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(count_vowels(), {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0})

if __name__ == '__main__':
    unittest.main()
