import json

class Greetings:
    """
    class Greetings
    """
    def __init__(self):
        # YOUR CODE HERE
        #ENGLISH="english_british"
        #self.default_lang = ENGLISH
        with open("languages.json", "r", encoding="utf-8") as lang_json:
            self.data = json.load(lang_json)
        if not isinstance(self.data, list):
            print(ValueError("the json file is not a list"))
        self.additional_lang=[]
        #self.default_hello = self.return_hellos(ENGLISH)
        # unique_keys = set()
        # for item in self.data:
        #     unique_keys.update(item.keys())
        #     if item.keys() == ENGLISH:
        #         self.default_hello = item.values()
        # self.unique_lang_list = list(str(unique_keys))
        # for each_lang in self.df_lang_list:
        #     if self.df_lang_list[each_lang] == 
        #     self.lang_list = [] + [str(x.keys()) for x in each_lang]
    
    def return_hellos(self,lang:str) -> str:
        lang = lang.lower()
        for y in self.data:
            for key,value in y.items():
                if lang == key:
                    return value
        for x in self.additional_lang:
            for key,value in x.items():
                if lang == key:
                    return value
        return "How are you?"
        
    def say_hellos(self, person:str="Anonymous", lang:str="british_english")->str:
        # YOUR CODE HERE
        JAPANESE="japanese"
        
        lang = lang.lower()
        if lang == JAPANESE:
            person = person + "-san"
        return f"{self.return_hellos(lang)} {person}."
    
    def amend_hello(self):
        # YOUR CODE HERE
        pass
    
    def add_hello(self, add_lang, hello_msg):
        # YOUR CODE HERE
        for y in self.additional_lang:
            for key, value in y.items():
                if key == add_lang:
                    if value == hello_msg:
                        print(f'{add_lang}:{value} has already existed. Action Abort.')
                        return False
                print(f'Entries: {add_lang}:{hello_msg} already existed. If you need to amend, use amend_hello instead. Action Abort.')
                return False
        self.additional_lang.append({add_lang:hello_msg})
        print(f'{add_lang}:{hello_msg} add into self.additional_lang')
        return True
    
    def reset_hello(self, remove_lang):
        # YOUR CODE HERE
        for idx,y in enumerate(self.additional_lang):
            for key, _ in y.items():
                if key == remove_lang:
                    del self.additional_lang[idx]
                    return True
        return False
    
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
    