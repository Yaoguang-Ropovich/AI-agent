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

user1= User("Yaoguang", 1)
message_1= Message("user", "什么是Agent")
message_2= Message("assistant", "Agent可以根据目标调用工具并完成任务")
messages= [message_1, message_2]

conversation= Conversation(user1, messages)

#content_count = 0
#for message in conversation.messages:
#    message_count = message_count + 1

message_count = len(conversation.messages)

print(f"用户：{conversation.user.name}")
print(f"消息数量:{message_count}")
print(f"第一条消息:{conversation.messages[0].content}")
print(f"第二条消息角色:{conversation.messages[1].role}")