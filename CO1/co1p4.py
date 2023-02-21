text="This is a sample of generated text"
words={}
for word in text.split(" "):
    if word in words.keys():
        words[word]+=1
    else:
        words[word]=1
print(words)        
        