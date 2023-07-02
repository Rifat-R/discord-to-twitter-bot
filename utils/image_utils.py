import requests
import shutil
import uuid



def save_image(url:str):
    res = requests.get(url, stream = True)
    file_location = f"images/{uuid.uuid4()}.png"

    if res.status_code == 200:
        with open(file_location,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_location)
        return file_location
    else:
        print('Image Couldn\'t be retrieved')
        return None
