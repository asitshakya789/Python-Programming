file1 = open('D:\Python 3.8\File Handling\hello.txt','w')
file1.close()
letter =0 
digit = 0
f =open('D:\Python 3.8\File Handling\hello.txt','r')
for a in f:
    if a.isalpha():
        letter = letter+1
    else:
        digit = digit+1
print("Number of letter",letter)
print("Number of digit",digit)