'''
Created on 2015/10/21

@author: sato
'''
import cv2


def resize_image(src_file_path, dest_file_path, target_width, target_height):
    try:
        im = cv2.imread(src_file_path)
        newIm = cv2.resize(im,(target_width,target_height))
        cv2.imwrite(dest_file_path,newIm)   
    
    except:
        raise


def effect_gry(src_file_path,dest_file_path):
    try:
        im = cv2.imread(src_file_path)
        newImage= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(dest_file_path,newImage)   
    except:
        raise

def effect_sepia(src_file_path,dest_file_path):
    
    try:
        img = cv2.imread(src_file_path)
        newImage = cv2.imread(src_file_path)
        i, j, k = img.shape
        for x in range(i):
            for y in range(j):
                R = img[x,y,2] * 0.393 + img[x,y,1] * 0.769 + img[x,y,0] * 0.189
                G = img[x,y,2] * 0.349 + img[x,y,1] * 0.686 + img[x,y,0] * 0.168
                B = img[x,y,2] * 0.272 + img[x,y,1] * 0.534 + img[x,y,0] * 0.131
                if R > 255:
                    newImage[x,y,2] = 255
                else:
                    newImage[x,y,2] = R
                if G > 255:
                    newImage[x,y,1] = 255
                else:
                    newImage[x,y,1] = G
                if B > 255:
                    newImage[x,y,0] = 255
                else:
                
                    newImage[x,y,0] = B
        newImage=cv2.GaussianBlur(newImage,(5,5),0)
        cv2.imwrite(dest_file_path,newImage)   
    except:
        raise

def effect_sepia_raw(img, newImage):
    
    try:
        i, j, k = img.shape
        for x in range(i):
            for y in range(j):
                R = img[x,y,2] * 0.393 + img[x,y,1] * 0.769 + img[x,y,0] * 0.189
                G = img[x,y,2] * 0.349 + img[x,y,1] * 0.686 + img[x,y,0] * 0.168
                B = img[x,y,2] * 0.272 + img[x,y,1] * 0.534 + img[x,y,0] * 0.131
                if R > 255:
                    newImage[x,y,2] = 255
                else:
                    newImage[x,y,2] = R
                if G > 255:
                    newImage[x,y,1] = 255
                else:
                    newImage[x,y,1] = G
                if B > 255:
                    newImage[x,y,0] = 255
                else:
                
                    newImage[x,y,0] = B
        newImage=cv2.GaussianBlur(newImage,(5,5),0)
    except:
        raise
