import os 
import shutil


# Functions for creating and deleting 
def create_img_dir(): 
    # Create folder where image objects (charts and tables) will be stored
    img_path = 'resources/image_dir/image_dump/'
    if not os.path.exists(img_path):
        os.mkdir(img_path)
        print(f'Created dir to dump images at: {img_path}')
    else: 
        print('Imgdump Path already exists.')
    
    return img_path

def delete_img_dir(del_image_dir:bool): 
    if del_image_dir: 
        print('Deleting image dir ->', end= ' ')
        shutil.rmtree('resources/image_dir/image_dump/')
    else: 
        print('Did not delete image dir. See "resources/image_dir/image_dump/" for raw images.')
    print('Done.')