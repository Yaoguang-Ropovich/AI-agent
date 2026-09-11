from dataclasses import dataclass

@dataclass
class Message:
    role :str
    content : str

@dataclass
class Conversation:
    messages : list[Message]

message_1 = Message("user" , "什么是Agent")
message_2 = Message("assistant" , "Agent可以调用工具完成任务")
messages = [message_1,message_2]
conversation = Conversation(messages)

print(f"消息数量:{len(conversation.messages)}")
print(f"第二条消息:{conversation.messages[1].content}")
