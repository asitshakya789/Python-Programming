file1 = open('D:\Python 3.8\File Handling\hello.txt',"w")
l = ["hey i am asit \n","i am a student \n", "i am engineering student \n"]
s = "i loove you \n"
file1.write(s)
file1.writelines(l)
file1 = open('D:\Python 3.8\File Handling\hello.txt','r')
print(file1.read())
file1.close()