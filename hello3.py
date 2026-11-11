import random as rd

sakura = ["sakura", 28, "pink"]
eunchae = {"name":"eunchae","age":19,"color":"red"}

sakura[0] = "SAKURA"
sakura.insert(2,"HKT")
del sakura[1]
sakura.remove("pink")
name1 = sakura.pop(0)

eunchae["name"] = "EUNCHAE"
eunchae.update({"age":20,"birthday":"11/10"})
del eunchae["age"]
name2 = eunchae.pop("name")

# print(name1)
# print(sakura)
# print(name2)
# print(eunchae)

class user:
    def __init__(self,name,id):
        id = rd.randint(1,100)
        self.name = name
        self.id = id

    def print_id(self):
        print(self.id)

user_name = input("waht your name?")

id = 0
user1 = user(user_name,id)

print(f"name:{user1.name}.ID={user1.id}")
user1.print_id()
