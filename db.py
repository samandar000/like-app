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
    return img_table.insert(data)
    


def add_like(doc_id: str, chat_id: str) -> bool:
    '''Like image
    
    Args:
        photo_id (str): Image name
        chat_id (str): User ID
        
    Returns:
        bool: True if image was liked, False if image doesn't exist
    '''
    doc = img_table.get(doc_id=doc_id)
    if not doc:    # Check if image exists
        return False
    
    if chat_id in doc['likes']:
        return False
    
    if chat_id in doc['dislikes']:
        doc['dislikes'].remove(chat_id) 
    
    doc['likes'].append(chat_id)
    img_table.update(doc)
    
    return True


def add_dislike(doc_id: str, chat_id: str) -> bool:
    '''Like image
    
    Args:
        photo_id (str): Image name
        chat_id (str): User ID
        
    Returns:
        bool: True if image was liked, False if image doesn't exist
    '''
    doc = img_table.get(doc_id=doc_id)
    if not doc:    # Check if image exists
        return False
    
    if chat_id in doc['dislikes']:
        return False
    
    if chat_id in doc['likes']:
        doc['likes'].remove(chat_id) 
    
    doc['dislikes'].append(chat_id)
    img_table.update(doc)
    
    return True


def get_data(doc_id: str) -> dict:
    '''Get image data
    
    Args:
        photo_id (str): Image name
        
    Returns:
        dict: Image data
    '''
    photo = img_table.get(doc_id=doc_id)
    if not photo:    # Check if image exists
        return False

    return photo

add_image('test.png')
print(add_like('test.png', '4241345242314213145'))
# print(get_data('test.png'))