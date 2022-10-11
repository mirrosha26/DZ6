import os

dir_path = 'example_3'
size_dict = {}
for filename in os.listdir(dir_path):
    path = os.path.join(dir_path, filename)
    with open(path, 'r', encoding='utf-8') as f:
        size_dict[path] = len(f.readlines())

return_dir_path = 'return'
return_path = os.path.join(return_dir_path, 'answer.txt')
with open(return_path, 'w', encoding='utf-8') as file_out:
    for i in os.listdir(dir_path):
        path = min(size_dict, key=size_dict.get)
        size = size_dict[path]
        with open(path, 'r', encoding='utf-8') as file_read:
            text = file_read.read()
            file_out.write(path + '\n')
            file_out.write(str(size) + '\n')
            file_out.write(text + '\n')
            size_dict.pop(path)
