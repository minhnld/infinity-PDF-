from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_path, convert_from_bytes,pdfinfo_from_path
from PIL import Image  
import PIL  
import tempfile
import os
directory = './'
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        info = pdfinfo_from_path('./'+str(filename), userpw=None, poppler_path=None)
        maxPages = info["Pages"]
        i=-1
        directory_dir=str(filename)+"_dir"
        parent_dir = "./"
        path = os.path.join(parent_dir, directory_dir) 
        os.mkdir(path) 

        # with tempfile.TemporaryDirectory() as path:         #output_folder=path,
        for page in range(1,maxPages,10):
            images_from_path = convert_from_path('./'+str(filename),  fmt='jpeg' , dpi=200, first_page=page, last_page = min(page+10-1,maxPages))
            for image in images_from_path:
                i+=1
                image.save("./"+str(filename)+"_dir"+"/"+str(filename)+"_"+str(i)+".jpeg","JPEG")

