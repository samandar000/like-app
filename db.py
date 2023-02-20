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
        'likes': [],
        'dislikes': []
    }
    q = Query()
    if img_table.contains(q.photo_id == photo_id):    # Check if image already exists
        return False
    img_table.insert(data)
    return True


def like(photo_id: str, chat_id: str) -> bool:
    '''Like image
    
    Args:
        photo_id (str): Image name
        chat_id (str): User ID
        
    Returns:
        bool: True if image was liked, False if image doesn't exist
    '''
    q = Query()
    if not img_table.contains(q.photo_id == photo_id):    # Check if image exists
        return False
    
    img = img_table.get(q.photo_id == photo_id)
    if chat_id in img['likes']:
        return False
    
    if chat_id in img['dislikes']:
        img['dislikes'].remove(chat_id) 
    
    img['likes'].append(chat_id)
    img_table.update(img)
    
    return True


def dislike(photo_id: str, chat_id: str) -> bool:
    '''Like image
    
    Args:
        photo_id (str): Image name
        chat_id (str): User ID
        
    Returns:
        bool: True if image was liked, False if image doesn't exist
    '''
    q = Query()
    if not img_table.contains(q.photo_id == photo_id):    # Check if image exists
        return False
    
    img = img_table.get(q.photo_id == photo_id)
    if chat_id in img['dislikes']:
        return False
    
    if chat_id in img['likes']:
        img['likes'].remove(chat_id)
    
    img['dislikes'].append(chat_id)
    img_table.update(img)

    return True


def get_data(photo_id: str) -> dict:
    '''Get image data
    
    Args:
        photo_id (str): Image name
        
    Returns:
        dict: Image data
    '''
    q = Query()
    if not img_table.contains(q.photo_id == photo_id):    # Check if image exists
        return False
    
    img = img_table.get(q.photo_id == photo_id)
    return img

# add_image('test.png')
# # print(like('test.png', '4241345242314213145'))
print(get_data('test.png'))