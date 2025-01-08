import os
import requests

def get_extinction(image_url:str)-> str or None:
    excitons: list[str] = ['.jpeg', '.gif', '.svg', 'jpg', '.png']
    for ext in excitons:
        if ext in image_url:
            return ext

def download_image(image_url: str, name: str, folder:str = None,):
    if ext:= get_extinction(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image exciton could not be located') 
    
    #Check if name already exist
    if os.path.isfile(image_name):
        raise Exception('File name already exist...')
    
    #Download the image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_url: str = input('Enter a url: ')
    input_name: str = input('Enter a name: ')

    print('Downloading...')
    download_image(input_url, name=input_name, folder='images')