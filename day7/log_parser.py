#1
def readfile(filePh):
    lines = []
    with open(f"{filePh}","r") as file:
        for line in file:
            lines.append(line.strip())
    return lines
#2
def is_error_in_line(line):
    return ("error" in line.lower())
def find_error(line):
    if is_error_in_line(line):
        return line

#3
def save_err_list(tline,tlist):
    tlist.append(tline)
    return tlist

#Target
def log_parser(filePh):
    readlines = []
    readlines = readfile(filePh)
    #print(readlines)
    err_lines = []
    for line in readlines:
        if is_error_in_line(line):
            save_err_list(find_error(line),err_lines)
    return err_lines


def main():
    err_log = log_parser("app.log")
    print("ERROR 行:")
    for err in err_log:
        print(err)



if __name__ =="__main__":
    main()

