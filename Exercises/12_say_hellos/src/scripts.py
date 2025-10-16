import json

class Greetings:
    """
    class Greetings
    """
    def __init__(self) -> str :
        # YOUR CODE HERE
        ENGLISH="english_british"
        self.default_lang = ENGLISH
        with open("languages.json", "r", encoding="utf-8") as lang_json:
            self.data = json.load(lang_json)
        if not isinstance(self.data, list):
            print(ValueError("the json file is not a list"))
        
        unique_keys = set()
        for item in self.data:
            unique_keys.update(item.keys())
            if item.keys() == ENGLISH:
                self.default_hello = item.values()
        self.unique_lang_list = list(str(unique_keys))
        # for each_lang in self.df_lang_list:
        #     if self.df_lang_list[each_lang] == 
        #     self.lang_list = [] + [str(x.keys()) for x in each_lang]
    
    def return_hellos(self,lang:str) -> str:
        lang = lang.lower()
        for y in self.data:
            for x in y:
                if lang == x.keys():
                    return x.values()
        return self.default_hello
        
    def say_hellos(self, person:str, lang:str)->str:
        # YOUR CODE HERE
        JAPANESE="japanese"
        print(self.return_hellos(lang))
        if not lang:
            lang = self.default_lang
        lang = lang.lower()
        if lang == JAPANESE:
            person = person + "-san"
        if self.unique_lang_list in lang:
            for item in self.data:
                if item.keys() == lang:
                    return f"{item[lang]} {person}."
        return f"{self.default_hello} {person}."
    
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
    