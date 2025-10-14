import json

class Greetings:
    """
    class Greetings
    """
    def __init__(self) -> str :
        # YOUR CODE HERE
        with open("languages.json", "r", encoding="utf-8") as lang_json:
            self.df_lang_list = json.load(lang_json)
        if not isinstance(self.df_lang_list, list):
            return ValueError("the json file is not a list")
        self.lang_available = []
        for x in self.df_lang_list:
            self.lang_available = [str(z.keys()) for z in x if z.keys() not in self.lang_available]
        # for each_lang in self.df_lang_list:
        #     if self.df_lang_list[each_lang] == 
        #     self.lang_list = [] + [str(x.keys()) for x in each_lang]
        
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
            return f"{self.df_lang_list[lang]} {person}."
        return f"{self.df_lang_list[self.default_lang]} {person}."
    
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
    