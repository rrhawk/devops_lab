base = []
n = int(input())
names = {}
marks_float = []
while n > 0:
    input_string = input()
    name = input_string.split(" ")[0]
    marks = input_string.split(" ")[1:]
    for mark in marks:
        marks_float.append(float(mark))
    names[name] = marks_float
    n -= 1
find_name = input()
average_mark = sum(names[find_name]) / 3
print(average_mark)
