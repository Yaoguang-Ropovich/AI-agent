# Day 2 Project: Text Analyzer

def analyze_text(text):
    words = text.split()

    word_count= len(words)
    unique_count= len(set(words))

    #创建一个空dic，记录每个词出现的频词
    word_frequency = {}

    #！！重点！！
    # 第一次后有 {“RAG”=1}，依次类推
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0)+1

    return word_count, unique_count, word_frequency

text = "RAG Agent RAG LangGraph Agent"

a, b, c = analyze_text(text)

print(f"text:{text}")
print(f"Word count: {a}")
print(f"Unique_words: {b}")
print(f"Word frequency:{c}")
