from FarasaPy3.api import FarasaPy3

class FarasaTest():
    def __init__(self):
        self.text = "بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام"
        self.farasaApi = FarasaPy3()
    
    def test_segmentation():
        assert self.farasaApi.Segmentation(text) == "بلاد+ي وان جار+ت على عزيز+ة و+اهلي وان ضن+وا على كرام", "incorrect Segmentation"

    def test_lemmatization():
        assert self.farasaApi.Lemmatization(text) == "بلد وان جارى على عزيز اهلي وان ضن على رام", "incorrect Lemmatization"

    def test_pos():
        assert self.farasaApi.POS(text) == "S NOUN PRON NOUN NOUN+NSUFF PREP NOUN+NSUFF CONJ NOUN NOUN V+PRON PREP NOUN E", "incorrect Lemmatization"
        
    def test_spellcheck():
        assert self.farasaApi.SpellCheck(text) == "بلادي وإن/وان جارت على عزيزة وأهلي/واهلي وإن/وان ضنوا على كرام", "incorrect Spellcheck"
        
    def test_diacritization():
        assert self.farasaApi.Diacritization(text) == "بِلادي وانْ جارَتْ عَلَى عَزيزَةٍ واهَّلي وانْ ضَنّوا عَلَى كِرامِ", "incorrect Diacritization"
        
    def test_diacritizatioV2():
        assert self.farasaApi.DiacritizationV2(text) == "بِلَادِي وَانْ جَارَتْ عَلَى عَزيزَةٍ واهَّلي وَانْ ضَنّوا عَلَى كِرامٍ", "incorrect DiacritizationV2"

    def test_dialectdiacritization():
        assert self.farasaApi.DialectDiacritization(text, "mor") == "بْلَادِي وَانْ جَارْتْ عْلَى عْزِيزَة وَاهْلِي وَانْ ضْنُّو عْلَى كَرَامْ", "incorrect DialectDiacritization"

    def test_dialectarsegmentation():
        assert self.farasaApi.DialectARSegmentation(text) == "بلاد+ي و+ان جار+ت على عزيز+ة و+اهل+ي و+ان ضن+وا على كرام", "incorrect DialectARSegmentation"
