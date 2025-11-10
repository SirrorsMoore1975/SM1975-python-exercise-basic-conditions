"""
   test script for say_hellos
"""
import json
import pytest
from src.scripts import Greetings

USERNAME="username"
AGE="age"
LANGUAGE="language"
ESTONIAN="estonian"
FILIPINO="filipino"
HAWAIIAN="hawaiian"
HMONG_DAW="hmong_daw"
YORUBA="yoruba"
YUCATEC_MAYA="yucatec_maya"
ZAPOTEC="zapotec"
JAPANESE="japanese"
ROMANIAN="romanian"
TAIWANESE="taiwanese_chinese"

ENGLISH="english_british"

users_payload=[
    {
        USERNAME:"Karen",
        AGE:18,
        LANGUAGE:JAPANESE
    },
    {
        USERNAME:"Robert",
        AGE:23,
        LANGUAGE:ROMANIAN
    },
    {
        USERNAME:"Quentin",
        AGE:20,
        LANGUAGE:FILIPINO
    },
    {
        USERNAME:"Issac",
        AGE:22,
        LANGUAGE:TAIWANESE
    },
    {
        USERNAME:"Charlie",
        AGE:31,
        LANGUAGE:HAWAIIAN
    },
    {
        USERNAME:"Lopez",
        AGE:19,
        LANGUAGE:ESTONIAN
    }
]

users_payload_two=[
    {
        USERNAME:"Lara",
        LANGUAGE:FILIPINO
    },
    {
        USERNAME:"Gentle",
        LANGUAGE:HAWAIIAN
    },
    {
        USERNAME:"Alyx",
        LANGUAGE:HMONG_DAW
    },
    {
        USERNAME:"Ramsey",
        LANGUAGE:YORUBA
    },
    {
        USERNAME:"Clinton",
        LANGUAGE:YUCATEC_MAYA
    },
    {
        USERNAME:"Walter",
        LANGUAGE:ZAPOTEC
    }
]

legal_adult_age=[18,22,25]

# @pytest.fixture(scope="module")
def data_list(database_json):
    with open(database_json, "r", encoding="utf-8") as the_data_list:
        return json.load(the_data_list)

main_lang_list = data_list("languages.json")
additional_lang_list = data_list("test_languages.json")
latest_add_lang_list = data_list("update_languages.json")
# with open("languages.json", "r", encoding="utf-8") as reading_list:
#     main_lang_list = json.load(reading_list)
    
# with open("test_languages.json","r", encoding="utf-8") as add_languages_list:
#     additional_lang_list = json.load(add_languages_list)

# with open("update_languages.json", "r", encoding="utf-8") as update_languages_list:
#     latest_add_lang_list = json.load(update_languages_list)

def add_language():
    for i in additional_lang_list:
        for key, value in i.items():
            Greetings().add_hello(key,value)
            
def update_language():
    for i in latest_add_lang_list:
        for key, value in i.items():
            Greetings().amend_hello(key,value)

def reset_language(lang):
    Greetings.reset_hello(lang)

def reset_all_language():
    Greetings().reset_all_hellos()
    
def search_lang_hello(lang_list,lang):
    for y in lang_list:
        for keys, value in y.items():
            if keys == lang:
                return {f"{keys}":f"{value}"}
    return {f"{lang}":"How are you"}

@pytest.mark.parametrize("candidate_index,expected",[
    (0,"Kohnichiwa? Karen-san."),
    (1,"Ce mai faceți? Robert."),
    (2,"How are you? Quentin."),
    (3,"Nǐ hǎo ma? Issac."),
    (4,"How are you? Charlie."),
    (5,"Kuidas läheb? Lopez.")
])

def test_greetings_languages(candidate_index,expected):
    person=users_payload[candidate_index][USERNAME]
    lang_use=users_payload[candidate_index][LANGUAGE]
    result = Greetings().say_hellos(person, lang_use)
    assert result == expected

@pytest.mark.parametrize("candidate_index,add_lang,expected",[
    (0,FILIPINO,"Kumusta ka na? Lara."),
    (1,HAWAIIAN,"Pehea 'oe? Gentle."),
    (2,HMONG_DAW,"Koj nyob li cas lawm? Alyx."),
    (3,YORUBA,"Bawo ni o se wa? Ramsey."),
    (4,YUCATEC_MAYA,"Bix a beel? Clinton."),
    (5,ZAPOTEC,"Xi modo nuulu? Walter.")
])

def test_add_language(candidate_index,add_lang,expected):
    test_lang = search_lang_hello(additional_lang_list,add_lang)
    Greetings().add_hello(add_lang, test_lang[add_lang])
    person=users_payload_two[candidate_index][USERNAME]
    lang_use=users_payload_two[candidate_index][LANGUAGE]
    result = Greetings().say_hellos(person, lang_use)
    assert result == expected
