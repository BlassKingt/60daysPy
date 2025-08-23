import os

#生成文件个数
num = 3
src_name = "test"
dst_name = "file"


def gen_txt():
    for i in range(1, num + 1):
        with open(f"dir/{src_name}{i}.txt","w") as f:
            f.write(f"This file's name is {src_name}{i}.txt")

def gen_log():
    for i in range(1, num + 1):
        with open(f"dir/{src_name}{i}.log","w") as f:
            f.write(f"This file's name is {src_name}{i}.log")

def show_files():
    files = os.listdir("dir")
    for file in files:
        print(file)
    return files



def main():
    print(f"生成{num}个txt和log文件。")
    gen_txt()
    gen_log()
    print("目前dir下文件有：")
    dir_files = show_files()

    txt_files = []
    for file in dir_files:
        #txt类型的文件，同时，排除那些已经符合名称格式的文件
        if file.endswith("txt") and not file.startswith(dst_name):
            txt_files.append(file)

    #txt_files 的顺序是随机的，如果不排序，下次通过enumerate生成序号可能会从上次的序列末尾开始        
    #txt_files.sort() 

    print("其中仍需要改名的txt文件有：")        
    print(txt_files)

    print("现在批量修改文件名")
    for no,filename in enumerate(txt_files,start=1):
        src_temp = f"dir/{filename}"
        dst_temp = f"dir/{dst_name}_{no}.txt"
       # print(dst_temp)
        
        if os.path.exists(dst_temp):
            print("%s已存在，先删除"%dst_temp)
            os.remove(dst_temp)
        #易错：这里不是else！
        os.rename(src_temp,dst_temp)
    
    print("目前dir下的文件有：")
    show_files()


if __name__ == "__main__":
    main()




