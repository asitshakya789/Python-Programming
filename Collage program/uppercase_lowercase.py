s = input("Enter a sentence")
w,d,u,l,=0,0,0,0
l-w == s.split()
w =len(l-w)
for c in s:
    if c.isdigit():
        d= d+1
    elif c.isupper():
        u= u+1
    elif c.islower():
        l=l+1
print(f"no of words {w}")
print(f"number of digit {d}")
print(f"number of upperletter {u}")
print(f"number of lower case letter {l}")