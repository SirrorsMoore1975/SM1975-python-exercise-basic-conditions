import pytest
import json
from src.scripts import Greetings

USERNAME="username"
AGE="age"
LANGUAGE="language"
ESTONIAN="estonian"
FILIPINO="filipino"
HAWAIIAN="hawaiian"
JAPANESE="japanese"
ROMANIAN="romanian"
TAIWANESE="taiwanese_chinese"

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

with open("../test/test_say_hellos/languages.json", "r", encoding="utf-8") as reading_list:
    # payload = json.load(reading_list)
    # main_lang_list = payload
    main_lang_list = json.load(reading_list)

def creating_message_to_greet(name, lang):
    pass


def amend_legal_age(age):
    pass


@pytest.mark.parametrize('legal_age,expected',[(18,19,20,21,22,23)])

def test_say_hellos(input, expected):
    
    result=Greetings.say_hellos(input)
    assert result == expected
