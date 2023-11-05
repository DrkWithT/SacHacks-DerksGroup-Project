"""
    loadenv.py\n
    Loads environment secrets like the Maps key.
"""

from dotenv import get_key

MAPS_API_KEY: str = get_key('./.env', 'MAPS_KEY')
