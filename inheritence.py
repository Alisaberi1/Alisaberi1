import random


class Human:
    def __init__( self, name, l_name, job ):
        self.name=name
        self.lname=l_name
        self.job=job

    def sleep(self):
        return f"{self.name}{self.lname} sleeping...ZZZZZZ"


class Student(Human):
    def __init__( self , name , l_name , job , Student_ID ):
        super().__init__( name , l_name , job )
        self.Student_ID = Student_ID
    def score(self):
        z=random.randint(0,21)
        if z<=10:
            print("you should study more")
        if z==10:
            print("you can be better")
        elif z>=10:
            print("that's not bad but not enough")
        elif z>=17:
            print("you are perfect")
        return z
a=input("name:")
s=input("l_name:")
d=input("job:")

g=Student(a,s,d,4001020934997)

print(g.score())
ali=Human(a,s,d)
print(ali.sleep())
