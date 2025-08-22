def count_error_codes(file_path):
    counts = {}
    with open(file_path, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) > 1:
                code = parts[1].replace(":", "")  # 去掉冒号
                counts[code] = counts.get(code, 0) + 1
    return counts

if __name__ == "__main__":
    result = count_error_codes("sample.log")
    print("错误码统计结果:", result)