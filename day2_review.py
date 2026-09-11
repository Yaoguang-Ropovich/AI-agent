# -------------------------
# test 1
# -------------------------
print("\n----- test 1 -----")

message = [ "RAG", "Agent", "RAG", "LangGraph", "Agent"]

print(len(message))
print(len(set(message)))
print(message[-1])
print(message[1:4])

# -------------------------
# test 2
# -------------------------
print("\n----- test 2 -----")

dicts = { "role" : "user", 
         "content": "什么是RAG",
         "tokens" : 12
         }

print(dicts["role"])

dicts["tokens"]= 20
#dicts.append(model = "gpt-5")
dicts["model"]= "gpt-5"

#dicts.get("temperature",0)
print(dicts.get("temperature", 0))

print(len(dicts))

#print(dicts.key)
#print(dicts.value)
print(dicts.keys())
print(dicts.values())

# -------------------------
# test 3
# -------------------------
print("\n----- test 3 -----")

def calculate_score(correct, total):
    result = correct/ total * 100
    return result

result = calculate_score(8, 10)
#print(f"Score : calculate_score(8, 10) ")
print(f"Score = {result} ")

# -------------------------
# test 4
# -------------------------
print("\n----- test 4 -----")

messages = [3, 8, 12, 5, 15, 2]

count = 0

for message in messages:
    if message >= 8:
        print(message)
        count = count + 1

print(f"Count = {count}")        
    
# -------------------------
# text_analyzer_review
# -------------------------
print("\n----- text_analyzer_review -----")

def text_analyzer(text):

    words = text.split()

    word_count = len(words)

    unique_words = len(set(words))

    word_frequency = {}

    for word in words:
        word_frequency[word]= word_frequency.get(word,0) +1
    return word_count, unique_words, word_frequency

text = "RAG Agent RAG LangGraph Agent"

(a,b,c)= text_analyzer(text)

print(f"Text: {text}")
print(f"Word count: {a}")    
print(f"Unique words:{b}")   
print(f"Word frequency:{c}")   
