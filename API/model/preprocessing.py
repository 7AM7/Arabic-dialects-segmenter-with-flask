#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this script uses pretrained model to segment Arabic dialect data.
# it takes the pretrained model trained on joint dialects and the 
# training vocab and produces segmented text
#
# Copyright (C) 2017, Qatar Computing Research Institute, HBKU, Qatar
# Las Update: Sun Oct 29 15:34:43 +03 2017
#
# BibTex: @inproceedings{samih2017learning,
#  title={Learning from Relatives: Unified Dialectal Arabic Segmentation},
#  author={Samih, Younes and Eldesouki, Mohamed and Attia, Mohammed and Darwish, Kareem and Abdelali, Ahmed and Mubarak, Hamdy and Kallmeyer, Laura},
#  booktitle={Proceedings of the 21st Conference on Computational Natural Language Learning (CoNLL 2017)},
#  pages={432--441},
#  year={2017}}
#
__author__ = 'Ahmed Abdelali (aabdelali@hbku.edu.qa)'

import re
import datetime
from nltk.tokenize import word_tokenize
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def valid_date(datestring):
    try:
        mat=re.match('^(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
        if mat is not None:
            datetime.datetime(*(map(int, mat.groups()[-1::-1])))
            return True
    except ValueError:
        pass
    return False

def valid_number(numstring):
    try:
        mat=re.match("^[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?$", numstring)
        if mat is not None:
            return True
    except ValueError:
        pass
    return False
    
def valide_time(timestring):
    try:
        mat=re.match('^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$', timestring)
        if mat is not None:
            datetime.time(*(map(int, mat.groups()[::])))
            return True
        mat=re.match('^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$', timestring)
        if mat is not None:
            datetime.time(*(map(int, mat.groups()[::])))
            return True
        mat=re.match('^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9]).([0-9]?[0-9])$', timestring)
        if mat is not None:
            datetime.time(*(map(int, mat.groups()[::])))
            return True
    except ValueError:
        pass        
    return False

def valid_email(emailstring):
    try:
        mat=re.match('^[^@]+@[^@]+\.[^@]+$',emailstring)
        if mat is not None:
            return True
    except ValueError:
        pass
    return False

def removeDiacritics(instring):
    return re.sub(r'[ـًٌٍَُِّْ]', '', instring)

def tokenizeline(txtstring):
    elements =[]
    #Remove Kashida and diacritics.
    txtstring = removeDiacritics(txtstring)

    #Split on Arabic delimiters
    for aword in re.split(r'،|٫|٫|٬|؛',txtstring):
        for word in aword.split():
            #print("==>",word)
            if (word.startswith("#")
                or word.startswith("@")
                or word.startswith(":")
                or word.startswith(";")
                or word.startswith("http://")
                or word.startswith("https://")
                or valid_email(word)
                or valid_date(word)
                or valid_number(word)
                or valide_time(word)):

                elements.append(word)
            else:
                for elt in word_tokenize(word):
                    elements.append(elt)
    output = ''
    for elt in elements:
        output = output + ' ' + elt 
    return output