import requests
from io import BytesIO
from PIL import Image

class General:
    def save_image_from_url(self, url, save_path):
        response = requests.get(url)

        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return save_path
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            
            
