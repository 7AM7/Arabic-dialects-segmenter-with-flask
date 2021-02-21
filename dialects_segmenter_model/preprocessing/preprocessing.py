
# Correct the segmented tweets 
# Create lookup list file
# Format data to Conll

# author: Ahmed Abdelali
# Date : Sun Jan 15 10:52:40 AST 2017
import pandas as pd
import sys
import codecs
import os

HERE = os.getcwd() + '/' 
data_path = os.path.join(HERE, 'data/SampleData.xlsx')
out_tweets_path = os.path.join(HERE, 'data/tweets.txt')
out_lookup_path = os.path.join(HERE, 'data/lookup_list.txt')
out_conll_path = os.path.join(HERE, 'data/joint.trian.3')

def create_dict_data(xls):
    sheet_names = ['Ahmed', 'Omar', 'Sara', 'Ghassan']
    seg_correct_dict = {}

    for sheet_name in sheet_names:
        df = pd.read_excel(xls, sheet_name)
        df.name = sheet_name
        Freq = df['Freq']
        Word = df['Word']
        Segments = df['Segments']
        Corrections = df['Corrections']
        for correct, seg in zip(Corrections, Segments):
            correct = str(correct).strip()
            seg = str(seg).strip()
            if correct != "nan":
                if seg not in seg_correct_dict:
                    seg_correct_dict[seg] = correct
    return seg_correct_dict

def create_correct_tweets(xls, correct_dict):
    tweets = []
    Data_df = pd.read_excel(xls, 'Data')
    for twet in Data_df['Tweet']:
        text = str(twet).strip().split(' ')
        t = ''
        for word in text:
            if word in correct_dict:
                word = correct_dict[word]
            t += word + ' '

        tweets.append(t.strip())
    return tweets

def convertTrainingData(infile, outfile,  append=False):
    fp = codecs.open(infile, 'r','utf-8')
    if append:
        output_file = open(outfile, "a")
    else:
        output_file= open(outfile, "w+")

    for line in fp:
        line = line.strip()
        #print('In:',line)
        if('<EOTWEET>' in line): #EOS
            output_file.write(''+'\n')
            #print('')
            continue
        for word in line.split():
            for elt in word.split('+'):
                if(len(elt)==1):
                    output_file.write(elt+'\t'+'S'+'\n')
                    #print(elt+'\t'+'S')
                elif(len(elt)>=2):
                    output_file.write(elt[0]+'\t'+'B'+'\n')
                    #print(elt[0]+'\t'+'B')
                    for i in range(1, len(elt)-1):
                        output_file.write(elt[i]+'\tM'+'\n')
                        #print(elt[i]+'\tM')
                    output_file.write(elt[-1]+'\t'+'E'+'\n')
                    #print(elt[-1]+'\t'+'E')
            output_file.write('WB\tWB'+'\n')
        #print('WB\tWB')
    fp.close()
    output_file.close()

if __name__ == '__main__':
    write_lookup = True
    data_2_conll = True
    append = True

    xls = pd.ExcelFile(data_path)
    seg_correct_dict = create_dict_data(xls)
    corrected_tweets =  create_correct_tweets(xls, seg_correct_dict)

    # Write corrected tweets to new file
    f= open(out_tweets_path,"w+")
    for tweet in corrected_tweets:
        f.write(tweet + '\n')
    f.close()  

    # Write lookup list to new file
    if write_lookup:
        lookup_list = set(seg_correct_dict.values())
        if append:
            f= open(out_lookup_path, "a")
        else:
            f= open(out_lookup_path, "w+")
        for word in lookup_list:
            f.write(word + '\n')
        f.close()  

    # Write converted conll data to new file
    if data_2_conll:
        convertTrainingData(out_tweets_path, out_conll_path, append=True)