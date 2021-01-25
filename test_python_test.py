# Imports
import pytest
from python_test import JsonReader



# Test Functions
@pytest.fixture(scope='module')
def data():
    print("---- setup ----")
    json_reader = JsonReader()
    data = json_reader.read_file('data.txt')
    yield data
    print("---- teardown ----")
    # -- close database in case of real implementation


@pytest.mark.parametrize('command_name, result',[
    ("parse", [{'function': 'parse', 'help': 'file help', 'value': 'file'}]),
    ("copy", [{'function': 'copy', 'help': 'copy help', 'value': 'file'}])
])
def test_get_commands(command_name, result, data):
    json_reader = JsonReader()
    commands = json_reader.get_specific_commands(data, command_name)
    assert commands == result

def test_functional_list_concatenation(data):
    json_reader = JsonReader()

    # fetching specific command lists
    parse_commands = json_reader.get_specific_commands(data, 'parse')
    copy_commands = json_reader.get_specific_commands(data, 'copy')

    # applying _list and _counter mods to lists
    parse_commands_mod = json_reader.apply_list_mod(parse_commands)
    copy_commands_mod = json_reader.apply_list_mod(copy_commands)

    # concatenating lists
    functional_commands = parse_commands_mod + copy_commands_mod

    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]


def test_random_sampling(data):
    json_reader = JsonReader()
    random_commands = json_reader.get_random_commands(data, 2)
    assert len(random_commands) == 2
