"""
   test script for say_hellos
"""
import json
import pytest
import math
import random
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
ESPERANTO="esperanto"
BOSNIAN="bosnian"
CROATIAN="croatian"
DANISH="danish"
DUTCH="dutch"

def random_integer(num: int)-> int:
    return math.floor(random.random() * (num + 1))

def data_list(database_json):
    with open(database_json, "r", encoding="utf-8") as the_data_list:
        return json.load(the_data_list)

def search_lang_hello(lang_list,lang):
    for y in lang_list:
        for keys, value in y.items():
            if keys == lang:
                return {f"{keys}":f"{value}"}
    return {f"{lang}":"How are you?"}

def test_random_existing_lang():
    # Create test dictionary
    my_greeting_class = Greetings()
    the_list = data_list("languages.json")
    for test_num in range(50):
        test_dict = the_list[random_integer(len(the_list))]
        for key, value in test_dict.items():
            person = "Marine-san" if key == JAPANESE else "Marine"
            expected = f'{value} {person}.'
            result = my_greeting_class.say_hellos(key, "Marine")
            assert result == expected, f"[{test_num}]: should show {expected} for {value}, instead show: {result}"

@pytest.mark.parametrize("lang",[
    (FILIPINO),
    (HAWAIIAN),
    (HMONG_DAW),
    (YORUBA),
    (YUCATEC_MAYA),
    (ZAPOTEC)
])

def test_not_existed_lang(lang):
    my_greeting_class = Greetings()
    result = my_greeting_class.say_hellos(lang,"Chad")
    assert result == "How are you? Chad.", "should say `How are you? Chad.` for non-existed language."

@pytest.fixture(scope="module")
def setup_environment():
    my_greeting_class = Greetings()
    add_lang_list = data_list("test_languages.json")
    
    for lang_data in add_lang_list:
        for key, value in lang_data.items():
            my_greeting_class.add_hellos(key,value)
    
    yield my_greeting_class
    
    my_greeting_class.reset_all_hellos()

@pytest.mark.parametrize("lang",[
    (FILIPINO),
    (HAWAIIAN),
    (HMONG_DAW),
    (YORUBA),
    (YUCATEC_MAYA),
    (ZAPOTEC)
])
def test_add_lang(setup_environment,lang):
    my_greeting_class = setup_environment
    result = my_greeting_class.say_hellos("Mark", lang)
    expected = f'{search_lang_hello(data_list("test_languages.json"),lang)[lang]} Mark.'
    assert result == expected, ""

@pytest.fixture(scope="module")
def setup_add_amend_language_env():
    add_amend_hello = Greetings()
    add_lang_list = data_list("test_languages.json")
    amend_lang_list = data_list("update_languages.json")
    
    for lang_data in add_lang_list:
        for key, value in lang_data.items():
            add_amend_hello.add_hello(key, value)

    for amend_lang_data in amend_lang_list:
        for key, value in amend_lang_data.items():
            add_amend_hello.amend_hello(key, value)

    yield add_amend_hello
    
    add_amend_hello.reset_all_hellos()

@pytest.mark.parametrize("lang, person",[
    (ESTONIAN, "James"),
    (JAPANESE, "James-san"),
    (HAWAIIAN, "James")
])
def test_add_amend_lang(setup_add_amend_language_env,person, lang):
    my_greeting_class = setup_add_amend_language_env
    result = my_greeting_class.say_hellos(person, lang)
    expected = f'{search_lang_hello(data_list("update_language.json"),lang)[lang]} {person}.'
    assert result == expected, "should amend the given langugage's hello"
