f = open("D:\Python 3.8\File Handling\hello.txt",'r')
f.seek(0)
print(f.tell())
print(f.readline())
f.close()