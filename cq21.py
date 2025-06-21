def group_by_vowel_count(words):
    vowels = "aeiouAEIOU"
    result = {}

    for word in words:
        count = 0
        for char in word:
            if char in vowels:
                count += 1

        
        if count not in result:
            result[count] = []

      
        result[count].append(word)

    return result


words_list = ["apple", "banana", "grape", "kiwi", "mango", "pear"]
grouped_words = group_by_vowel_count(words_list)

print(grouped_words)
