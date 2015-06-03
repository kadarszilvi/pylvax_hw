#!/usr/bin/env python
# -*- coding: utf-8 -*-
import textwrap

# írj egy programot, ami beolvassa az alábbi szöveget (http://paste.ee/r/5IvSb) és
# A. megmondja hogy mely szavak palindromok
# B. statisztikát készít a szavak gyakoriságáról (kinyomtatja csökkenő sorrendben hogy melyik szó hányszor szerepel)
# C. statisztikát készít a mondatok hosszáról (melyik a legrövidebb, és a leghoszabb mondat, milyen hosszúak, valamint az átlagos mondathossz ., ?, ! végű mondatoknál)
# D. a szavakat anagramma csoportokba rendezi

# A szavas részeknél a kisbetű-nagybetű nem számít.

# Előkészítés (beolvasás, szövegtisztítás, szavakra vágás, listába és setbe rakás)
#szöveg beolvasása

def read_the_text(filename):
	text = open(filename)
	opened_text = text.read()
	return opened_text

# KÉSŐBBRE megadott szöveg beolvasása, check
#current_text = read_the_text('website_text.txt')
#print current_text

# szöveg tisztítása

def text_cleaning(text):
	text = text.lower()
	cleaned_text = text.replace(".","").replace(":","").replace("?","").replace(";","").replace("-","").replace(",","").replace("(","").replace(")","").replace('"','')
	return cleaned_text

# KÉSŐBBRE megadott szöveg tisztítása
#current_cleaned_text = text_cleaning(current_text)
#print current_cleaned_text

# szavak listába

def words_in_text(text):
	words_list = text.split()
	return words_list

# listából set

def list2set(the_list):
	the_set = set(the_list)
	return the_set

# KÉSŐBBRE megadott szöveg szavainak összeszedése, check
#current_words = words_in_text(current_cleaned_text)
#print len(current_words)

#KÉSŐBBRE szavak set, check
#current_words_set = list2set(current_words)
#print current_words_set

# annak megvizsgálása, hogy valódi szó-e (csak betűből áll, több, mint egy betű)

def onlyrealwords(wordset):
	realwords_list = []
	for maybewords in wordset:
		if maybewords.isalpha() and len(maybewords)>1:
			realwords_list.append(maybewords)
		else:
			continue
	return realwords_list

# KÉSŐBBRE csak a valódi szavakból kreált, 1x szereplő lista, sorbarakva, check
#words_cleaned = sorted(onlyrealwords(current_words_set))
#print words_cleaned

# A) megoldása:

#palindrom szavak összeszedése

def palindrom_check(wordlist):
	palindrom_list = []
	for words in wordlist:
		if words == words[::-1]:
			palindrom_list.append(words)
		else:
			continue
	return palindrom_list


# A) eredmény:

current_text = read_the_text('website_text.txt')
current_cleaned_text = text_cleaning(current_text)
current_words = words_in_text(current_cleaned_text)
current_words_set = list2set(current_words)
words_cleaned = sorted(onlyrealwords(current_words_set))
A_solution = palindrom_check(words_cleaned)

print "A) The palindrom words: \n%s" % A_solution
line = "_________________________________________________\n"
print line

# B) megoldása:

# szavak gyakorisága, ami legalább 2x szerepel

def word_counter(text, wordlist):
	word_count_list = []
	for words in wordlist:
		if text.count(words)>1:
			word_count_list.append((words, text.count(words)))
		else:
			continue
	return word_count_list

# B) eredmény:

prevalance_real_words = word_counter(current_cleaned_text, words_cleaned)
prevalance_sorted = sorted(prevalance_real_words, key = lambda elements:elements[1], reverse=True)

print "B_v1) The 50 most common words are: \n%s" % prevalance_sorted[:50]
print line

# B) megoldása dict-tel:

# szavak gyakorisága

def word_counter_v2(text, wordlist):
	word_counter_dict = {}
	for words in wordlist:
		if text.count(words)>1:
			word_counter_dict[words] = text.count(words)
	return word_counter_dict

# B)_v2 eredmény:

prevalance_real_words_v2 = word_counter_v2(current_cleaned_text, words_cleaned)
sorted_v2 = sorted(prevalance_real_words_v2.items(), key=lambda x: x[1], reverse=True)
print "B_v2) The 50 most common words with dict:\n", sorted_v2[:50]
print line

# C) megoldása:

# szöveg mondatokra bontása

def sentences_in_text(text):
	replaced = text.replace(". ",".\n").replace("? ","?\n").replace("! ","!\n")
	sentences_list = replaced.splitlines()
	return sentences_list

# KÉSŐBBRE a jelen mondatok összegyűjtése, check
#current_sentences = sentences_in_text(current_text)
#print sentences_in_text(current_text)

def sentence_counter(sentencelist):
	sentence_counter_dict = {}
	for sentences in sentencelist:
		if sentences:
			sentence_counter_dict[sentences] = len(sentences)
	return sentence_counter_dict

# C) eredmény:

current_sentences = sentences_in_text(current_text)
sentence_lenght = sentence_counter(current_sentences)
print "C_a) The shortest sentence is:\n", min(sentence_lenght.items(), key = lambda x:x[1]) 
print "C_b) The longest sentence is:\n", max(sentence_lenght.items(), key = lambda x:x[1])
print "C_c) The average sentence lenght is:\n", len(current_text)/len(sentence_lenght)
print line

# D) megoldása:

# szavakból betűk, sorbarendezve, összefűzve

def wrapping(word):
	wrapped = sorted(textwrap.wrap(word, 1))
	joined = "".join(wrapped)
	return joined

# dict-be gyűjtés: {szó: betűi}

def wrapping_list(wordlist):
	words_and_fonts = {}
	for words in wordlist:
		words_and_fonts[words] = wrapping(words)
	return words_and_fonts

# KÉSŐBBRE valódi szavak beolvasása, listába rakása
#current_words_and_fonts = wrapping_list(words_cleaned)

# set előállítása kereséshez

def fonts_set(fontdict):
	fontlist = fontdict.values()
	fonts_set = set(fontlist)
	return fonts_set

# c=fonts_set, kreál egy listákból álló listát

def create_list(c):
	d = []
	for e in c:
		d.append((e, []))
	return d

# kreált lista első elemét nézi a dict value-ban, ha egyezik, hozzáteszi

def anagram_creator(dict_):
	anagrams = create_list(fonts_set(dict_))
	for l in anagrams:
		for k,v in dict_.items():
			if v == l[0]:
				l[1].append(k)
			else:
				continue
	return anagrams


# testing
# test = "abba baba ajjaj jajaj baj van"
# wordlist_test = ["abba", "baba", "ajjaj", "jajaj", "baj", "van"]
# test_wrap = wrapping_list(wordlist_test)
# print anagram_creator(test_wrap)

# KÉSŐBBRE, check
#current_anagrams = anagram_creator(current_words_and_fonts)
#print current_anagramas[0]

# csak azokat az anagrammákat nyomtassa ki, amiből több, mint egy van

def anagram_printer(list_):
	for l in list_:
		if len(l[1])>1:
			print l[1]

# D) eredmény:

current_words_and_fonts = wrapping_list(words_cleaned)
current_anagrams = anagram_creator(current_words_and_fonts)

print "D) The following words are anagrams:"
anagram_printer(current_anagrams)

