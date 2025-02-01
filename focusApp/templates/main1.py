import ollama

response = ollama.generate(model="deepseek-r1:1.5b",prompt='what is a qubit?')
print(response['response'])