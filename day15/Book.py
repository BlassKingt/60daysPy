import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"<<{self.title}>> by {self.author}"

def read_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def main():
    book = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    data_list = [book, book2, book3]

    with open("books.json", "w") as file:
        json.dump([book.__dict__ for book in data_list], file, indent=4)
# 在 Python 里，大多数对象都有一个 __dict__ 属性，它是一个字典，存放这个对象所有的实例属性
# book.__dict__ for book in data_list 返回列表中的所有book对象的所有属性，然后通过[]集合传给dump
    #print(read_file("books.json"))
    for i in range(3):
        data_dict_list = read_file("books.json")
        data_dict = data_dict_list[i]
        print(Book(**data_dict)) # 字典解包

if __name__ == "__main__":
    main()