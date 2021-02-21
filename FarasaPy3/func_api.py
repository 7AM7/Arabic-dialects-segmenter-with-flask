import requests, json
import re

farasa_url = 'https://farasa-api.qcri.org'

apis_list = {
            "Segmentation": {'url':"/msa/webapi/segmenter", }, 
            "Lemmatization": {'url':"/msa/webapi/lemma", }, 
            "POS":  {'url':"/msa/webapi/pos", }, 
            "SpellChecker":  {'url':"/msa/webapi/spellcheck",}, 
            "Diacritization":  {'url':"/msa/webapi/diacritize", }, 
            "DiacritizationV2":  {'url':"/msa/webapi/diacritizeV2", },
        }

def FarasaAPIs(url, apiName, params, dict_only=False):
    headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
    response = requests.get(url + apiName, params=params, headers=headers)
    if dict_only:
        match_result = re.match('{[^{]+?}',  response.text)
        if match_result:
            result = json.loads(match_result.group())
    else:
        result = json.loads(response.text)
    return result

def Segmentation(text):
    params = {'text': text}
    segmenter = FarasaAPIs(farasa_url, apis_list['Segmentation']['url'], params)
    result = segmenter['segtext']
    result = ' '.join(result)
    return result

def Lemmatization(text):
    params = {'text': text}
    lemma = FarasaAPIs(farasa_url, apis_list['Lemmatization']['url'], params)
    result = lemma['result']
    result = ' '.join(result)
    return result

def POS(text):
    params = {'text': text}
    pos = FarasaAPIs(farasa_url, apis_list['POS']['url'], params)
    result = []
    for value in pos:
        result.append(value['POS'])
    result = ' '.join(result)
    return result
    
def SpellCheck(text):
    params = {'text': text}
    spellcheck = FarasaAPIs(farasa_url, apis_list['SpellChecker']['url'], params)
    result = spellcheck['result']
    return result

def Diacritization(text):
    params = {'text': text}
    diacritize = FarasaAPIs(farasa_url, apis_list['Diacritization']['url'], params)
    result = diacritize['output']
    return result

def DiacritizationV2(text):
    params = {'text': text}
    diacritizeV2 = FarasaAPIs(farasa_url, apis_list['DiacritizationV2']['url'], params)
    result = diacritizeV2['output']
    return result

def DialectDiacritization(text, dialect):
    params = {"dialect":dialect, "content":text}
    dialectDiacritize = FarasaAPIs("http://40.115.122.93/demo/", "diacritization_api?", params, dict_only=True)
    dialect = dialectDiacritize['dialect']
    return text


def DialectARSegmentation(self, text):
    params = {"text": text}
    dialectARSegmentation = FarasaAPIs("https://farasa.herokuapp.com/", "DialectalARSeg?", params, dict_only=True)
    text = dialectARSegmentation['result']
    return text