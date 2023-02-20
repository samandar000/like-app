from tinydb import TinyDB, Query

db = TinyDB('db.json', indent=4)

# img_table
img_table = db.table('images')


def add_image(photo_id: str) -> bool:
    '''Add image to database
    
    Args:
        image (str): Image name
        
    Returns:
        bool: True if image was added, False if image already exists
    '''
    data = {
        'photo_id': photo_id,
        'likes': []
    }
    q = Query()
    if img_table.contains(q.photo_id == photo_id):    # Check if image already exists
        return False
    img_table.insert(data)
    return True


print(add_image('test.png'))