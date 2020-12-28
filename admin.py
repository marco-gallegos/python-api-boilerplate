"""
@Author Marco A. Gallegos
@Date   2020/12/26
@Update 2020/12/26
@Description
    
"""
from utils.migrate import migrate

migrated = migrate()

if migrated:
    print(f"db migrated")