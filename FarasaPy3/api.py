import requests, json
import re
from constants import farasa_url, apis_list

class FarasaPy3(object):
    def __init__(self):
        pass

    def FarasaAPIs(self, url, apiName, params, dict_only=False):
        headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
        response = requests.get(url + apiName, params=params, headers=headers)
        if dict_only:
            match_result = re.match('{[^{]+?}',  response.text)
            if match_result:
                result = json.loads(match_result.group())
        else:
            result = json.loads(response.text)
        return result

    def Segmentation(self, text):
        params = {'text': text}
        segmenter = self.FarasaAPIs(farasa_url, apis_list['Segmentation']['url'], params)
        result = segmenter['segtext']
        result = ' '.join(result)
        return result

    def Lemmatization(self, text):
        params = {'text': text}
        lemma = self.FarasaAPIs(farasa_url, apis_list['Lemmatization']['url'], params)
        result = lemma['result']
        result = ' '.join(result)
        return result

    def POS(self, text):
        params = {'text': text}
        pos = self.FarasaAPIs(farasa_url, apis_list['POS']['url'], params)
        result = []
        for value in pos:
            result.append(value['POS'])
        result = ' '.join(result)
        return result
        
    def SpellCheck(self, text):
        params = {'text': text}
        spellcheck = self.FarasaAPIs(farasa_url, apis_list['SpellChecker']['url'], params)
        result = spellcheck['result']
        return result

    def Diacritization(self, text):
        params = {'text': text}
        diacritize = self.FarasaAPIs(farasa_url, apis_list['Diacritization']['url'], params)
        result = diacritize['output']
        return result

    def DiacritizationV2(self, text):
        params = {'text': text}
        diacritizeV2 = self.FarasaAPIs(farasa_url, apis_list['DiacritizationV2']['url'], params)
        result = diacritizeV2['output']
        return result

    def DialectDiacritization(self, text, dialect):
        params = {"dialect":dialect, "content":text}
        dialectDiacritize = self.FarasaAPIs("http://40.115.122.93/demo/", "diacritization_api?", params, dict_only=True)
        text = dialectDiacritize['res']
        return text

    def DialectARSegmentation(self, text):
        params = {"text": text}
        dialectARSegmentation = self.FarasaAPIs("https://farasa.herokuapp.com/", "DialectalARSeg?", params, dict_only=True)
        text = dialectARSegmentation['result']
        return text
