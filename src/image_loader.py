import numpy as np
import pandas as pd
import PIL.Image as Image
from skimage.transform import resize, rescale, downscale_local_mean

class Imageset:

    sets = None
    subtype = None
    path = None
    data_images = None
    IMAGE_WIDTH = 183
    IMAGE_HEIGHT = 135
    
    
    def __init__(self, sets, subtype, path):
        self.sets = sets
        self.subtype = subtype
        self.path = path
        
        self.data_images = self.load_images_type_dim(self.sets, self.subtype, self.path)
        
    def get_subtype_df(self, set, subtype):
        """
            Returns a dataframe containing all cards of the subtype 
            given from the sets given.
        """
        data = set[set["type"].str.contains(subtype,case=False)].drop_duplicates("name")
        return data.sort_values("printings")
    
    def load_set(self, set):
        if not ".csv" in set:
            csv_file_name = "%s.csv" % set
        else:
            csv_file_name = "%s" % set
        csv_path = "../data/card_data/csv"
        csv_file_path = "%s/%s" % (csv_path, csv_file_name)

        return pd.read_csv(csv_file_path)
    
    def crop_image(self, img, cropx, cropy):
        return img[cropy[0]:cropy[1],cropx[0]:cropx[1]]
    
    def load_images_type_dim(self, sets, subtype, images_path_):
        pics = []
        x_dim = [20,203]
        for index, set in sets.iterrows():
            images_path = "%s/%s" % (images_path_, set['name'])
            y_dim = [set['Ya'],set['Yb']]

            # Load subset type cards from csv lists
            try: #Try to load the given set, if it doesn't exist, pass
                card_names = self.get_subtype_df(self.load_set(set['name']),subtype)['name'].values
                for image in card_names:
                    try:
                        im_file_name = "%s.full.jpg" % image
                        #print(set, ": ", im_file_name)
                        im_file_path = "%s/%s" % (images_path, im_file_name)
                        #print(im_file_path)
                        image = np.asarray(Image.open(im_file_path))
                        image = resize(image, (310,223), mode='reflect')
                        pics.append(self.crop_image(image,x_dim,y_dim))
                    except OSError:
                        pass
            except:
                pass

        return pics
    
#    def get_batch(image_files, width, height, mode):
#        data_batch = np.array(
#            [get_image
    
    def get_batches(self, batch_size):
        IMAGE_MAX_VALUE = 255
        
    def get_images(self):
        return self.data_images
        
        
        
        
        
        
        
        
        
        
        