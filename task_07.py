def combine_anagrams(words_array):
    groups = {}

    for word in words_array:
        key = ''.join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())








#Тестирование
#combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
#=> [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"]

words = ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
result = combine_anagrams(words)
print(result)