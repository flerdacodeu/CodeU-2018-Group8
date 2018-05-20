def is_anagram(s1, s2, case_sensitive=True):
    if not case_sensitive:
        return sorted(s1.lower()) == sorted(s2.lower())
    return sorted(s1) == sorted(s2)
