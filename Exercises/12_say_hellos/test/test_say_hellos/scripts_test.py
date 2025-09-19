import pytest
from src.scripts import say_hellos

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

def creating_message_to_greet(name, lang):
    pass


def amend_legal_age(age):
    pass


pytest.mark.parametrize('input,expected',[()])

def test_say_hellos(input, expected):
    
    result=say_hellos(input)
    assert result == expected
