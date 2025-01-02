# 4-3. Counting to Twenty
for i in range(1, 21):
    print(i)
print()


# 4-4. One Million
num = []
for i in range(1, 1000001):
    print(i)
    num.append(i)
print()


# 4-5. Summing a Million
num = []
for i in range(1, 1000001):
    print(i)
    num.append(i)
print(f"Min num: {min(num)}")
print(f"Max num: {max(num)}")
print(f"Sum num: {sum(num)}")
print()


# 4-6. Odd Numbers
for i in range(1, 20, 2):    # for i in range(first value, second value, step size)    aka    # for i in range(start, stop, step size)
    print(i)
print()


# 4-7. Threes
multiples_of_3 = []
for i in range(3, 30, 3):
    print(i)
    multiples_of_3.append(i)
print()

"""# A different way to write it
multiples_of_three = list(range(3, 30, 3))
for i in multiples_of_three:
    print(i)
print()"""


# 4-8. Cubes
cubes = []
for i in range(1, 11):
    cube = i ** 3
    cubes.append(cube)
print(cubes)


# 4-9. Cube Comprehension
cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)
