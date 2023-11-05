"""
    mockdata.py\n
    Stores hardcoded data generated from our ML model about collision risk. If our app were extended, we would use ssh between this Flask application and the remote model to link both.
"""

# Tiny demo sample data: 2 risky locations in the NY metro area.
MOCK_DATA = [
    {
        'lat': -73.943695,
        'lon': 40.649990,
        'risk': 0.83 
    },
    {
        'lat': -73.931510,
        'lon': 40.680164,
        'risk': 0.97
    }
]

# Placeholder data sent on bad requests such as invalid action code or not JSON.
DEFAULT_ERR_DATA = {'ok': False, 'msg': 'Invalid request.'}
