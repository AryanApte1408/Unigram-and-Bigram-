
from nltk.util import ngrams
import nltk
from tabulate import tabulate
from collections import Counter
import numpy as np

#Data Collection & Cleaning
corpus=" José Mário dos Santos Félix Mourinho was born 26 January 1963 in Setúbal, Portugal. His father was Portuguese goalkeeper Félix Mourinho. Mourinho began his sporting career as a footballer, but never made it as a top player. He studied sports science at the Technical University of Lisbon and spent five years teaching in schools. After spells working as an assistant manager and a youth team coach, in 1992 he became an interpreter for Sir Bobby Robson when he got a job at Sporting Club Portugal. He also followed  Robson to FC Porto in Dec 1993. The two developed a good working relationship with Jose Mourinho learning from Bobby Robson and Robson increasingly trusting the ideas of the young Mourinho. When Robson went to Barcelona in 1996, Mourinho followed – learning Catalan and becoming an important part of the set-up. When Robson left, Mourinho stayed on, working for the Dutchman, Louis van Gaal in a successful two years for Barcelona. Mourinho was also given responsibility for managing Barcelona B team, and Barcelona A for some cup competitions. He later said of his time in Barcelona:In September 2000, he was offered a manager’s post at Benfica, in Portugal. However, this proved short-lived, and in 2001, he left for Uniao de Leira, who with Mourinho in charge were able to make spectacular progress up the league table.In 2002, he was picked to coach Porto, and using innovative scientific methods he helped Porto to unprecedented success: including league titles, cup title, the UEFA cup (2003) and in 2004 the UEFA Champions League.This stood out as an impressive achievement. Few Portuguese sides have won the most prestigious European competitions, and this made him one of the top management targets. Following this triumph, he was tempted to join English Premier League Chelsea, who, under Roman Abramovich, had unprecedented funding on the transfer market. Mourinho became the highest paid manager, earning a salary of over £5 million a year. He took Chelsea to two league titles in 2005 and 2006, though the European Champions League remained elusive.Mourinho’s relationship with the English press was turbulent. At times he entertained, at other times courted controversy. He was rarely out of the headlines. Also, his relationship with Abramovich was uneasy. In September 2007, he left Chelsea out of mutual consent.He moved to Inter Milan in 2008. In 2010, he led Inter to a unique treble, winning Serie A, the Italian Cup and the UEFA champions league. As in England, he had a tempestuous relationship with referees and other managers.In 2010, Mourinho moved to Real Madrid, who were desperate to end their under-achievement relative to Barcelona. After a difficult first season, he won the Spanish La Liga in 2011–12 season. Mourinho has been under great pressure at Real Madrid, but he says he thrives on the pressure: With the retirement of Alex Ferguson at the end of the 2013 season, there was speculation that Jose Mourinho would be offered the ‘dream job’ at Manchester United. But, this did not materialise and in the end, Mourinho returned to his former club Chelsea.In the 2013–14 season, Chelsea finished 3rd in the Premier League, just four points behind winners Manchester City.In the 2014–15 season, Mourinho led Chelsea to another Premier League title, Chelsea won by eight clear points, and also took the League Cup.As defending champions, Chelsea made a disastrous start to the 2015–16 season, losing an unprecedented number of games, and languished in the bottom half of the table, just above relegation. Despite the poor run of form and off the field problems, Mourinho remained popular with most Chelsea supporters. However, it appeared that he had lost the 100% commitment of many of his players. After the Leicester game, Mourinho complained he had been betrayed by some of his players.In May 2016, he was given a new contract by Manchester United. Since Alex Ferguson’s retirement in 2013, Manchester had struggled to live up to their previous standard. In their first season, Manchester began to make some progress, but finished a modest 6th place. In 2016/17, Manchester won the Europa Cup and the League Cup final. In 2017/18 season, Manchester United finished 2nd in the league. However, over the summer of 2018, there was increased disastifaction in the club and reported fall outs between Jose Mourinho and big star players – notably Paul Pogba. After Manchester’s worst start to a Premier League campaign, he was sacked following a 3-1 defeat to arch rivals Jurgen Klopp.Mourinho is considered an excellent tactician and has sometimes been criticised for emphasising defensive strengths rather than encouraging attacking play. However, Mourinho is unmoved by criticism arguing the job of the manager is to win.During his career, Mourinho has often been involved in personal spats with other managers, referees and members of the media. He is not afraid to speak his mind – even if it upsets others."
corpuspf=''.join(ch for ch in corpus if ch not in '!\"#$%&\'()*+,-/:;<=>?@[\]^_`{|}~')  
token = nltk.word_tokenize(corpus)
tokenpfree=nltk.word_tokenize(corpuspf)

#Unigram
unigrams=ngrams(token,1)
unigramspf=ngrams(tokenpfree,1)
unigrams_arr=list(Counter(unigrams).items())
unigramspf_arr=list(Counter(unigramspf).items())

#Bigram
n=2
bigrams=ngrams(token,n)
bigramspf=ngrams(tokenpfree,n)
bigrams_arr=list(Counter(bigrams).items())
bigramspf_arr=list(Counter(bigramspf).items())

#Data Cleaning
unigramsCount={}
unigramsCountpf={}
bigramsCount={}
bigramsCountpf={}
listofBigram=[]
listofBigrampf=[]
for i in unigrams_arr:
    unigramsCount[i[0][0]]=i[1]
for i in unigramspf_arr:
    unigramsCountpf[i[0][0]]=i[1]
for i in bigrams_arr:
    bigramsCount[i[0]]=i[1]
    listofBigram.append(i[0])
for i in bigramspf_arr:
    bigramsCountpf[i[0]]=i[1]
    listofBigrampf.append(i[0])

#Probability
prob={}
probpf={}
for bigram in listofBigram:
    word1 = bigram[0]
    word2 = bigram[1]
    prob[bigram]=float(bigramsCount.get(bigram)/unigramsCount.get(word1))
for bigram in listofBigrampf:
    word1 = bigram[0]
    word2 = bigram[1]
    probpf[bigram]=float(bigramsCountpf.get(bigram)/unigramsCountpf.get(word1))

#Structuring Data
data=[]
datapf=[]
for bigram in listofBigram:
    data.append([bigram,bigramsCount.get(bigram),prob.get(bigram)])
for bigram in listofBigrampf:
    datapf.append([bigram,bigramsCountpf.get(bigram),probpf.get(bigram)])

#Visualization
print()
print('Bigrams With Punctuation')
print()
print(tabulate(data,headers=['Bigrams with Punctuations','Count'],tablefmt="grid"))
print()
print('Bigrams Without Punctuation')
print()
print(tabulate(datapf,headers=['Bigrams without Punctuations','Count'],tablefmt="grid"))

#Save Data
content=tabulate(data,headers=['Bigrams with Punctuations','Count'],tablefmt="grid")
text_file=open("BigramWithPunctuation.txt","w")
text_file.write(content)
text_file.close()
content=tabulate(datapf,headers=['Bigrams with Punctuations','Count'],tablefmt="grid")
text_file=open("BigramWithoutPunctuation.txt","w")
text_file.write(content)
text_file.close()

sp=set(corpus.split())
SparMat=[]
spf=set(corpus.split())
SparMatpf=[]

for i in sp:
    Temp=[i]
    for j in sp:
        if (i , j) in prob:
            Temp.append(prob.get((i,j)))
        else:
            Temp.append(0)
    SparMat.append(Temp)
for i in spf:
    Temp=[i]
    for j in spf:
        if (i , j) in probpf:
            Temp.append(probpf.get((i,j)))
        else:
            Temp.append(0)
    SparMatpf.append(Temp)

content=tabulate(SparMatpf,headers=list(spf),tablefmt="grid")
text_file=open("BigramWithoutPunctuationSparse.txt","w")
text_file.write(content)
text_file.close()
print()

#Testing
print()
sentence="Mourinho began his sporting career as a footballer, but never made it as a top player."
t=nltk.word_tokenize(sentence)
p=1
pf=1
b=ngrams(t,2)
for i in b:
    if(prob.get(i)!=None and probpf.get(i)!=None):
        p=p*(prob.get(i))
        pf=pf*(probpf.get(i))
    elif(prob.get(i)!=None and probpf.get(i)==None):
        p=p*(prob.get(i))
        pf=pf*0
    elif(prob.get(i)==None and probpf.get(i)!=None):
        p=p*0
        pf=pf*(probpf.get(i))
    else:
        p=p*0
        pf=pf*0
print()
print('Bigrams Without Punctuation')
print()
print("Probability of the given sentence \'{a}\' is {b}".format(a=sentence,b=pf))