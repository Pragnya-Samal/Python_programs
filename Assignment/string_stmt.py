#String Functions
#Q1 Find the length of a string.
s=input("Enter a string: ")
print("Length of the string is:", len(s))
#Q2 Convert a string to uppercase.
print("String in uppercase:", s.upper())
#Q3 Count the number of vowels in a string.
vowels = 'aeiouAEIOU'
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)
#Q4 Reverse a string without using slicing.
reversed = ''
for char in s:
    reversed = char + reversed
print("Reversed string:", reversed)
#Q5 Check whether a string is palindrome.
if s == reversed:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#Q6 Count frequency of each character in a string.
char_freq = {}
for char in s:
    char_freq[char] = char_freq.get(char, 0) + 1
print("Character frequency in the string:", char_freq)
#Q7 Find how many words are in a sentence.
words = s.split()
print("Number of words in the string:", len(words))
#Q8 Replace all spaces with hyphens.
hyphenated_str = s.replace(' ', '-')
print("String with spaces replaced by hyphens:", hyphenated_str)
#Q9 Check whether a string contains only digits.
if s.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
#Q10 Remove all special characters from a string.
import re
cleaned_str = re.sub(r'[^A-Za-z0-9 ]+', '', s)
print("String after removing special characters:", cleaned_str)
#Q11 Find the first and last occurrence of a character.
char_to_find = input("Enter a character to find its first and last occurrence: ")
first_occurrence = s.find(char_to_find)
last_occurrence = s.rfind(char_to_find)
print(f"First occurrence of '{char_to_find}':", first_occurrence)
print(f"Last occurrence of '{char_to_find}':", last_occurrence)
#Q12 Convert a string to title case.
title_case_str = s.title()
print("String in title case:", title_case_str)
#Q13 Count uppercase and lowercase letters.
upper_count = 0
lower_count = 0
for char in s:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
#Q14 Check whether two strings are anagrams.
s2 = input("Enter another string to check for anagram: ")
if sorted(s.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
#Q15 Extract digits from a string.
digits = ''.join([char for char in s if char.isdigit()])
print("Digits extracted from the string:", digits)
#Q16 Split a string and join using
split_str = s.split()
joined_str = '-'.join(split_str)
print("String after splitting and joining with hyphens:", joined_str)
#Q17 Remove duplicate characters from a string.
seen = set()
result = ''
for char in s:
    if char not in seen:
        seen.add(char)
        result += char
print("String after removing duplicate characters:", result)
#Q18 Find the longest word in a sentence.
longest_word = max(words, key=len) if words else ''
print("The longest word in the string is:", longest_word)
#Q19 Check whether a string starts and ends with same character.
if s and s[0] == s[-1]:
    print("The string starts and ends with the same character.")
else:
    print("The string does not start and end with the same character.")
#Q20 Sort characters of a string alphabetically.
sorted_str = ''.join(sorted(s))
print("String with characters sorted alphabetically:", sorted_str)

