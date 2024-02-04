ch = input("Enter the charachter :=")
if ch >='a'and ch<='z' or ch>='A' and ch<='Z':
    print(f'{ch} is  character:')
elif ch>='0 ' and ch<='9':
    print(f'{ch} is a digit')
else:
    print("Some spaicel character")