'''
Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:
Sample Input
Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
A char calculate() method that calculates a Student object's average and returns the grade character representative of
their calculated average:
'''


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
# Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        total_mark = 0
        for marks in self.scores:
            total_mark += marks
        avg_mark = total_mark / len(self.scores)
        print(avg_mark)
        if (90.0 <= avg_mark <=100.0):
            return 'O'
        elif (80.0 <= avg_mark <90.0):
            return 'E'
        elif (70.0 <= avg_mark < 80.0):
            return 'A'
        elif (55.0 <= avg_mark < 70.0):
            return 'P'
        elif (40.0 <= avg_mark < 60.0):
            return 'D'
        else:
            return 'T'

#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())