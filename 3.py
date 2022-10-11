
files_list = ['example/1.txt', 'example/2.txt', 'example/3.txt' ]
size_dict = {}
for path in files_list:
    size_dict[path] = len(open(path,"r", encoding="utf-8").readlines())

for i in size_dict:
    