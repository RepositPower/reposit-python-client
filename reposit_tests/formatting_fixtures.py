summary_response = {
    'data': {
        'battery': {
            'state': 'ONLINE',
            'val': 2.0
        },
        'grid': {
            'state': 'ONLINE',
            'val': 40.0,
            'something_else': 'not_included'
        },
        'house': {
            'state': 'ONLINE',
            'val': 25.0
        },
        'solar': {
            'state': 'ONLINE',
            'val': 30.0,
            'other_key': 'blah'
        },
        'key5': {
            'this_isnt': 'included'
        }
    }
}

expected = {
    'battery': {
        'state': 'ONLINE',
        'value': 2.0
    },
    'grid': {
        'state': 'ONLINE',
        'value': 40.0
    },
    'house': {
        'state': 'ONLINE',
        'value': 25.0
    },
    'solar': {
        'state': 'ONLINE',
        'value': 30.0
    },
}

summary_response_2 = {
    'data': {
        'battery': {
            'state': 'ONLINE',
            'val': 2.0
        },
        'grid': {
            'state': 'ONLINE',
            'val': 40.0,
            'something_else': 'not_included'
        }
    }
}

expected_2 = {
    'battery': {
        'state': 'ONLINE',
        'value': 2.0
    },
    'grid': {
        'state': 'ONLINE',
        'value': 40.0
    }
}