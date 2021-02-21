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

import sys
import numpy as np
from tensorflow.keras.preprocessing import sequence
import os
from .utils import getData
from .preprocessing import tokenizeline

maxlen, word2index, index2word, idx2Label, lookupList = getData(model=False)

def decode(model, text):
    result = ""
    sentences = []
    sentences_len = []
    l  = 0
    text = text.split('\n')
    for line in text:
        sentence = []

        if len(line) < 2:
            continue
        words = tokenizeline(line).strip().split()
        for word in words:
                for ch in word:
                    sentence.append([ch,'WB'])
                    l = l + 1
                sentence.append(['WB','WB'])
                l = l + 1
        if len(sentence) > 0:
            if 'DOCSTART' not in sentence[0][0]:
                sentences.append(sentence)
                sentences_len.append(l)


    listwords,tags = zip(*[zip(*row) for row in sentences])
    X_words_test = np.array([[word2index.get(w, word2index['<UNK>']) for w in words] for words in listwords])
    X_words_test = sequence.pad_sequences(X_words_test, maxlen=maxlen, padding='post')

    test_y_pred = model.predict(X_words_test, batch_size=200).argmax(-1)[X_words_test > 0]

    in_data = []
    for i in range(len(X_words_test)):
        for j in range(len(X_words_test[i])):
            if X_words_test[i][j] > 0:
                in_data.append(index2word[X_words_test[i][j]])

    listchars = []
    for words in listwords:
        for w in words:
            listchars.append(w)

    word = ''
    segt = ''
    sent = 0
    for i in range(len(test_y_pred)):
        if(idx2Label[test_y_pred[i]] in ('B','M')):
            segt += in_data[i]
            word += listchars[i]
        elif(idx2Label[test_y_pred[i]] in ('E','S') and idx2Label.get(test_y_pred[i+1]) !='WB'):
            segt += in_data[i]+'+'
            word += listchars[i]
        elif(idx2Label[test_y_pred[i]] in ('E','S') and idx2Label.get(test_y_pred[i+1]) =='WB'):
            segt += in_data[i]
            word += listchars[i]
        elif(idx2Label[test_y_pred[i]] == 'WB'):
            if(word in lookupList):
                result += lookupList[word] + ' '
            else:
                if('<UNK>' in segt):
                    segt = word
                result += segt + ' '
            word = ''
            segt = ''            
        if(sentences_len[sent] == i):
            sent = sent + 1 
    return result.strip()
