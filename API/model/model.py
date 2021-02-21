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

import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense, Embedding, LSTM, Bidirectional, Dropout
from tensorflow.keras.layers import TimeDistributed
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import Callback, EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import Sequential
from .ChainCRF import ChainCRF

def build_model(model_path, max_features, word_embedding_dim, maxlen, nb_seg_tags, lstm_dim):
    model = Sequential()
    model.add(Embedding(max_features, word_embedding_dim, input_length=maxlen, name='word_emb', mask_zero=True))
    model.add(Dropout(0.5))
    model.add(Bidirectional(LSTM(lstm_dim,return_sequences=True)))
    model.add(Dropout(0.5))
    model.add(TimeDistributed(Dense(nb_seg_tags)))
    crf = ChainCRF()
    model.add(crf)
    model.compile(loss=crf.sparse_loss,
                   optimizer= RMSprop(0.01),
                   metrics=['sparse_categorical_accuracy'])

    return model