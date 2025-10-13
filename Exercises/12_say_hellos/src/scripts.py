import json

class Greetings:
    """
    class Greetings
    """
    def __init__(self) -> str :
        # YOUR CODE HERE
        with open("languages.json", "r", encoding="utf-8") as lang_json:
            self.default_lang_list = json.load(lang_json)
        self.lang_list = [str(key) for key, _ in self.default_lang_list.items()]
        ENGLISH="english_british"
        self.default_lang = ENGLISH
    
    def say_hellos(self, person, lang):
        # YOUR CODE HERE
        JAPANESE="japanese"
        if not lang:
            lang = self.default_lang
        lang = lang.lower()
        if lang == JAPANESE:
            person = person + "-san"
        if self.lang_list in lang:
            return f"{self.default_lang_list[lang]} {person}."
        return f"{self.default_lang_list[self.default_lang]} {person}."
    
    def amend_hello(self):
        # YOUR CODE HERE
        pass
    
    def add_hello(self):
        # YOUR CODE HERE
        pass
    
    def reset_hello(self):
        # YOUR CODE HERE
        pass
    
    def reset_all_hellos(self):
        # YOUR CODE HERE
        pass
    
    def is_adult(self):
        # YOUR CODE HERE
        pass
    
    def amend_adult_age(self):
        # YOUR CODE HERE
        pass
    
    def reset_adult_age(self):
        # YOUR CODE HERE
        pass
    
    def reset_to_default(self):
        # YOUR CODE HERE
        pass
    