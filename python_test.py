import json
import random



class JsonReader:
    def __init__(self):
        self.data = None

    def read_file(self, file_path: str) -> list:
        try:
            with open(file_path, 'r') as file:
                data = json.loads(file.read())
                self.data = data
        except:
            raise Exception("Error occured in reading json file.")

    

    def get_specific_commands(self, command_name: str) -> list:
        if self.data == None: raise Exception("Data class variable is set to None")
        return [elem.copy() for elem in self.data if ('function' in elem) and elem['function'] == command_name]

    def apply_list_mod(self, arr1: list) -> list:
        modded_list = []
        count = 0
        for elem in arr1: 
            elem_c = elem.copy()
            count += 1
            elem_c["_list"] = elem_c["function"]
            elem_c["_counter"] = count
            modded_list.append(elem_c)
        return modded_list

    def get_random_commands(self, numb_of_rand_samples: int) -> list:
        if self.data == None: raise Exception("Data class variable is set to None")
        return random.sample(self.data, numb_of_rand_samples)

if __name__ == '__main__':

    json_reader = JsonReader()

    # reading json file
    json_reader.read_file('data.txt')

    # fetching specific command lists
    parse_commands = json_reader.get_specific_commands('parse')
    copy_commands = json_reader.get_specific_commands('copy')

    # applying _list and _counter mods to lists
    parse_commands_mod = json_reader.apply_list_mod(parse_commands)
    copy_commands_mod = json_reader.apply_list_mod(copy_commands)

    # concatenating lists
    functional_commands = parse_commands_mod + copy_commands_mod

    # random commands
    random_commands = json_reader.get_random_commands(2)

    # Printing values
    print(parse_commands)
    print(copy_commands)
    print(parse_commands_mod)
    print(copy_commands_mod)
    print(functional_commands)
    
    print( parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}])
    print( copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}])
    print( functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}])
    print( len(random_commands) == 2)
    

