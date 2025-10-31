"""
   test script for say_hellos
"""
import os
import json
import pytest
from src.scripts import Greetings

# self-test
cwd = os.getcwd()
print(f'current path: {cwd}')


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

with open("languages.json", "r", encoding="utf-8") as reading_list:
    # payload = json.load(reading_list)
    # main_lang_list = payload
    main_lang_list = json.load(reading_list)
    
with open("test_languages.json","r", encoding="utf-8") as add_languages_list:
    additional_lang_list = json.load(add_languages_list)

with open("update_languages.json", "r", encoding="utf-8") as update_languages_list:
    latest_add_lang_list = json.load(update_languages_list)

languages = [str(item.keys()) for item in main_lang_list]
hellos = [str(item.values()) for item in main_lang_list]

# self-test
print("languages\n",languages,"\nhellos\n",hellos)

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

# @pytest.fixture(scope="module")
# def my_greeting_instance():
#     instance = Greetings()
#     for key,value in additional_lang_list:
#         Greetings().add_hello(key,value)
#     return instance

@pytest.mark.parametrize("candidate_index,expected",[
    (0,"Kumusta ka na? Lara."),
    (1,"Pehea 'oe? Gentle."),
    (2,"Koj nyob li cas lawm? Alyx."),
    (3,"Bawo ni o se wa? Ramsey."),
    (4,"Bix a beel? Clinton."),
    (5,"Xi modo nuulu? Walter.")
])

def test_add_language(candidate_index,expected):
    """ 
    The test for add language. 
    This test will test the class when new language has been added.
    After the test is completed, the new added languages add should be forgotten (this will required next test to check)

    Args:
        candidate_index (_type_): _the index number of users_payload_two (int)_
        expected (_type_): _the expected answer (str)_
    """
    
    def before_test():
        for i in additional_lang_list:
            for key, value in i.items():
                Greetings().add_hello(key,value)

    def after_test():
        Greetings().reset_all_hellos()

    def test_add_cases():
        person=users_payload_two[candidate_index][USERNAME]
        lang_use=users_payload_two[candidate_index][LANGUAGE]
        result = Greetings().say_hellos(person, lang_use)
        assert result == expected

    before_test() # setup test for add new language 
    test_add_cases() # The test itself
    after_test() # reset and remove added languages

# @pytest.mark.parametrize("candidate_index,expected",[
#     (0,"Ogenkidesuka? Karen-san."),
#     (1,"Ce mai faceți? Robert."),
#     (2,"How are you? Quentin."),
#     (3,"Nǐ hǎo ma? Issac."),
#     (4,"Howzit? Charlie."),
#     (5,"Kuidas sul läheb? Lopez.")
# ])
