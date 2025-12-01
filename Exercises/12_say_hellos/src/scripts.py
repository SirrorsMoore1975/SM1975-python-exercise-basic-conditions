"""
    _SOLUTION BRANCH_
"""
import json

class Greetings:
    """
        class Greetings
    """
    def __init__(self):
        # YOUR CODE HERE
        with open("languages.json", "r", encoding="utf-8") as lang_json:
            self.data = json.load(lang_json)
        if not isinstance(self.data, list):
            print(ValueError("the json file is not a list"))
        self.additional_lang=[]
        self.default_age = 20

    def return_hellos(self,lang:str) -> str:
        """
            Helper function helping say_hellos
        """
        lang = lang.lower()
        def check_lang_list(lang_list):
            for z in lang_list:
                if isinstance(z, dict):
                    for key, value in z.items():
                        if lang == key:
                            return value
            return None
        check_list = [self.additional_lang, self.data]
        for i in check_list:
            result = check_lang_list(i)
            if result is not None:
                return result
        return "How are you?"

    def say_hellos(self, person:str="Anonymous", lang:str="british_english")->str:
        # YOUR CODE HERE
        """
            _The class function that return the hello of a given language_

        Args:
            person (str): _The name of the person who the script shall address to. Default: "Anonymous"._
            lang (str): _The language to greet, if supported, to the person. Default: "british_english"._

        Returns:
            (dict): _return the greeting statement address to the given person on that given language, if available,_
        """
        JAPANESE="japanese"

        lang = lang.lower()
        if lang == JAPANESE:
            person = person + "-san"
        return f"{self.return_hellos(lang)} {person}."

    def amend_hello(self, amend_lang:str, amend_hello:str):
        # YOUR CODE HERE
        """
            _amend or amend added hello of a language_
        """
        amend_lang = amend_lang.lower()
        for data in self.additional_lang:
            for key, value in data.items():
                if amend_lang == key:
                    data[key] = amend_hello
                    print(f'amend_hello: {amend_lang} hello {value} has changed to {amend_hello}')
                    return None
        for the_data in self.data:
            for key, value in the_data.items():
                if amend_lang == key:
                    self.additional_lang.append({ key : amend_hello })
                    print(f'amend_hello: {amend_lang} hello {value} has changed to {amend_hello}')
                    return None
        print(f'amend_hello: No matching {amend_hello} found. use add_hellos')
        return None

    def add_hello(self, add_lang:str, hello_msg:str) -> None:
        # YOUR CODE HERE
        """
            _Add hello to a specified language with the hello message. 
            The script should accept one entry. 
            Further same language will not write to the given class. 
            If required amendment to the language, use amend_hello instead._

        Args:
            add_lang (str): _add language into the class_
            hello_msg (str): _add hello message to that language_

        Returns:
            _None_type_: _None is expected_
        """
        result = {}
        add_lang = add_lang.lower()
        def check_repeat(lang_list):
            for z in lang_list:
                if isinstance(z, dict):
                    for key, _ in z.items():
                        if key == add_lang:
                            return True
            return False
        check_list = [self.data,self.additional_lang]
        for i in check_list:
            result = check_repeat(i)
            if result:
                return None
        result = {add_lang:hello_msg}
        self.additional_lang.append(result)

    def reset_hello(self, remove_lang:str)-> None:
        # YOUR CODE HERE
        """
            _reset the added or amended specific language_
        """
        remove_lang = remove_lang.lower()
        for idx,y in enumerate(self.additional_lang):
            for key, _ in y.items():
                if key == remove_lang:
                    del self.additional_lang[idx]
                    return None
        print(f'reset_hello: {remove_lang} not found. No language has been reset.')
        return None
    
    def reset_all_hellos(self) -> None:
        # YOUR CODE HERE
        """
            _Reset all hellos_
        """
        self.additional_lang = []
        print("reset_all_hellos: All added hellos are removed and back to default.")

    def is_adult(self, age: int = 20) -> bool:
        # YOUR CODE HERE
        """
            _returns True if the age is adult, or else False_
        """
        print(f"is_adult: age checking for {age}")
        return age >= self.default_age

    def amend_adult_age(self, age :int = 20) -> None:
        # YOUR CODE HERE
        """
            _amend legal adult age_
        """
        self.default_age = age
        print(f"amend_adult_age: legal adult age changed to {age}")

    def reset_adult_age(self) -> None:
        # YOUR CODE HERE
        """
            _reset adult age to default 20_
        """
        self.default_age = 20
        print("reset_adult_age:")
        print("legal adult age changed back to 20")

    def reset_to_default(self) -> None:
        # YOUR CODE HERE
        """
            _reset legal adult age to 20 and remove all add and amended additional language_
        """
        self.default_age = 20
        self.additional_lang = []
        print("reset_to_default:")
        print("reset adult age: 20")
        print("reset add and amended language back to default")
    