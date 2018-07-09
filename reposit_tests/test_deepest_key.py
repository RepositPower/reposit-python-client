import pytest

from reposit.data.utils import deepest_key

three_levels = {
    'level1': {
        'level2': {
            'level3': {}
        }
    }
}

single_level = {
    'level1': {}
}

two_levels = {
    'level1': {
        'level2': {}
    }
}


@pytest.mark.parametrize('_dict, expected', [
    (single_level, 'level1'),
    (two_levels, 'level2'),
    (three_levels, 'level3'),
])
def test_deepest_key_func(_dict, expected):
    assert deepest_key(_dict) == expected
