
from nltk.util import ngrams
import nltk
from tabulate import tabulate
from collections import Counter

#Data Collection & Cleaning
corpus=" José Mário dos Santos Félix Mourinho was born 26 January 1963 in Setúbal, Portugal. His father was Portuguese goalkeeper José Félix Mourinho. Mourinho began his sporting career as a footballer, but never made it as a top player. He studied sports science at the Technical University of Lisbon and spent five years teaching in schools. After spells working as an assistant manager and a youth team coach, in 1992 he became an interpreter for Sir Bobby Robson when he got a job at Sporting Club Portugal. He also followed  Robson to FC Porto in Dec 1993. The two developed a good working relationship with Jose Mourinho learning from Bobby Robson and Robson increasingly trusting the ideas of the young Mourinho. When Robson went to Barcelona in 1996, Mourinho followed – learning Catalan and becoming an important part of the set-up. When Robson left, Mourinho stayed on, working for the Dutchman, Louis van Gaal in a successful two years for Barcelona. Mourinho was also given responsibility for managing Barcelona B team, and Barcelona A for some cup competitions. He later said of his time in Barcelona:In September 2000, he was offered a manager’s post at Benfica, in Portugal. However, this proved short-lived, and in 2001, he left for Uniao de Leira, who with Mourinho in charge were able to make spectacular progress up the league table.In 2002, he was picked to coach Porto, and using innovative scientific methods he helped Porto to unprecedented success: including league titles, cup title, the UEFA cup (2003) and in 2004 the UEFA Champions League.This stood out as an impressive achievement. Few Portuguese sides have won the most prestigious European competitions, and this made him one of the top management targets. Following this triumph, he was tempted to join English Premier League Chelsea, who, under Roman Abramovich, had unprecedented funding on the transfer market. Mourinho became the highest paid manager, earning a salary of over £5 million a year. He took Chelsea to two league titles in 2005 and 2006, though the European Champions League remained elusive.Mourinho’s relationship with the English press was turbulent. At times he entertained, at other times courted controversy. He was rarely out of the headlines. Also, his relationship with Abramovich was uneasy. In September 2007, he left Chelsea out of mutual consent.He moved to Inter Milan in 2008. In 2010, he led Inter to a unique treble, winning Serie A, the Italian Cup and the UEFA champions league. As in England, he had a tempestuous relationship with referees and other managers.In 2010, Mourinho moved to Real Madrid, who were desperate to end their under-achievement relative to Barcelona. After a difficult first season, he won the Spanish La Liga in 2011–12 season. Mourinho has been under great pressure at Real Madrid, but he says he thrives on the pressure: With the retirement of Alex Ferguson at the end of the 2013 season, there was speculation that Jose Mourinho would be offered the ‘dream job’ at Manchester United. But, this did not materialise and in the end, Mourinho returned to his former club Chelsea."
corpuspf=''.join(ch for ch in corpus if ch not in '!\"#$%&\'()*+,-/:;<=>?@[\]^_`{|}~')
token = nltk.word_tokenize(corpus)
tokenpfree=nltk.word_tokenize(corpuspf)

#Unigram
n=1
unigrams=ngrams(token,n)
unigramspf=ngrams(tokenpfree,n)
unigrams_arr=list(Counter(unigrams).items())
unigramspf_arr=list(Counter(unigramspf).items())

#Data Cleaning
unigramsCount={}
unigramsCountpf={}
for i in unigrams_arr:
    unigramsCount[i[0]]=i[1]
for i in unigramspf_arr:
    unigramsCountpf[i[0]]=i[1]

#Total Frequency
print(unigrams_arr)
sumtotal=0
for i in unigrams_arr:
    sumtotal += i[1]
sumtotalpf=0
for i in unigramspf_arr:
    sumtotalpf += i[1]

#Structuring Data
data=[]
datapf=[]
for i in unigrams_arr:
    data.append([i[0],i[1],float(i[1]/sumtotal)])
for i in unigramspf_arr:
    datapf.append([i[0],i[1],float(i[1]/sumtotalpf)])

#Visualization
print()
print('Unigrams With Punctuation')
print()
print(tabulate(data,headers=['Unigrams with Punctuations','Count','Probability'],tablefmt="grid"))
print()
print('Unigrams Without Punctuation')
print()
print(tabulate(datapf,headers=['Unigrams without Punctuations','Count','Probability'],tablefmt="grid"))

#Save Data
content=tabulate(data,headers=['Unigrams with Punctuations','Count','Probability'],tablefmt="grid")
text_file=open("UnigramWithPunctuation.txt","w")
text_file.write(content)
text_file.close()
content=tabulate(datapf,headers=['Unigrams with Punctuations','Count','Probability'],tablefmt="grid")
text_file=open("UnigramWithoutPunctuation.txt","w")
text_file.write(content)
text_file.close()

#Testing
print()
sentence="José Mário dos Santos Félix Mourinho was born 26 January 1963 in Setúbal, Portugal."
t=nltk.word_tokenize(sentence)
p=1
pf=1
b=ngrams(t,1)
for i in b:
    if(unigramsCount.get(i)!=None and unigramsCountpf.get(i)!=None):
        p=p*(unigramsCount.get(i)/sumtotal)
        pf=pf*(unigramsCountpf.get(i)/sumtotal)
    elif(unigramsCount.get(i)!=None and unigramsCountpf.get(i)==None):
        p=p*(unigramsCount.get(i)/sumtotal)
        pf=pf*0
    elif(unigramsCount.get(i)==None and unigramsCountpf.get(i)!=None):
        p=p*0
        pf=pf*(unigramsCountpf.get(i)/sumtotal)
    else:
        p=p*0
        pf=pf*0
print()
print('Unigrams With Punctuation')
print()
print("Probability of the given sentence \'{a}\' is {b}".format(a=sentence,b=p))
print()
print('Unigrams Without Punctuation')
print()
print("Probability of the given sentence \'{a}\' is {b}".format(a=sentence,b=pf))