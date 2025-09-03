class Student:
    def __init__(self,name,score):
        self.stu_name = name
        self.score = score
    
    def say_hello(self):
        print(f"Hello,我是{self.stu_name}")
    
    def show_info(self):
        print(f"姓名: {self.stu_name}, 成绩: {self.score}")
    
    def update_score(self,newscore):
        self.score = newscore
        print(f"新成绩已更新：{self.score}")



def main():
    stu1 = Student("Alex",95)
    stu1.say_hello()
    stu1.show_info()
    stu1.update_score(96)


if __name__ == "__main__":
    main()