def count_char_frequencies(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = "data structures and algorithms"
print(count_char_frequencies(s))