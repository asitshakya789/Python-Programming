l = ['asit ', "ka namr" , "kumar ", "ho sakta hai"]
file1 = open('D:\Python 3.8\File Handling\hello.txt','w')
file1.writelines(l)
file1.close()
file1 = open('D:\Python 3.8\File Handling\hello.txt','r')
lines = file1.readlines()
print(lines)
file1.close()