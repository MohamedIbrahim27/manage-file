import os
import shutil


file_path=os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(file_path):
    
    ######
    if filename.endswith((".png","jpg","jpeg")):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print('done')
        
        
    ########
    if filename.endswith((".mp4","3gp","mov","mkv")):
        if not os.path.exists("videos"):
            os.mkdir('videos')
        shutil.copy(filename,"videos")
        os.remove(filename)
        print('done')

    if filename.endswith((".pdf","pptx","ppt")):
        if not os.path.exists("pdf-file"):
            os.mkdir('pdf-file')
        shutil.copy(filename,"pdf-file")
        os.remove(filename)
        print('done')