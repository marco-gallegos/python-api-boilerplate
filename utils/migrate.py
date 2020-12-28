"""
"""
from config.ORM import db
from model import User

models_to_migrate = [User]

def migrate()->bool:
    """Migrate models

    Returns:
        bool: migration status
    """
    status=False
    try:
        db.create_tables(models_to_migrate)
        status=True
    except:
        status=False
    return status