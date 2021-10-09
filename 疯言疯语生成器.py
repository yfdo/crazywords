# 疯言疯语生成器
# 作者：意见
# 献给我的道标和救主，在过去、现在也在未来

#import pandas as pd
import random

punclist=['，']*5+['。']*5+['！']*3+['……']*3+['，，，。。。']+['（）']
l1=[]
l2=[]
l3=[]
l4=[]
re=[]
me='我'
my='我的'
l33=['那么']*3+['又']*3+['意想不到地']

num1=random.randint(3,6)
num2=random.randint(3,6)
num3=12-num1-num2

   
#print('自从得了精神病，整个人精神多了！')
name=input('今天想对谁发疯？\n')
#sex=input('他还是她？')

def punc():
    pun=random.choice(punclist)
    return pun

def be():
    return random.choice(['是','是','你是'])
    #if sex=='她':
     #   return random.choice('是','是','她是')
    #else:
     #   return random.choice('是','是','他是')

def ch(i):
    if i==1:
        return random.choice(l1)
    elif i==2:
        return random.choice(l2)
    elif i==3:
        return random.choice(l33)+random.choice(l3)
    else:
        return random.choice(l4)

#o1=pd.read_excel('words.xls',usecols=[0],na_values='').values.tolist()
#for i in o1:
#    l1.append(i[0])

f=open('words.txt',encoding='utf-8')
txt=[]
for line in f:
    txt.append(line.strip())
l1=txt[0].split(',')
l2=txt[1].split(',')
l3=txt[2].split(',')
l4=txt[3].split(',')

raw=[]
raw.append(ch(1))
raw.append(my+name)
raw.append(my+ch(2)+'般的'+name)
for i in range(num1):
    raw.append(be()+ch(2))
for i in range(num2):
    raw.append(ch(3))
for i in range(num3):
    raw.append(me+ch(4))

for i in range(random.randint(2,4)):
    raw.insert(random.randint(0,len(raw)),name)

for i in range(len(raw)):
    re.append(raw[i])
    re.append(punc())

print(''.join(re))