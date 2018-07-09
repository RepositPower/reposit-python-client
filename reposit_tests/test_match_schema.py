import pytest

from reposit.data.utils import match_to_schema

key_1 = 'inverterP'

data_1 = {
    'data': {
        'inverterP': 40.0
    }
}

key_2 = 'houseP'

data_2 = {
    'houseP': 50.00
}

key_3 = 'blah2'

data_3 = {
    'data': {
        'generation': {
            'some_data': {
                'blah': 2,
                'blah2': 1,
                'blah3': 40,
            }
        }
    }
}


@pytest.mark.parametrize('_dict, requested_key, expected', [
    (data_1, key_1, 40.0),
    (data_2, key_2, 50.0),
    (data_3, key_3, 1),
])
def test_match_schema_func(_dict, requested_key, expected):
    assert match_to_schema(_dict, requested_key) == expected
