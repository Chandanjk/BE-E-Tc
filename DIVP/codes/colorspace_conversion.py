import cv2
import numpy as np
from matplotlib import pyplot as plt

def rgb_to_YIQ(img, maxRGB=255):
    '''
    Convert HSI to RGB
    H:      H
    S:      S
    I:      I
    Hnorm:  True for normalized H
            False for H in degrees (default)
    maxRGB: Maximum RGB (255 by default)
    '''
    if Hnorm:
        H *= 360
    with warnings.catch_warnings():
        # NaNs are expected when r=g=b
        # Python throws a warning on NaN, but ArcGIS Pro just fails
        warnings.simplefilter('ignore')
        case = np.where(np.isnan(H), 0, np.where(H < 120, 1, np.where(H < 240, 2, 3)))
        H = np.where(case == 0, 0, np.where(case == 1, H, np.where(case == 2, H-120, H-240)))
        c1 = np.where(case == 0, I, I*(1-S))
        c2 = np.where(case == 0, I, I*(1+S*np.cos(H/180*np.pi)/np.cos((60-H)/180*np.pi)))
        c3 = np.where(case == 0, I, 3*I-(c1+c2))
    R = np.where(case <= 1, c2, np.where(case == 2, c1, c3))*maxRGB
    G = np.where(case <= 1, c3, np.where(case == 2, c2, c1))*maxRGB
    B = np.where(case <= 1, c1, np.where(case == 2, c3, c2))*maxRGB
    return R, G, B

def rgb_to_cmy(R, G, B, maxRGB=255):
    '''
    Convert RGB to CMY
    R:      R
    G:      G
    B:      B
    maxRGB: Maximum RGB (255 by default)
    '''
    C = maxRGB-R;
    M = maxRGB-G;
    Y = maxRGB-B;
    return C, M, Y

def rgb_to_hsi(img, maxRGB=255, Hnorm=False):
    '''
    Convert RGB to HSI
    R:      R
    G:      G
    B:      B
    maxRGB: Maximum RGB (255 by default)
    Hnorm:  True for normalized H
            False for H in degrees (default)
    '''
    r = R/maxRGB
    g = G/maxRGB
    b = B/maxRGB
    I = (r+g+b)/3
    with warnings.catch_warnings():
        # NaNs are expected when r=g=b
        # Python throws a warning on NaN, but ArcGIS Pro just fails
        warnings.simplefilter('ignore')
        theta = np.arccos(((r-g)+(r-b))/2/np.sqrt((r-g)**2+(r-b)*(g-b)))/np.pi*180
        H = np.where(g >= b, theta, 360-theta)
        if Hnorm:
            H /= 360
        # clip S just in case there are small negative numbers
        S = np.clip(1-np.minimum.reduce([r, g, b])/I, 0, 1)
    return H, S, I


img1 = cv2.imread('Images/babyincradle.png')

plt.subplot(2, 2, 1), plt.imshow(img1,),plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(log_image, 'gray'),plt.title('Image after Log Transformation')
plt.subplot(2, 2, 3), plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 2, 4), plt.hist(log_image.ravel(),256,[0,256]),plt.title('Histogram of Image after Log Transformation')
plt.show() # To show figure