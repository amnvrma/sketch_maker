
import skimage.io
import skimage.viewer
import pyautogui

import time


time.sleep(2)
# START=time.time()
pyautogui.PAUSE=0.001


image=skimage.io.imread(fname="prof.png",as_gray=True)
image=skimage.transform.resize(image,(373,250))

viewer=skimage.viewer.ImageViewer(image)
# print(image.shape)
# h,w=image.shape
# print(image[0,0])
print("ENjoy the sketch !!")
print("guess who it can be")


for i in range(0,w,2):

	for j in range(0,h,2):
		if(image[j,i]<0.4):
			pyautogui.PAUSE=0
			pyautogui.moveTo(i+200,j+250)
			pyautogui.PAUSE=0.01
			pyautogui.click()

# END=time.time()
# print("time taken:",round(END-START,2))

print("yes..You guessed it right..its Professor Sergio")
		

viewer.show()


