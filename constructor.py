#class Student:#
  #  name="karan"
  #  def __init__(self):
   #     print(self)
    #    print("ADDIng to github")
#s1=Student()
#print(s1)

class Student:
    def __init__(self,fullname):
         self.name=fullname
         print("adding to github")
s1=Student("karan")
print(s1.name) #karan
s2=Student("ayush")
print(s2.name)
