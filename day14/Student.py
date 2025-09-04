class Student:
    def __init__(self,name,sid,score=[]):
        self.name = name
        self.sid = sid
        self.score = score
    
    def say_hello(self):
        print(f"Hello,我是{self.name}")
    
    def add_score(self,value):
        self.score.append(value)
    
    @property
    def average(self):
        if len(self.score) is not 0:
            return sum(self.score)/len(self.score)
        else:
            return "N/A"

    def __str__(self):
        return f"Student {self.name} (ID: {self.sid}), 平均分：{self.average}"


    


def main():
    stu1 = Student("Alex","S025")
    #stu1.say_hello()
    print(stu1)

    stu1.add_score(95)
    stu1.add_score(96)
    #stu1.add_score(101)
    print(stu1)



if __name__ == "__main__":
    main()