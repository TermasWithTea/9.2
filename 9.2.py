first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(x) for x in first_strings if len(x) >= 5]

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [ (x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
sort = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable', 'Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
trid_result = {x: len(x) for x in sort if len(x)%2 == 0 }

print(first_result)
print(second_result)
print(trid_result)