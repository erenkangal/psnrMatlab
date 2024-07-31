import math
#import cv2

def psnr(original, noisy):

    if original.shape != noisy.shape:
        raise ValueError("Images must have the same dimensions.")

    mse = 0
    height, width, channels = original.shape
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                diff = int(original[y, x, c]) - int(noisy[y, x, c])
                mse += (float(diff) * float(diff))

    mse /= (height * width * channels)
    max_intensity = 255.0

    if mse == 0:
        return float('inf')

    psnr = 10 * math.log10(max_intensity ** 2 / mse)

    return psnr


#######################################################################################################################
###################################           For Try                 #################################################

""" original_image = cv2.imread("Noise.png")
noisy_image = cv2.imread("NoisedImage.png")

psnr_value = psnr(original_image, noisy_image)

print("PSNR:", psnr_value, "dB") """