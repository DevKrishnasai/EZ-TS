# single inheritance = one parent one child

class parent:
    def sai(self):
        print("I am from parent")

class child(parent):            #parent class is passed as argument to class
    def krishna(bro):
        print("I am from child")

c = child()   #creating object to child to access parent as well as child methods
c.krishna()
c.sai()


# Hierarchical inheritance  =  one parent many children

class parent:
    def sai(self):
        print("I am from parent")

class child1(parent):
    def krishna(bro):
        print("I am from child")

class child2(parent):
    def krishna(bro):
        print("I am from child")

c = child1()
d = child2()

c.krishna()
c.sai()
print("----------")
d.krishna()
d.sai()

#Muti level inheritance  =  one parent to child and that child act as parent to another child and so on..  =  its like a chain

class parent:
    def parentMethod(self):
        print("parent method")

class child(parent):
    def childMethod(self):
        print("child method")

class grandchild(child):
    def grandchildMethod(self):
        print("grandchild method")

c = grandchild()
c.parentMethod()
c.childMethod()
c.grandchildMethod()

# Mutiple inheritance = single child inherits from more then 1 parent

class parent1:
    def first(self):
        print("first parent")

class parent2:
    def second(self):
        print("second parent")

class child(parent1,parent2):
    def childMethod(self):
        print("child method")

c = child()
c.first()
c.second()
c.childMethod()

#Hybrid inheritance = it is the combination of other inheritances like below example

#Hierarchical + Mutilevel = hybrid

class parent:
    def first(self):
        print("first")

class child1(parent):
    def childmethod1(self):
        print("child method 1")

class child2(parent):
    def childmethod2(self):
        print("child method 2")

class grandchild(child1):
    def grandchildmethod(self):
        print("grandchild method")

c = grandchild()
d = child2()
c.grandchildmethod()
c.childmethod1()
c.first()

d.first
d.childmethod2()
