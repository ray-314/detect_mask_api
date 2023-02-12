"""Create keys
"""

import random
import json

def main(path: str = 'secret.json') -> None:
    """Create keys for authentication

    Args:
        path (str, optional): Path of json file to save. Defaults to 'secret.json'.
    """
    with open(path) as f:
        secret = json.load(f)

    secret['KEY'] = str(random.randint(1000000000000000, 9999999999999999))

    with open(path, 'w') as f:
        json.dump(secret, f)
    
    return None

if __name__=='__main__':
    main()