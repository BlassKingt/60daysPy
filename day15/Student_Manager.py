from Student import Student
import json

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        if not self.students:
            print("\n没有学生信息。")
            return
        else:
            for student in self.students:
                print(student)

    def add_score(self, ID, score):
        for student in self.students:
            if student.ID == ID:
                student.add_score(score)
                break
   
   # 无需类方法，普通实例方法即可，因为本manager存储了所有student，其实只需要一个manager
    def generate_id(self):
        if not self.students:
            return "001"
        return str(max(int(student.ID) for student in self.students) + 1).zfill(3)
        # str.zfill() 是 Python 字符串的一个方法，用来在字符串的左边填充 '0'，直到指定的宽度。

    def save_data(self):
        with open("students.json", "w") as file:
            json.dump([student.__dict__ for student in self.students], file)
        # [] 是必要的
        # 因为 json.dump 需要“一个”可序列化的对象列表
        # 必须用 w 而不是 a， 因为每次保存时都需要覆盖旧数据，若每次新增数据，将导致列表紊乱

    def load_data(self):
        try:
            with open("students.json", "r") as file:
                student_data = json.load(file)
                # save_data 存的是一个list，含有学生信息的字典列表
                self.students = [Student(**data_dict) for data_dict in student_data]
                #**data_dict 解包字典中存储的学生信息
        except FileNotFoundError:
            self.students = [] # 有可能首次载入无文件
        except json.JSONDecodeError:
            self.students = []


def main():
    manager = StudentManager()
    manager.load_data()

    while True:
        print("\n1. 添加学生(姓名：必须，成绩：可选，学号：无需-会自动生成)")
        print("2. 查看所有学生")
        print("3. 更新成绩")
        print("4. 保存数据并退出")
        choice = input("请选择操作: ")

        if choice == "1":
            name = input("请输入学生姓名: ")
            score_input = input("请输入学生成绩: ")
            if score_input:
                score = [int(score_input)]
            else:
                score = []
            ID = manager.generate_id()
            
            student = Student(name, ID, score)
            manager.add_student(student)
        elif choice == "2":
            manager.display_all_students()
        elif choice == "3":
            ID = input("请输入学生ID: ")
            score = int(input("请输入新成绩: "))
            manager.add_score(ID, score)
        elif choice == "4":
            manager.save_data()
            break
        else:
            print("无效选择，请重试。")

if __name__ == "__main__":
    main()