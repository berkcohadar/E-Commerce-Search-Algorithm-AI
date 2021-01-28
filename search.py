import random
from datetime import datetime

f = open("deneme.txt", "r",encoding="Latin-1")
words = []
for i in f:
    line = i.split(' ')
    words.append(line[5].replace("'","").replace(",","").lower())
length = len(words)
rand = random.randint(0,length-1)
print(length,' Adet Kelime arasindan yapilan bir arama.')
word = words[rand]
print('Yapilmak Istenen Arama: ',word)
rand = random.randint(0,len(word)-1)
word = word.replace(word[rand],'x')
rand = random.randint(0,len(word)-1)
word = word.replace(word[rand],'x')
print('Yanlis Yazilan Arama: ',word)
best={}

start=datetime.now()
for i in words:
    counter=0
    if abs(len(i) - len(word)) < 2:
        for x in range(len(word)):
            try:
                if i[x] == word[x]:
                    counter+=1
            except:
                continue
        best[i] = counter

best = dict(sorted(best.items(), key=lambda item: item[1]))
best = list(best.keys())
print('Programin Tahminleri: ',best[-1],best[-2],best[-3],best[-4],best[-5])
end=datetime.now()
print("Bulma Suresi: ",end-start, )