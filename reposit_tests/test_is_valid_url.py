import pytest

from reposit.data.utils import is_valid_url


@pytest.mark.parametrize('url, expected', [
    ('https://www.repositpower.com', True),
    ('http://www.repositpower.com', True),
    ('://www.repositpower.com', False),
    ('://www.repositpower', False),
    ('www.repositpower', False),
])
def test_is_valid_url(url, expected):
    assert is_valid_url(url) == expected
