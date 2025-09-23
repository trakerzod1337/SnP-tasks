def count_words(string):
    for char in "',-.!?:;><":
        string = string.replace(char, ' ')

    string = string.split()

    counter = {}
    for word in string:
        word = word.lower()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter



#Тестирование
print(count_words("A man, a plan, a canal -- Panama"))
# {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}

print(count_words("Doo bee doo bee doo"))
# {'doo': 3, 'bee': 2}
print(count_words("ехал Грека через реку. - ? в реке рука Грека ехал через-через"))