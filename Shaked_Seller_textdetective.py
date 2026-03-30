def load_words(filename: str) -> list[str]:
    """
     Reads a file containing one word per line.
     Returns a list of words.
     """
    word_list = []
    with open(filename, "r") as words:
        for line in words:
            word_list.append(line.strip("\n"))

    return word_list

def normalize(text: str) -> str:
    """
     Returns lowercase letters only (a-z).
     Removes punctuation, spaces, digits, etc.
     """
    new_text = []
    for i in text:
        if i.isalpha():
            new_text.append(i.lower())

    return "".join(new_text)

def set_signature(text: str) -> frozenset:
    """
     Normalize the text, then return frozenset of unique letters.
     Example: "aab" -> frozenset({'a','b'})
     """
    text = normalize(text)
    return frozenset(text)

def freq_signature(text: str) -> tuple:
    """
     Normalize the text, then return a 26-length tuple of counts for a..z.
     Example: "aab" -> (2,1,0,0,...)
     """
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    text = normalize(text)
    counts = []
    for a in alphabet:
        counts.append(text.count(a))

    return tuple(counts)

"""
Incorrect anagram check
Returns true for some cases that are not actually anagrams
"""
def is_anagram_using_sets(a: str, b: str) -> bool:
    return set_signature(a) == set_signature(b)

"""
The correct anagram check
Checks letter counts
"""
def is_anagram(a: str, b: str) -> bool:
    return freq_signature(a) == freq_signature(b)

def group_anagrams(words: list[str]) -> dict[tuple, list[str]]:
    """
     Groups words by freq_signature (correct).
     key = freq_signature
     value = list of original words with that signature
     """
    anagram_groups = {}

    for w in words:
        sig = freq_signature(w)
        if sig in anagram_groups:
            anagram_groups[sig].append(w)
        else:
            anagram_groups[sig] = []
            anagram_groups[sig].append(w)

    singletons = 0
    for i in anagram_groups.values():
        if len(i) == 1:
            singletons += 1

    print("---Anagram Group Report---")
    print(f"Total words loaded: {len(words)}")
    print(f"Total anagram groups: {len(anagram_groups.keys())}")
    print(f"Singleton groups (size 1) : {singletons}")

    top_5_groups = []
    def get_len(item):
        return len(item[1])

    top_5 = sorted(anagram_groups.items(), key = get_len, reverse = True)[:5]

    print("----------------------------------------------")
    print(f"Largest anagram group:")
    print(f"\nAnagram key: {top_5[0][0]}\nGroup (size {len(top_5[0][1])}): {top_5[0][1]}")

    print("----------------------------------------------")
    print("Top 5 Anagram Groups:\n")
    for i in top_5:
        k, v = i
        print("------------------------")
        print(f"Anagram key: {k}\nGroup (size {len(v)}): {v}")

    return anagram_groups

def main():
    word_list = load_words("words.txt")
    anagram_groups = (group_anagrams(word_list))
    print("----------------------------------------------")
    print("When is checking anagrams using sets wrong?")
    print("Calling the function with parameters:")
    print('("ab", "aab")')
    print("Returns: ", is_anagram_using_sets("ab", "aab"))
    print('("mississippi", "misp")')
    print("Returns: ", is_anagram_using_sets("mississippi", "misp"))
    print('("adder", "read)')
    print("Returns: ", is_anagram_using_sets("adder", "read"))

    print("-----Reflection-----")
    print("Why is [x in my_set] average-case O(1)?")
    print("\tSets use a hashing mechanism that allows the computer to directly determine the location of an element.")
    print("Why is [x in my_list] O(n)?")
    print("\tIterating through a list requires processing a number of elements that is directly proportional to the size of the list")
    print("Building a freq signature for a word of length k is what complexity?")
    print("\tBuilding a freq signature for a word of length k would have complexity O(26), ")
    print("One sentence: why sets alone fail for anagrams?")
    print("\tSets remove duplicates, so it would think for example that 'ab' and 'aabb' are anagrams.")

main()
