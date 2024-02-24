def program (**kwargs):
    for key, value in kwargs.items():
        print(key,"==",value)
program(first = "Hello",mid = "welcome",last = "yaar")