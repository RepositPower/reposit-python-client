"""
Test the data formatting functions
"""
import pytest

from reposit.data.utils import format_summary_response
from reposit_tests.formatting_fixtures import expected, summary_response, summary_response_2, expected_2


@pytest.mark.parametrize('data, expected_data', [
    (summary_response, expected),
    (summary_response_2, expected_2),
])
def test_format_summary(data, expected_data):
    assert format_summary_response(data) == expected_data
