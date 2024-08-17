first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(y, c) for y in first_strings for c in second_strings if len(y) == len(c)]

all_strings = first_strings + second_strings
third_result = {w: len(w) for w in all_strings if len(w) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
