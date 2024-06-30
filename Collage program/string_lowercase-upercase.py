from numpy import True_
while True_:
    line  = input("Enter the Sentence :-")
    if line.lower() == "quit":
        break
    upper_line = line.upper()
    print(upper_line)