
files_list = ['example/1.txt', 'example/2.txt', 'example/3.txt']
size_dict = {}
for path in files_list:
    with open(path, 'r', encoding='utf-8') as f:
        size_dict[path] = len(f.readlines())

with open('out.txt', 'w+', encoding='utf-8') as file_out:
    for i in files_list:
        path = min(size_dict, key=size_dict.get)
        size = size_dict[path]
        with open(path, 'r', encoding='utf-8') as file_read:
            text = file_read.read()
            file_out.write(path + '\n')
            file_out.write(str(size) + '\n')
            file_out.write(text + '\n')
            size_dict.pop(path)
