import pytest
from IPNBvideoembed import is_valid_url

URL_test_data = [
    ("http://pytorch.org", True),
    ("https://pytorch.org", True),
    ("http://pytorch", False),
    ("http//pytorch", False),
    ("http:/pytorch", False),
    ("http/pytorch", False),
    ("http/pytorch", False),
    ("pytorch.org", False),
    ("http://asyef/", False),
]

@pytest.mark.parametrize("url, expected", URL_test_data)
def test_is_valid_url(url, expected):
    assert is_valid_url(url) == expected
    
    