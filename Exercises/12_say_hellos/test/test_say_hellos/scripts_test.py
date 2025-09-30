import pytest, os, json
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

def test_greetings_languages():
    pass

def test_greetings_no_alter():
    for lang in main_lang_list:
        print(lang)
    

def creating_message_to_greet(name, lang):
    pass


def amend_legal_age(age):
    pass


@pytest.mark.parametrize('legal_age,expected',[(18,19,20,21,22,23)])

def test_say_hellos(input, expected):
    
    result=Greetings.say_hellos(input)
    assert result == expected
