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
import io
# import fitz


path='/home/mehroz/pdf_filed_2/Untitled Folder/Aluminum paper/'
list_of_papers=listdir(path)

for paper_name in range(0,len(list_of_papers)):
    paper=path+list_of_papers[paper_name]
    print('\n paper',list_of_papers[paper_name])
    doc = fitz.open(paper)
    #print('\n paper')
    c = 0
    save_files = '/home/mehroz/images/'
    save_folder = save_files + list_of_papers[paper_name]
    os.mkdir(save_folder)
    save_folder = save_folder + '/'

    #print(doc.getPageImageList(3))
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            num=img[0]
            xref = img[0]

            print(xref)
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 4:       # this is GRAY or RGB




                pix.writePNG("p%s-%s.png" % (i, xref))
                pix.getImageData(output='png')

                d = pix.getImageData(output='png')
                image = Image.open(io.BytesIO(d))

                image.save(save_folder + str(c) + '.png')
                c = c + 1

                # pix.samples
                # mode = "RGBA" if pix.alpha else "RGB"
                # img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
                # img.save('/home/mehroz/images/'+str(num)+'.png')
                # #imshow(img)
                #tkimg = ImageTk.PhotoImage(img)
            #
            #     #print('\n p value : ',p)
            # else:               # CMYK: convert to RGB first
            #     pix1 = fitz.Pixmap(fitz.csRGB, pix)
            #     pix1.writePNG("p%s-%s.png" % (i, xref))
            #     p1=pix1.getImageData(output='png')
            #     print('\n p value : ',p1)
            #     pix1 = None
            # pix = None
            #

