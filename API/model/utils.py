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

import os
import numpy as np
from itertools import chain
from collections import Counter
from .model import build_model

HERE = os.path.dirname(os.path.realpath(__file__)) + '/'
lookup = os.path.join(HERE, 'data/lookup_list.txt')
vocab = os.path.join(HERE, 'data/vocab.txt')
model_path = os.path.join(HERE, 'models/joint.trian.3_keras_weights.h5')

def load_file(path):
    """
    Load sentences. A line must contain at least a word and its tag.
    Sentences are separated by empty lines.
    """
    sentences = []
    sentence = []
    for line in open(path):
        line = line.rstrip()
        if not line:
            if len(sentence) > 0:
                if 'DOCSTART' not in sentence[0][0]:
                    sentences.append(sentence)
                sentence = []
        else:
            word = line.split()
            assert len(word) >= 2
            sentence.append(word)
    if len(sentence) > 0:
        if 'DOCSTART' not in sentence[0][0]:
            sentences.append(sentence)
    words, tags = zip(*[zip(*row) for row in sentences])
    return words, tags

def load_lookuplist(path):
    """
    Load lookp list.
    """
    listwords = {}
    for line in open(path):
        line = line.rstrip()
        listwords[line.replace('+','')] = line     
    return listwords

def load_vocab(path):
    """
    Load vocab/index2word list.
    """
    index2word = []
    for line in open(path):
        line = line.strip()
        index2word.append(line)
    return index2word

def _fit_term_index(terms, reserved=[], preprocess=lambda x: x):
    all_terms = chain(*terms)
    all_terms = map(preprocess, all_terms)
    term_freqs = Counter(all_terms).most_common()
    id2term = reserved + [term for term, tf in term_freqs]
    return id2term

def _invert_index(id2term):
    return {term: i for i, term in enumerate(id2term)}

def getData(model):
    seg_tags = ['E', 'S', 'B', 'M', 'WB']
    idx2Label = {0:'E', 1:'S', 2:'B', 3:'M', 4:'WB'}
    label2Idx = {'E':0, 'S':1, 'B':2, 'M':3, 'WB':4}

    word_embedding_dim = 200
    lstm_dim = 200

    index2word = load_vocab(vocab)
    word2index = _invert_index(index2word)
    
    index2pos = seg_tags
    pos2index = _invert_index(index2pos)
    maxlen = 500 # Set to 500 max num of chars in one line.

    max_features = len(index2word)
    nb_seg_tags = len(index2pos)
    lookupList = load_lookuplist(lookup)
    if model:
        return max_features, word_embedding_dim, maxlen, nb_seg_tags, lstm_dim
    else:
        return maxlen, word2index, index2word, idx2Label, lookupList


def load_model():
    max_features, word_embedding_dim, maxlen, nb_seg_tags, lstm_dim = getData(model=True)
    model = build_model(model_path, max_features, word_embedding_dim, maxlen, nb_seg_tags, lstm_dim)
    model.load_weights(model_path)
    
    return model