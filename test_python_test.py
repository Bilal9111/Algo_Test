# Imports
import pytest
from python_test import JsonReader



# Test Functions
@pytest.fixture(scope='module')
def json_reader():
    print("---- setup ----")
    json_reader = JsonReader()
    json_reader.read_file('data.txt')
    yield json_reader
    print("---- teardown ----")
    # -- close database in case of real implementation


@pytest.mark.parametrize('command_name, result',[
    ("parse", [{'function': 'parse', 'help': 'file help', 'value': 'file'}]),
    ("copy", [{'function': 'copy', 'help': 'copy help', 'value': 'file'}])
])
def test_get_commands(command_name, result, json_reader):
    commands = json_reader.get_specific_commands(command_name)
    assert commands == result

def test_functional_list_concatenation(json_reader):
    # fetching specific command lists
    parse_commands = json_reader.get_specific_commands('parse')
    copy_commands = json_reader.get_specific_commands('copy')

    # applying _list and _counter mods to lists
    parse_commands_mod = json_reader.apply_list_mod(parse_commands)
    copy_commands_mod = json_reader.apply_list_mod(copy_commands)

    # concatenating lists
    functional_commands = parse_commands_mod + copy_commands_mod

    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]


def test_random_sampling(json_reader):
    random_commands = json_reader.get_random_commands(2)
    assert len(random_commands) == 2
