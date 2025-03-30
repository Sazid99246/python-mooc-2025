def anagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2


if __name__ == "__main__":
    print(anagrams("tame", "meta"))  # True
    print(anagrams("tame", "mate"))  # True
    print(anagrams("tame", "team"))  # True
    print(anagrams("tabby", "batty"))  # False
    print(anagrams("python", "java"))  # False
