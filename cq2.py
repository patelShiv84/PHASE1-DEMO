# Write a function that takes a list of words and groups them based on the number of vowels in each word.
# The function should return a dictionary where the keys are vowel counts and the values are lists of words

list_word = ["apple","banana","kiwi","chiku"]
vowel = "aoeuiAOEUI"


dict_word1 = {}
count1 = 0
list1 = []

for word in list_word[0]:
    for i in word:

        if i in vowel:
            list1.append(i)
            count1 += 1

dict_word1 = [count1,list1]

          
# print(dict_word1)

# ------------------------------------------

ict_word2 = {}
count2 = 0
list2 = []

for word in list_word[1]:
    for i in word:

        if i in vowel:
            list2.append(i)
            count2 += 1 

dict_word2 = [count2,list2]         
        
# print(dict_word2)

# ------------------------------------------

dict_word3 = {}
count3 = 0
list3 = []

for word in list_word[2]:
    for i in word:

        if i in vowel:
            list3.append(i)
            count3 += 1 

dict_word3= {count3:list3}
        
# print(dict_word3)

# ------------------------------------------

dict_word4 = {}
count4 = 0
list4 = []

for word in list_word[3]:
    for i in word:

        if i in vowel:
            list4.append(i)
            count4 += 1 

dict_word4= {count4:list4}
        
# print(dict_word4)

# ------------------------------------------


# list22 = [dict_word1,dict_word2]
# print(list22)

dict_og  = dict(dict_word1)
print(dict_og)





"main code"

# count1 = 0
# list1 = []

# for word in list_word[0]:
#     for i in word:
#         #  print(i)

#         if i in vowel:
#             list1.append(i)
#             count1 += 1

# # print(list1)
# # print(count1)

# dict_word = {count1:list1}
# print(dict_word)
