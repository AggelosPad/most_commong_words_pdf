

import re
import pdfplumber
from collections import Counter
import string
from PyPDF2 import PdfFileReader

def deleting_common_words(words_sorted):
    
    i =0
    length = len(words_sorted)
    while (i < length):
        (x, y) = words_sorted[i]
        
        for j in range(0,len(word_to_del)):
            if word_to_del[j] == x:
                words_sorted.pop(i)
             
        length = len(words_sorted)
        i = i+1           

def top_20_words(words_sorted):
    top_words = []
    top_words_values = []
    for i in range(0,20):
        (x,y) = words_sorted[i]
        top_words.append(x)
        top_words_values.append(y)

    print("Top 20 most common words in this pdf file: \n")
    for i in range(0,20):
     print(top_words[i],"(" + str(top_words_values[i]) +")")    


print("Path for the pdf file: ")
path = str(input())


with pdfplumber.open(path) as pdf:

    pdf_reader = PdfFileReader(path,,strict=False)
    pages = pdf_reader.numPages
    
    first_page = pdf.pages[0]
    text =  first_page.extract_text()

    for i in range(1,pages):
        first_page = pdf.pages[i]
        text =  first_page.extract_text() + text
       
    text = text.lower()
    
    word_freq = Counter(text.split())
    
    words_sorted = sorted(word_freq.items(), key=lambda x: x[1],reverse=True)
        
    length = len(words_sorted)
    word_to_del = ['a','i','this' , 'of' , 'to' ,'at','from','the','in','and','on',"a",'A']
     
    
    print('\n\n')

    for i in range(0,len(word_to_del)):
        deleting_common_words(words_sorted)
    
    top_20_words(words_sorted)



                
        
    