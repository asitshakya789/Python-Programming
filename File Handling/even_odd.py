fille = open('D:\Python 3.8\File Handling\even_odd.txt','w')
fille.write("12 \n")
fille.write("13 \n")
fille.write("134 \n")
fille.write("1345 \n")
fille.write("16 \n")
fille.write("16 \n")
fille = open("D:\Python 3.8\File Handling\even_odd.txt",'r')
for i in fille:
    if i.strip:
        num= int(i)
    if(num%2==0):
        even = open('D:\Python 3.8\File Handling\even.txt','w')
        even.write(str(num))
        even.write('\n')
    else:
        odd = open('D:\Python 3.8\File Handling\odd.txt','w')
        odd . write(str(num))
        odd.write('\n')
