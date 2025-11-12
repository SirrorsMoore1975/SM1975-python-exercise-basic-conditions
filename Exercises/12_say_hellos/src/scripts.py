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
        def check_lang_list(lang_list):
            for z in lang_list:
                if isinstance(z, dict):
                    for key, value in z.items():
                        if lang == key:
                            return value
            return None
        check_list = [self.data, self.additional_lang]
        for i in check_list:
            result = check_lang_list(i)
            if result is not None:
                return result
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
    
    def add_hello(self, add_lang:str, hello_msg:str) -> None:
        # YOUR CODE HERE
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
        return None
    
    def reset_hello(self, remove_lang:str)-> None:
        # YOUR CODE HERE
        remove_lang = remove_lang.lower()
        for idx,y in enumerate(self.additional_lang):
            for key, _ in y.items():
                if key == remove_lang:
                    del self.additional_lang[idx]
                    return None
        print(f'{remove_lang} not found. No language has reset.')
        return None
    
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
    