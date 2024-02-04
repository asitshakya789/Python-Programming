rollno=int(input("Rollno "))
name=input("Name ")
sub1=int(input("Subject1 Marks "))
sub2=int(input("Subject2 Marks "))
sub3=int(input("Subject3 Marks "))
total=sub1+sub2+sub3
avg=total/3
print(f'''
Rollno {rollno}\tName {name}
Subject1 {sub1}\tSubject2 {sub2}\tSubject3 {sub3}
Total {total}\tAvg {avg:.2f}''')
