#string functions.py
str1 = "Hello, World!"
str2 = "    Python Programming is incredible ."
print("Length of str2:", len(str2))
print("Uppercase str1:", str1.upper())
print("capitalize function",str1.capitalize())
print("Lowercase str2:", str2.lower())
print("Split str2 into words:", str2.split())
print("Replace 'incredible' with 'awesome' in str2:", str2.replace("incredible", "awesome"))
print("Check if 'World' is in str1:", "World" in str1)
print("Find index of 'Programming' in str2:", str2.find("Programming"))
print("Count occurrences of 'i' in str2:", str2.count("i"))
print("Strip whitespace from str2:", str2.strip())
print("startswith 'Python' in str2:", str2.startswith("Python"))
print("endswith '.' in str2:", str2.endswith("."))
print("join words with '-':", "-".join(str2.split()))
print("is alphabet:", str1.isalpha())
print("is digit:", str1.isdigit())
print("is title :", str2.istitle())
print("join str1 with space:", " ".join(str1))
roll_number = "2024"
print("Original roll number:",roll_number.isdigit())

