name=input("Enter Name ")
sub1=int(input("Enter Subject1 Marks "))
sub2=int(input("Enter Subject2 Marks "))
total=sub1+sub2
avg=total/2
result="pass" if sub1>=40 and sub2>=40 else "fail"
print(f'''Name {name}
Subject1 {sub1}
Subject2 {sub2}
Total {total}
Avg {avg:.2f}
Result {result}''')
