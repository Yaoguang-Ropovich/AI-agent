# -------------------------
# class|method
# -------------------------
print("\n----- class|method -----")

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old"
    
user1 = User("Yaoguang", 25)

print(user1.name)
print(user1.age)

print(user1.introduce())

# -------------------------
# dataclass
# -------------------------
print("\n----- dataclass -----")

from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str

message = Message("user","什么是RAG")
print(message)
print(message.role)
print(message.content)

# -------------------------
# compare
# -------------------------
print("\n----- compare -----")

class NormalUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old"

normaluser = NormalUser("Yaoguang", 25)
print(normaluser.name) 
print(normaluser.age)
print(normaluser.introduce())


from dataclasses import dataclass
@dataclass
class DataUser:
    name:str
    age:int

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old"

datauser = DataUser("Yaoguang", 25)
print(datauser.name)
print(datauser.age)
print(datauser.introduce())

print(normaluser)
print(datauser)

# -------------------------
# typing
# -------------------------
print("\n----- typing -----")

def calculate_price(price:float, quantity:int) ->float:
    total = price * quantity 
    return total

Total_price = calculate_price(19.9, 3)
print(f"Total price: {Total_price:.1f}")

def show_age(age: int) -> int:
    return age

result = show_age("25")

print(result)
print(type(result))

# -------------------------
# 数据模型
# -------------------------
print("\n----- 数据模型-----")

from dataclasses import dataclass
@dataclass
class Message:
    role: str
    content: str

@dataclass
class User:
    name: str
    user_id: int

@dataclass
class Conversation:
    user: User
    messages: list[Message]

user1 = User("Yaoguang", 1)
message1 = Message("user", "什么是RAG")
message2 = Message("assistant", "RAG是一种检索增强生成技术")
messages = [message1, message2]
conversation = Conversation(user1, messages)

print(conversation.user.name)
print(conversation.user.user_id)
print(conversation.messages[0].role)
print(conversation.messages[0].content)
print(conversation.messages[1].content)








