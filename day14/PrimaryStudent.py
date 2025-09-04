from Student import Student

class PrimaryStudent(Student):
    def __init__(self,name,sid,score=[]):
        super().__init__(name,f"PS{sid}", score)
    
    def add_score(self, value):
        if (value < 0) or (value >100):
            print(f"Warning: 分数必须是 0 ~ 100！输入的{value}分不生效")
        else:
            self.score.append(value) 

class GraduateStudent(Student):
    def __init__(self, name, sid, score=[], bonus=0):
        super().__init__(name,f"PS{sid}",score)
        self._bonus = bonus
    
    # _bonus和bonus：property方法不能和属性同名
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self,value):
        self._bonus = value

    @property
    def average(self):
        if(super().average != "N/A"):
            return super().average + self._bonus
        else:
            return self._bonus
    
    def __str__(self):
        return f"Student {self.name} (ID: {self.sid}), 平均分：{self.average} （科研分加后）"

def print_info(student):
    # 参数名称无需与基类一致，只是一个标记
    print(student.__str__()) 

def main():
    print("\nPrimaryStudent类")
    stu1 = PrimaryStudent("Bob","0039")
    print_info(stu1)
    stu1.add_score(100)
    stu1.add_score(101)
    print_info(stu1)

    print("\nGraduateStudent类")
    gs1 = GraduateStudent("Max","0011")
    print(gs1)
    gs1.bonus = 5 #property设置了之后，方法当作属性来赋值
    gs1.add_score(100)
    print_info(gs1)

    print(f"gs1是否是GraduateStudent：{isinstance(gs1,GraduateStudent)}")


if __name__ == "__main__":
    main()