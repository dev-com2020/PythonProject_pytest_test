def greet(name):
    print(f"Hi! {name}")

def shout_deco(func):
    def wrapper(name):
        print('!!!')
        func(name.upper())
        print("!!!")
    return wrapper

greet = shout_deco(greet)
greet("Tomek")