def say_hello(name):
    print() 
    print(f'hello {name}! (using {__name__}.say_hello)')
    print()

def count(n):
    print(f'counting to {n} (using {__name__}.count)')
    for i in range(n):
        print(f'i={i}')
    print()


