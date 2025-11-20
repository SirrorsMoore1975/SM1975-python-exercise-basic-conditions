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
HAKKA="hakka"

@pytest.fixture(scope="module")
def setup_environment():
    my_greeting_class = Greetings()
    add_lang_list = data_list("test_languages.json")
    
    for lang_data in add_lang_list:
        for key, value in lang_data.items():
            my_greeting_class.add_hello(key,value)
    
    yield my_greeting_class
    
    my_greeting_class.reset_all_hellos()
    
def data_list(database_json):
    with open(database_json, "r", encoding="utf-8") as the_data_list:
        return json.load(the_data_list)

def search_lang_hello(lang_list,lang):
    for y in lang_list:
        for keys, value in y.items():
            if keys == lang:
                return {f"{keys}":f"{value}"}
    return {f"{lang}":"How are you?"}


@pytest.mark.parametrize("lang",[
    (FILIPINO),
    (HAWAIIAN),
    (HMONG_DAW),
    (YORUBA),
    (YUCATEC_MAYA),
    (ZAPOTEC)
])
def test_amend_lang_and_reset(setup_environment,lang):
    my_greeting_class = setup_environment
    result = my_greeting_class.say_hellos("Mark", lang)
    expected = f'{search_lang_hello(data_list("test_languages.json"),lang)[lang]} Mark.'
    assert result == expected, ""
    