#import PyMuPDF
import fitz
from matplotlib.pyplot import imshow
from PIL import Image, ImageTk
from os import listdir
from pathlib import Path
import json
import os.path
import os
#
#
import pandas as pd
import io
# import fitz


path='/home/mehroz/pdf_filed_2/Untitled_Folder/collection_of_papers/'

images = '/home/mehroz/Mat-Sci/freq_data/images'
os.mkdir(images)
images = images + '/'

list_of_papers=listdir(path)
comp_dict = {}
comp_df = pd.DataFrame.from_dict({'no_of_images': ['1']})

for paper_name in range(0,len(list_of_papers)):
    paper=path+list_of_papers[paper_name]
    #print('\n paper',list_of_papers[paper_name])
    counter = 0

    doc = fitz.open(paper)


    #print(doc.getPageImageList(3))
    for i in range(len(doc)):
        counter=counter+len(doc.getPageImageList(i))

        print(doc.getPageImageList(i))

    no_of_images = {'no_of_images': [str(counter)]}
    # print('type of entity ',ent.text.encode("utf-8").isdigit())
    df = pd.DataFrame.from_dict(no_of_images.copy())
    comp_df = comp_df.append(df, ignore_index=True)
    comp_df.drop(comp_df.index[0], inplace=True)
    comp_df.to_csv(images + list_of_papers[paper_name][:-4] + '.csv', header=True, index=False, encoding='utf-8')
    comp_df = 0
    comp_df = pd.DataFrame.from_dict({'no_of_images': ['1']})

