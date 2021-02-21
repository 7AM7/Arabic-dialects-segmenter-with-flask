# Farasa Python API V3.0.0
  Farasa (which means “insight” in Arabic), is a fast and accurate text processing toolkit for Arabic text. Farasa can do segmentation, lemmatization, POS tagging, Arabic diacritization, dependency parsing, constituency parsing, named-entity recognition, and spell-checking.

# Installation:

`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps FarasaPy3`

# Features
  - Segmentation
  - Lemmatization
  - Spell Checker
  - POS Tagging
  - Diacritization
  - DiacritizationV2
  - Dialect Diacritization

# Usage:
  1- Segmentation
  ```
      from FarasaPy3.api import FarasaPy3
      farasaApi = FarasaPy3()
      result = farasaApi.Segmentation(text)
      print(result)
  ```
  2- Lemmatization
  ```
    from FarasaPy3.api import FarasaPy3
    farasaApi = FarasaPy3()
    result = farasaApi.Lemmatization(text)
    print(result)
  ```
  3- Spell Checker
  ```
    from FarasaPy3.api import FarasaPy3
    farasaApi = FarasaPy3()
    result = farasaApi.SpellCheck(text)
    print(result)
  ```
  4- POS
  ```
    from FarasaPy3.api import FarasaPy3
    farasaApi = FarasaPy3()
    result = farasaApi.POS(text)
    print(result)
  ```
  5- Diacritization
  ```
    from FarasaPy3.api import FarasaPy3
    farasaApi = FarasaPy3()
    result = farasaApi.Diacritization(text)
    print(result)
  ```
  6- DiacritizationV2
  ```
    from FarasaPy3.api import FarasaPy3
    farasaApi = FarasaPy3()
    result = farasaApi.DiacritizationV2(text)
    print(result)
  ```
  7- Dialect Diacritization
  ```
    from FarasaPy3.api import FarasaPy3
    farasaApi = FarasaPy3()
    dialect =  [tun,mor,msa,ca]
    result = farasaApi.DialectDiacritization(text, dialect[1])
    print(result)
  ```
# Examples to Illustrate the Functionality
  1- Segmentation
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام
  > بلاد+ي وان جار+ت على عزيز+ة و+اهلي وان ضن+وا على كرام
  ```
  2- Lemmatization
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام
  > بلد وان جارى على عزيز اهلي وان ضن على رام
  ```
  3- Spell Checker
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام
  > بلادي وإن/وان جارت على عزيزة وأهلي/واهلي وإن/وان ضنوا على كرام
  ```
 3- POS
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام
  > S NOUN PRON NOUN NOUN+NSUFF PREP NOUN+NSUFF CONJ NOUN NOUN V+PRON PREP NOUN E
  ```
  5- Diacritization
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام
  > بِلادي وانْ جارَتْ عَلَى عَزيزَةٍ واهَّلي وانْ ضَنّوا عَلَى كِرامِ
  ```
  6- DiacritizationV2
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام 
  > بِلَادِي وَانْ جَارَتْ عَلَى عَزيزَةٍ واهَّلي وَانْ ضَنّوا عَلَى كِرامٍ
  ```
  6- Dialect Diacritization (MOR)
  ```
  - بلادي وان جارت على عزيزة واهلي وان ضنوا على كرام 
  > بْلَادِي وَانْ جَارْتْ عْلَى عْزِيزَة وَاهْلِي وَانْ ضْنُّو عْلَى كَرَامْ
  ```

# References
- https://packaging.python.org/tutorials/packaging-projects/
