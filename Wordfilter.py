my_file = open("Input.txt","r")
f = open("badwords.txt")
text = my_file.read()
text = text.lower()
my_file.close()
censored = []
for line in f :
    censored.append(line.rstrip('\n'))
f.close()
for i in censored:
  if i in text:
    hidden = '*' * len(i)
    text = text.replace(i,hidden)
filo = open("Output.txt","w")
filo.write(text)
filo.close()
