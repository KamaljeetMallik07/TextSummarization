import re
import nltk
import math

from nltk.stem import PorterStemmer 
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
#run only once to download it.
#nltk.download('stopwords')
#nltk.download('wordnet')

fp=open("C:/Users/lenovo/Desktop/DS/Project/OverCoatAndLeaf.txt","r",encoding="utf8")#Opening the file
summary_lines=0#No of lines of summary you want.

text=fp.read()#Reading the file contents
sentence=re.split('[.]',text)#Splitting the paragraph to get sentences
sentence.pop()#To remove additional noise
print("No of sentences :",end=" ")
print(len(sentence))
summary_lines=int(input("Enter no of lines of summary you want: "))
#Giving id to each sentence
sentenceid={}
for i in range(len(sentence)):
	sentence[i]=sentence[i].lstrip()
	sentenceid[i]=(sentence[i]+".")
#print(sentenceid)
#Removing unwanted noise
text=text.replace(',',' ')
text=text.replace("'ll","")
text=text.replace('-','')
text=text.replace('!','')
text=text.replace('.',' ')
text=text.replace('"','')
text=text.replace(';',' ')
text=text.replace("'s","")
text=text.replace("n't","")
text=text.replace("'d","")

#print(text)
#Removing stop words
w=word_tokenize(text)
words=[word for word in w if not word in stopwords.words()]
#print(words)
#Stemming to get the root word #Note: doesn't matter which you use!
ps = PorterStemmer()
lm=WordNetLemmatizer()
for r in range(len(words)):
	words[r]=ps.stem(words[r])
	words[r]=words[r].lower()
print(words)
#Counting total occurences of each word 
word_dict={}
for w in words:
	if w not in word_dict.keys():
		word_dict[w]=words.count(w)
print(word_dict)
#Finding weight of each sentence
sentence_weights={}
word_sqr=0
k=0
total_weight=0
for i in sentence:
	#print(i)
	words_sent=re.findall(r'\w+',i)
	for j in words_sent:
		for key,value in word_dict.items():
			if(key==j):
				#print(j+":"+key)
				word_sqr+=value**2
	word_sqr=math.sqrt(word_sqr)
	for j in words_sent:
		for key,value in word_dict.items():
			if(key==(j)):
				total_weight+=value/word_sqr	
	#print(total_weight)
	sentence_weights[k]=total_weight
	k+=1
	total_weight=0
	word_sqr=0	
	#break
print(sentence_weights)
sentence_weights1=sentence_weights.copy()
#print(sentence_weights1)
#Finding the sentences having max weigths
l=[]
for i in range(summary_lines):
	max_key=max(sentence_weights1,key=sentence_weights1.get)
	l.append(max_key)
	del sentence_weights1[max_key]
l.sort()
#print(l)
#Storing the suummary
summary=str()
for i in l:
	for key,value in sentenceid.items():
		if(key==i):
			summary+=str(value)+"\n"
#print(summary)
#Writing the summary into a file
final=open('summary_OverCoatAndLeaf.txt','w')
final.write(summary)
print("Summary formation complete!",end="")
fp.close()
final.close()