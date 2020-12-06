numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Yunus"
new_list = [letter for letter in name]
print(new_list)

mylist = [i * 2 for i in range(1, 5)]
print(mylist)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

# exercise 2
result = [n for n in numbers if n % 2 == 0]
print(result)



### Dictionary comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student:random.randint(1,100) for student in names}
print(students_score)

passed_students = {student:score for (student,score) in students_score.items() if score>=60}
print(passed_students)


#Dictionary comprehension example-1
sentence = "What is the Airspeed Velocity of an Unloaden Swallow?"
results={word:len(word) for word in sentence.split()}
print(results)



########## NATO alphabet ##########

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
output_list=[phonetic_dict[letter] for letter in word]
print(output_list)

