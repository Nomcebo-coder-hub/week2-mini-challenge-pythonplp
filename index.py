sum = [1, 2, 3]
print(sum)

books = ("Othello", "Romeo and Juliet", "Hamlet")
print(books[0])
print(books[1])
print(books[2])

name = {"What is your name?: Nomcebo"}
print(name)
age = {"What is your age?: 26"}
print(age)
favourite_color = {"What is your favourite color?: Pink"}
print(favourite_color)

A = {1, 3, 5}
B = {1, 2, 3}
print('Intersection using &:', A & B)
print('Intersection using intersection():' , A.intersection(B))

A = {2, 3, 5}
B = {1, 2, 6}
print('Difference using &:' , A - B)
print('Difference using difference():' , A.difference(B))