first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
firsth_result = [len(f) for f in first_strings if len(f) > 5]
second_result = [(f, g) for f in first_strings for g in second_strings if len(f) == len(g)]
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 3}
print(firsth_result)
print(second_result)
print(third_result)