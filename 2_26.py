counter = 0
total = 0
score = 0
average = 0
tests = int(input('How many tests did you take? '))
while tests < 0:
    tests = int(input('Please enter a positive number '))
for i in range (tests):
    score = float(input('Enter a test score '))
    while score < 0:
        score = int(input('Please enter a positive number '))
    counter += 1
    total = total + score
print (counter)
print (total)
average = (total / counter)
print (format(average, '.2f')) 

if average >= 0:
    if average >= 90:
        if average == 100:
            print ('Perfect Score')
        else:
            print ('A')
    else:
        if average >= 80:
            print ('B')
        else:
            if average >= 70:
                print ('C')
            else:
                if average >= 60:
                    print ('D')
                else :
                    if average <60:
                        print ('Failed')
