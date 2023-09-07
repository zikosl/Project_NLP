from nltk import FreqDist
from nltk.tokenize import word_tokenize
import csv
#Utile Function 
def splitbyspace(l,Tags,dc):
    l= str(l)
    l = l.replace('\n','')
    l=l.split(" ")
    a=[]
    for i in l:
        tag = i.split('_')
        word = tag[1]
        tag = tag[0]
        if(tag not in Tags):
            Tags.append(tag)
        a.append([tag,word])    
        dc[word] = tag
    return a
def save_Tokens(TokenList,text,Tags,dc):
    a =[]
    with open('tokenized.txt','w+',encoding='utf-8') as out:
        for line in text:
            a+=splitbyspace(line,Tags,dc)
        out.write(str(a))
        out.close()
    TokenList = a

#extraireAll Gram
def get_Ngram(f,dc):
    files = f.read()
    files = files.replace(',','.')
    files = files.split(' ')
    with open('gram.cfg',"w+") as gr :
        u = 0
        for i in files :
            rs = extraireRule(i,dc)
            gr.write('S'+str(u)+"->"+rs)
            u+=1

def extraireRule(text,dc):
    text = text.split(' ')
    gram = ""
    for i in text:
        gram += dc[i]
    return gram

def get_Frequence(sent):
    N = len(word_tokenize(sent))
    fd = FreqDist(word for word in word_tokenize(sent))
    with open('Results.csv', 'w') as csvfile:
        fieldnames = ['mot','frequence','prob','r*prob']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        v = 1
        for i in fd:
            writer.writerow({'mot': str(i),'frequence':str(N),'prob': str(fd[i]), 'r*prob': str(fd[i])})
            v+=1
            if(v>15):
                break

#Load File
#dc = {}
#f = open('free-french-treebank-master\\130612\\frwikinews\\txt-tok-pos\\frwikinews-20130110-pages-articles.txt.tok.stanford-pos','r',encoding='utf-8')
#TokenList =[]
#Tags = []
# save_Tokens()
# get_Ngram()
#get_Frequence()
# print(Tags)
# #Get Ngram


# # exxtract n-grame