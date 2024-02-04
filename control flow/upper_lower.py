ch =  input("Enter any charachter :=")
if ch>='a' and ch<='z':
    ch =chr(ord(ch)-32)
    print(ch)
elif ch>='A' and ch<='Z':
    ch =chr(ord(ch)+32)
    print(ch)
else:
    print("input character must be alphabet")