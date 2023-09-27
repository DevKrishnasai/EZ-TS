#class without making object
class name:
    def first():
        print("first")
    def second():
        print("second")

name.first()

#class with making object
class Name:
    def first(self):
        print("first")
    def second(self):
        print("second")

c = Name()
d = Name()
print(c==d)
