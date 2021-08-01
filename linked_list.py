class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LL:
    def __init__(self):
        self.head=None
    def add_beg(self,data):
        new=Node(data)
        new.ref=self.head
        self.head=new
    def end_beg(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new
    def LLprint(self):
        if self.head is None:
            return 0 
        else:
            n=self.head
            while n :
                print(n.data,"--->",end=" ")
                n=n.ref
    def add_after(self,data,x):
        n=self.head
        while n:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            return 0
        else:
            new=Node(data)
            new.ref=n.ref
            n.ref=new
    def add_before(self,data,x):
        if self.head is None: return 0 
        if self.head.data==x:
            new=Node(data)
            new.ref=self.head
            self.head=new
            return
        n=self.head
        while n.ref :
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            return 0 
        else:
            new=Node(data)
            new.ref=n.ref
            n.ref=new
    def del_beg(self):
        if self.head is None:
            return 0 
        else:
            
            self.head=self.head.ref
            
            return
        
    def del_end(self):
        if self.head is None:
            return 0 
        n=self.head
        while n.ref.ref is not None :
            n=n.ref
        n.ref=n.ref.ref
        
    def del_value(self,x):
        if self.head is None: return 0 
        if self.head.data == x :
            self.head=self.head.ref
        n=self.head
        while n :
            if n.ref.data==x:
                break
            n=n.ref
        print(n.data)
        if n is None:
            return 0 
        else:
            n.ref=n.ref.ref
            
        
    
        
LL1=LL()
LL1.end_beg(0)

LL1.add_beg(10)

LL1.end_beg(15)

LL1.add_beg(20)

LL1.end_beg(25)

LL1.add_after(5,25)

LL1.add_before(12,15)

LL1.add_before(1,20)

LL1.end_beg(-1)

LL1.add_beg(22)
print(LL1.LLprint())
LL1.del_beg()
LL1.del_end()
LL1.del_value(25)
print(LL1.LLprint())


