"""
Day 2 - Python 数据结构
"""

# -------------------------
# 1. list
# -------------------------
#有顺序、可修改
print("\n----- list -----")

# list：有顺序、可修改、可以保存多个值
messages = ["你好", "什么是RAG", "介绍一下Agent"]

#下标从0开始
print(messages)
print(messages[0])
print(messages[1])

#append：在列表末尾添加一个元素
messages.append("什么是LangGraph") 

print(messages)

#len：获取列表元素数量
print(len(messages))

#修改指定下标的元素
messages[1] = "RAG是什么"

print(messages)

#-1：倒数第一个元素
print(messages[-1])

#切片[开始位置：结束位置]
#左包右不包
#此处取下标1和2
print(messages[1:3])
print(type(messages))

# -------------------------
# 2. dict
# -------------------------
#词典，keys和values
print("\n----- dict -----")

# dict 使用 key-value（键值对）保存数据
message = {
    "role": "user",
    "content": "什么是RAG",
    "tokens": 12
}

# 通过 key 获取对应的 value
print(message)
print(message["role"])
print(message["content"])

# 修改已有 key 的 value
message["tokens"] = 15

# 添加新的 key-value
message["model"] = "gpt-5"

print(message)

# dict 的 len() 统计键值对数量
print(len(message))

# get：安全地获取某个 key(如果直接获取某个不存在的元素会报错，get不会)
print(message.get("model"))
print(message.get("temperature"))
print(message.get("temperature", 0))

# keys：获取所有 key
print(message.keys())

# values：获取所有 value
print(message.values())

#生成keys列表
print(list(message.keys()))

#生成values列表
print(list(message.values()))

#查看类型
print(type(message))
print(type(message.keys()))
print(type(list(message.keys())))

# -------------------------
# 3. set
# -------------------------
#去重数据，去重后无顺序

print("\n----- set -----")

# 原始文档 ID，其中存在重复项
doc_ids = ["doc1", "doc2", "doc1", "doc3", "doc2"]

# list 转成 set，会自动去重
unique_ids = set(doc_ids)

print(doc_ids)
print(unique_ids)

# 比较去重前后的数量
print(len(doc_ids))
print(len(unique_ids))

# add：向 set 添加元素
unique_ids.add("doc4")
print(unique_ids)

# in：判断元素是否存在
print("doc2" in unique_ids)
print("doc5" in unique_ids)

# -------------------------
# 4. tuple
# -------------------------
#有顺序、不可修改
print("\n----- tuple -----")

model_info = ("gpt-5", 128000, "OpenAI")

print(model_info)
print(model_info[0])
print(model_info[1])
print(len(model_info))

# -------------------------
# 5. function
# -------------------------
print("\n-----function-----")

#定义函数：接受一个名字，返回问候语
def greet(name):
    return "Hello "+ name 

message = greet("Yaoguang")
print(message)

#定义函数：接受两个数字，返回相加结果
def add(a,b):
    #return "The result is " + str(a+b) ，类型转换：int -> string
    #return f"The result is {a+b}" ,fstring：在字符串里直接嵌入变量或表达式
    return a+b

result = add(10,20)
#print(result)
print("The result is",result)

#函数处理list
def count_items(items):
    return len(items)

documents = ["doc1", "doc2", "doc3"]

document_count = count_items(documents)

print(f"Document count: {document_count}")

#可以直接调用，不需要return
def greet(name):
    print(f"Hello {name}")
greet("Yaoguang")

# -------------------------
# 6. data processing
# -------------------------
print("\n----- data processing -----")

documents = ["RAG", "Agent", "LangGraph"]

for document in documents:
    print(document)
   
print("\n ----- list + dict + for -----")

documents = [
    {"title":"RAG",
    "score":0.92},
    {"title":"Agent", 
     "score":0.85},
    {"title":"LangGraph", 
     "score":0.88}
]

for document in documents:
    print(document["title"])
    print(document["score"])

print(documents)
print(len(documents))

for document in documents:
    print(document.keys())
    print(document.values())

print(type(documents))
print(type(documents[0]))
print(type(documents[0]["title"]))
print(type(documents[0]["score"]))

# -------------------------
# 7. if
# -------------------------
print("\n----- if -----")

for document in documents:
    if document["score"]>=0.9:
        print(document["title"])

# -------------------------
# 8. 综合数据处理
# -------------------------
print("\n----- 综合数据处理 -----")

def filter_documents(documents, threshold):
    results = []
    for document in documents:
        if document["score"] >= threshold:
            results.append(document["title"])

    return results

filtered_documents = filter_documents(documents, 0.87)
print(type(filtered_documents))
print(filtered_documents)
