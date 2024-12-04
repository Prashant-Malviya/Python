words = ['radha','person','qualities','friend','*']

with open('replace.txt' , 'r') as f:
    content = f.read()

for word in words:
    replaceWith = content.replace(word, '$' * len(word))


with open('replace.txt' , 'w') as f:
    f.write(replaceWith)

