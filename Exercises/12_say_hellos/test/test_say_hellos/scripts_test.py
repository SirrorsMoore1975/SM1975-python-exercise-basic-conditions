"""
   test script for say_hellos
"""
import json
import pytest
from src.scripts import Greetings

my_greeting_class = Greetings()

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
HAKKA="hakka"

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
            my_greeting_class.add_hello(key,value)
            
def update_language():
    for i in latest_add_lang_list:
        for key, value in i.items():
            my_greeting_class.amend_hello(key,value)
    return None

def reset_language(lang):
    my_greeting_class.reset_hello(lang)
    return None

def reset_all_language():
    my_greeting_class.reset_all_hellos()
    return None
    
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
    result = my_greeting_class.say_hellos(person, lang_use)
    assert result == expected

@pytest.mark.parametrize("candidate_index,add_lang,expected_one, expected_two",[
    (0,FILIPINO,"Kumusta ka na? Lara.","How are you? Lara."),
    (1,HAWAIIAN,"Pehea 'oe? Gentle.", "How are you? Gentle."),
    (2,HMONG_DAW,"Koj nyob li cas lawm? Alyx.", "How are you? Alyx."),
    (3,YORUBA,"Bawo ni o se wa? Ramsey.", "How are you? Ramsey."),
    (4,YUCATEC_MAYA,"Bix a beel? Clinton.", "How are you? Clinton."),
    (5,ZAPOTEC,"Xi modo nuulu? Walter.", "How are you? Walter.")
])

def test_add_and_reset_language(candidate_index,add_lang,expected_one, expected_two):
    """
        pytest for add and remove language
    """
    test_lang = search_lang_hello(additional_lang_list,add_lang)
    my_greeting_class.add_hello(add_lang, test_lang[add_lang])
    person=users_payload_two[candidate_index][USERNAME]
    lang_use=users_payload_two[candidate_index][LANGUAGE]
    result = my_greeting_class.say_hellos(person, lang_use)
    assert result == expected_one
    my_greeting_class.reset_hello(add_lang)
    result = my_greeting_class.say_hellos(person, lang_use)
    assert result == expected_two

@pytest.mark.parametrize("lang, add_msg, person, expected",[
    (TAIWANESE,"Ni Hao Ma?","Xiao Mei", "Nǐ hǎo ma? Xiao Mei."),
    (HAKKA,"Ng3 Ho4 Ma3 ?", "MeiLing", "ng3 ho4 ma3 ? MeiLing."),
    (JAPANESE,"Ohayogozaimasu?", "Sayori", "Kohnichiwa? Sayori-san."),
    (ESTONIAN,"Kuidas sul läheb?", "Mark", "Kuidas läheb? Mark.")
])
def test_existed_lang_not_addible(lang, add_msg, person, expected):
    """
        _existed language cannot be add_

    Args:
        lang (_type_): _description_
        add_msg (_type_): _description_
        person (_type_): _description_
        expected (_type_): _description_
    """
    my_greeting_class.add_hello(lang,add_msg)
    result=my_greeting_class.say_hellos(person,lang)
    assert result == expected, "add hello to an existing language cannot change the language hello"
    my_greeting_class.reset_hello(lang)
    result=my_greeting_class.say_hellos(person,lang)
    assert result == expected, "reset to a language hello should caused no effect at all"
    