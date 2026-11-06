import random

print(random.choice(["a","b","c"]))

sakura = ["sakura",28,"3/19"]
chaewon = ["chaewon",26, "8/1"]

yunjin = {"name":"yunjin","old":24,"bithday":"10/16"}

def open_userinfo(name):
    i = 0
    while i < len(name):
        print(name[i])
        i += 1

# open_userinfo(chaewon)

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def username(self):
        print(f"I am {self.name}")


user1 = User("tanaka",22)

