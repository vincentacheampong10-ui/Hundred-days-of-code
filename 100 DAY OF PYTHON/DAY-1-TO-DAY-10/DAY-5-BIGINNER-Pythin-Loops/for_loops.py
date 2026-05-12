fruits = ["Apple", "Peach", "Pear",]
for fruit in fruits:
    print(fruit)


student_scores = [100,99,86,89,0,28,53,67,89,99,100,23,45,67,67,85,95]

sum = 0
for score in student_scores:
    sum += score
    print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
        print(score)


# Range Function with for loops

for number in range(1,10):
    print(number)
