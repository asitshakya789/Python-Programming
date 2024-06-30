def func(*args,**kwrags):
    print("Positional argument") 
    for arg in args:
        print(arg)

    print("Keyword argument")
    for key,value in kwrags.items():
        print('f{key}:{value}')
func(name ="asit",age = 30,)
