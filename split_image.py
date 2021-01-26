import cv2
import argparse
import os
parser = argparse.ArgumentParser(description="image splitter command line options")
parser.add_argument('-e', action= 'store', help = 'set path to export subimage')
parser.add_argument('-s', action='store', help='number of split up images', default=2)
parser.add_argument('-f', action='store', help = 'image filename')
args=parser.parse_args()
path = args.f 

if path is None:
    path = "E:\Pictures\Export\social_media_exports\IR6_7207-Pano.jpg"
    
filename = os.path.basename(path).split(".")[0]

export_path = args.e 
if export_path is None:
    export_path=os.path.dirname(path)

num_splits = 7 
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
# img = cv2.imread('E:\Pictures\Export\social_media_exports\IR6_7207-Pano.jpg',cv2.IMREAD_UNCHANGED)
height=int(img.shape[0])
width=int(img.shape[1])


sub_width=width/num_splits
odd=False
# is image width an odd number?
if sub_width%2 is 1:
    odd=True
print(f"image parameters, height:{height} width:{width} num of splits:{num_splits}")

x1 =1
index=0
for sub_image in range(0,num_splits):
    x2 = int(x1 + sub_width)
    # sub_image =img[280:340, 330:390]
    sub_image=img[0:height, x1:x2]
    # sub_image=img[height:1, x2:x1]
    print(f"index:{index} x1:{x1} x2:{x2}")
    x1 = x2
    index += 1
    cv2.imshow("Resized image", sub_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    path_filename=(f"{export_path}\{filename}_{int(index)}.jpg")
    cv2.imwrite(path_filename,sub_image)
