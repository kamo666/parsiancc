class MakeListofDicts:
    def extractKeys(self, input_str):
        Keys = input_str.split("\n")[0].split("|")
        return Keys

    def extractValues(self, input_str,n):
        if n == 1:
           list_of_Values = input_str.split("\n")[1:-3]
        elif n == 0:
           list_of_Values = input_str.split("\n")[1:-2]
        Values = [item.split("|") for item in list_of_Values]
        return Values

    def assignKeyValues(self, Keys, Values):
        list_of_dicts = []
        template = {}
        for value_index, value in enumerate(Values):
            for key_index, key in enumerate(Keys):
                template[key] = value[key_index]
            list_of_dicts.append(template)
            template = {}
        return list_of_dicts
