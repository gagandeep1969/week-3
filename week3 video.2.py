class person : 
  
     def __init__(self)
      self.name = "sam"
      self.gender = "Male" 
      self.age = 19

      def talk(self):
       print("Hi I'am", self.name)

       def vote(self)
         if self.age<18 : 
          print("I am not eligible to vote")
        else:
         print("I am eligible to vote")

obj1 = person("sam","male")
obj2 = person("jesse","female",.16)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()
