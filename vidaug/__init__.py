import cv2
import numpy as np
import os

from PIL import Image, ImageSequence
import augmentors as va

from os.path import isfile, join

def image_loader(path, modality="RGB"):
    with open(path, 'rb') as f:
        with Image.open(f) as video:
            index = 1
            for frame in ImageSequence.Iterator(video):
                frames.append(frame.convert(modality))
                print (index)
                index += 1
        return frames

def get_frames_array(path):
        frames = []
        files = [f for f in os.listdir(path) if isfile(join(path, f))]
 
        # for sorting the file names properly
        files.sort(key = lambda x: x[5:-4])
        files.sort()
 
        for i in range(len(files)):
                filename = path + files[i]
                # reading each files
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width,height)
                print(filename)
                # inserting the frames into an image array
                frames.append(img)
        return frames, size

path = r"C:/Users/wahab/Desktop/FYP/This"
save_path = r"C:/Users/wahab/Desktop/FYP/Augmented Videos/"
dir = os.listdir(path)

for file in dir:
        print (file)
        
        if not os.path.exists(save_path+file):
                        os.mkdir(save_path+file)

        dirs = os.listdir(path+'/'+file) 
        for action in dirs:
                print (action)
        
                frames = []
                fps = 30
                frames, size = get_frames_array(path+'/'+file+'/'+action+'/')
		
		# Horizontal Flip
		frames[0]
                sometimes = lambda aug: va.Sometimes(1, aug) # Used to apply augmentor with 100% probability
                seq = va.Sequential([   
                sometimes(va.HorizontalFlip()) 
                ])

                video_aug = seq(frames)
                out = cv2.VideoWriter(save_path+file+'/'+action+'_HorizontalFlip.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
                for i in range(len(video_aug)):
                        out.write(video_aug[i])
                out.release()

                # Vertical Flip
                frames[0]
		sometimes = lambda aug: va.Sometimes(1, aug) # Used to apply augmentor with 100% probability
                seq = va.Sequential([  
                sometimes(va.VerticalFlip()) 
                ])

                video_aug = seq(frames)
                out = cv2.VideoWriter(save_path+file+'/'+action+'_VerticalFlip.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
                for i in range(len(video_aug)):
                        out.write(video_aug[i])
                out.release()

                # Below is an example to use some other augmentation techniques.


                # To add Salt effect in Video
                # frames[0]

                # sometimes = lambda aug: va.Sometimes(0.5, aug) # Used to apply augmentor with 100% probability
                # seq = va.Sequential([
                #         sometimes(va.Salt(ratio=50))
                # ])

                # video_aug = seq(frames)

                # out = cv2.VideoWriter(save_path+file+'/'+action+'_Salt.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

                # for i in range(len(video_aug)):
                #         out.write(video_aug[i])
                # out.release()

                # For Random Shear in Video
                # frames[0]

                # sometimes = lambda aug: va.Sometimes(1, aug) # Used to apply augmentor with 100% probability
                # seq = va.Sequential([ # randomly rotates the video with a degree randomly choosen from [-10, 10]  
                #         sometimes( va.RandomShear(x=0.3,y=0.3) )
                # ])

                # video_aug = seq(frames)

                # out = cv2.VideoWriter(save_path+file+'/'+action+'_RandomShear.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

                # for i in range(len(video_aug)):
                #         out.write(video_aug[i])
                # out.release()
