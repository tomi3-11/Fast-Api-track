from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World")


name = input("What is your name? ")
say_hi()
say_hi(name)
