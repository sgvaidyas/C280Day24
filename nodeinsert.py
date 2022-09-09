class Node:
   def __init__(self,ele):
      self.data = ele
      self.top=None
      self.bottom=None
      self.right= None


class ImplementTopDown:
    def __init__(self):
        self.head=None

    def insert(self,ele):
        temp = Node(ele)
        if self.head == None:
            self.head=temp
        else:
            x = ele%10
            ptr = self.head
            while ptr.bottom!=None and ptr.data%10<x:
                if ptr!=self.head:
                    print(ptr.top.data,"ptr.bot = ",ptr.bottom.data,ele,ptr.data%10,x)
                else:
                    print(ptr.data)
                ptr = ptr.bottom
                print(ptr.bottom!=None and ptr.data%10<x,ele)


            print("---------------------")

            if (ptr.top==None and ptr.data%10>x) :
                temp.bottom = self.head
                self.head.top = temp
                self.head = temp

            elif ptr.bottom==None and ptr.data%10<x:
                ptr.bottom=temp
                temp.top = ptr
            else:
                pp = ptr.top
                pp.bottom  =   temp
                temp.top   =   pp
                temp.bottom=   ptr
                ptr.top    =   temp

    def disp(self):
        if self.head==None:
            print("No elements ")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data,"\n |\n |\n V")
                ptr = ptr.bottom
            print("None")

ob = ImplementTopDown()
ob.insert(33)
ob.insert(66)
ob.insert(11)

ob.insert(92)
ob.insert(58)
ob.disp()
