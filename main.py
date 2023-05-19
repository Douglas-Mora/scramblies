def scramble(s1, s2):
    dict1 = {}
    for char1 in s1:
        if char1 not in dict1:
            dict1[char1] = s1.count(char1)
    dict2 = {}
    for char2 in s2:
        if char2 not in dict2:
            dict2[char2] = s2.count(char2)
    for key,value in dict2.items():
        if key not in dict1:
            return False
        if dict2[key] > dict1[key]:
            return False
    return True

         
print(scramble('cedewaraaossoqqyt', 'codewars'))

# print("theseee".count("t"))

