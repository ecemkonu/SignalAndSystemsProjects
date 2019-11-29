from scipy.fftpack import ifftn
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

######################################################################
# Am example image is created
# Explain each line of the code using line comments
im = np.zeros((200, 200)) #image with size 200x200 initialized, all blocks are black (0,0,0 )-> no color pigment.
im[:, 100:200] = im[:, 100:200] + 255 #initialize left half of columns with white value.
plt.figure() #plot figure
plt.imshow(im, cmap='gray') #plot im, np array with colors gray in figure.
plt.title('Image') #name plot title as image.
plt.show() #show plot, otherwise it wont be shown from console.

####################################################################
# Explain each line of the following code block separately
im_fft = np.fft.fft2(im) #applies 2 dim fourier transform to input array, transforms it to freq domain
im_fft = np.fft.fftshift(im_fft)  #zero frequency spectrum is centered in image
plt.imshow(np.abs(im_fft), cmap= 'gray') #shows freq domain rep of im
plt.title('FT of the image') #name plot title as  ft image.
plt.show()

# Explain image of fourier transfom. Why did you get such an image?
"""
with fourier transform, we change the basis of our image from x,y indexes to frequency
vertical frequency u and horizontal freq v, that has radiance as unit.
Since we took the integral, and image has no change in x axis, u=0, v = 100n.
Our output image goes has shape [0,200] x[0,200] because input image had this as period.
Two dimensional spatial representation of im, had no difference on u axis,
had impulse like response for 100, where image showed a horizontal change,
since v is a frequency response, it has response in small range close to 100, which represents
complex exponential like frequency response of input image.
shifted zero component enabled us to see impulse in center, showing it diminish when value gets further away in both directions.
"""
################################################################
# Another example image is created
# Explain each line of the code using line comments
im = np.zeros((200, 200)) #same as first initialization.
im[100:200, :] = im[100:200, :] + 255 #image is same size as first, however this time image goes from black to white in rows, simulating vertical change.
plt.figure()
plt.imshow(im,  cmap= 'gray')
plt.title('Image')
plt.show()


####################################################################
# Explain each line of the following code block separately
im_fft = np.fft.fft2(im)
im_fft = np.fft.fftshift(im_fft)
plt.imshow(np.abs(im_fft),  cmap= 'gray')
plt.title('FT of image')
plt.show()

# Explain image of fourier transfom. Why did you get such an image?
# Why are there differences between this image and previous image of fft?
"""
This time image had shown change in vertical axis, which simulates a change, impulse like frequency response from u will be expected. when u =100, there is a change from input
image which colors pixels white, in our new basis u will show change in value. Since image has unit impulse response as freq response, output image is plotted, showing
a small ranging signal that diminishes closely as our u value grows distant from 100, u = delta(y-100). 
"""

###############################################################
# Explain each line of the following code block separately
im_fft = np.fft.ifftshift(im_fft) # im is fitted to center using fftshift, im_fft should be converted back before running ifft2. zero freq component shifted to beginning again/
im = np.fft.ifft2(im_fft) # ifft runs fourier analysis on provided data.
plt.figure()
plt.imshow(im.real, cmap= 'gray')
plt.title('IFT of FT of image') #we are expected to see second image we have used, analysis method will map F(u,v) to f(x,y). Since v was similar to delta(x-100), we expect
#to see a color shift at around x= 100.
plt.show()
#and no change until im size is met[1 period.].

###############################################################
# Explain each line of the following code block separately
im_fft = np.fft.fftshift(im_fft)  #ifft canceled, im_fft is fitted in center, impulse can be seen in center. 
im_fft[105:199, :] = 0  # rows from 105 to 199 is set to zero, could be to reduce size of image, since u is set to zero in some values that it should have small changes. 
# this could cause some white values to overlap with black in image, since frequency of it would be increased.
im = np.fft.ifft2(im_fft)
plt.figure()
plt.imshow(im.real, plt.cm.gray)
plt.title('IFT of filtered FT of image')
plt.show()

# Why do you obtained such an image after previous operation?
"""
Since some u values were set to black, change was reduced, freq response was decreased in transformed image. White would had its frequency increased, which would increase periodicity,
in spatial domain output image from ifft thus showed some white values overlapped in black.
"""

##########################################################################
# Explain each line of the followinf code block separately
N = 100
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N,N)) #array with size 100x100
xf[0, 5] = 1 # first row 5th col is white.
Z = ifftn(xf) #inverse fourier transform, specified array had change in u ->0 v ->5.  
ax1.imshow(xf,  cmap= 'gray')
ax4.imshow(np.real(Z),  cmap= 'gray')
xf = np.zeros((N, N))
xf[5, 0] = 1
Z = ifftn(xf)
ax2.imshow(xf,  cmap= 'gray')
ax5.imshow(np.real(Z), cmap='gray')
xf = np.zeros((N, N))
xf[5, 10] = 1
Z = ifftn(xf)
ax3.imshow(xf, cmap='gray')
ax6.imshow(np.real(Z), cmap='gray')
figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()
plt.show()

# Comment about obtained images
"""
In first image we expect to see a vertical striped image with period, 100/5 -> 20. 
In second image we expect to see a horizontal striped image with period, 100/5 -> 20. 
In third image we expect to see diagonal striped image with periods 20 20.
"""

#######################################################################################
# Explain each line of the following code block separately
N = 100
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N,N))
xf[0, 20] = 1
Z = ifftn(xf)
ax1.imshow(xf, cmap ='gray')
ax4.imshow(np.real(Z), cmap = 'gray')
xf = np.zeros((N, N))
xf[20, 0] = 1
Z = ifftn(xf)
ax2.imshow(xf, cmap='gray')
ax5.imshow(np.real(Z), cmap='gray')
xf = np.zeros((N, N))
xf[10, 20] = 1
Z = ifftn(xf)
ax3.imshow(xf, cmap='gray')
ax6.imshow(np.real(Z), cmap='gray')
figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()
plt.show()

# Comment about difference between this image and previous image
"""
Write your comments in here
"""



