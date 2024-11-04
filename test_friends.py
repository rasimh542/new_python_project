import pytest
from Friends import sanitize, read_file, analyze_friends

@pytest.fixture
def mock_friends_file(tmp_path):
    # Creating a mock file for friends.txt
    friends_file = tmp_path / "friends.txt"
    friends_file.write_text("John Doe\n(555) 123-4567\nJane Smith\n(555) 987-6543\n")
    return friends_file.open()

@pytest.fixture
def mock_areacodes_file(tmp_path):
    # Creating a mock file for map_areacodes_states.txt
    areacodes_file = tmp_path / "map_areacodes_states.txt"
    areacodes_file.write_text("555\nCalifornia\n")
    return areacodes_file.open()

def test_read_file(mock_friends_file, mock_areacodes_file):
    # Testing read_file with mock files
    names, phones = read_file(mock_friends_file)
    areacodes, states = read_file(mock_areacodes_file)
    
    assert names == ("John Doe", "Jane Smith")
    assert phones == ("(555) 123-4567", "(555) 987-6543")
    assert areacodes == ("555",)
    assert states == ("California",)

def test_sanitize():
    # Testing the sanitize function
    phones = ("(555) 123-4567", "(555) 987-6543")
    expected = ("5551234567", "5559876543")
    assert sanitize(phones) == expected

def test_analyze_friends(capsys, mock_friends_file, mock_areacodes_file):
    # Testing analyze_friends with mock data
    names, phones = read_file(mock_friends_file)
    clean_phones = sanitize(phones)
    areacodes, states = read_file(mock_areacodes_file)
    
    analyze_friends(names, clean_phones, areacodes, states)
    
    captured = capsys.readouterr()
    assert "You have 2 friends!" in captured.out
    assert "Their are codes are ('555',)" in captured.out
    assert "They live in ('California',)" in captured.out
