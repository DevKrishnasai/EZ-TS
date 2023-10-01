class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def last(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)
    def first(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next=self.head
            self.head=temp

linkedList = LinkedList()
while True:
    n = int(input("Enter a value: "))
    if n==-1:
        print("Bro stopped")
        break
    linkedList.last(n)

temp = linkedList.head
while temp!=None:
    print(temp.data)
    temp=temp.next

linkedList.first(11)
print("--------------")

temp = linkedList.head
while temp!=None:
    print(temp.data)
    temp=temp.next

