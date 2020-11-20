from PIL import Image
from scipy import fft
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np


def save_new(pixels, filename, mark):
    image = Image.fromarray(pixels, 'L')
    image.save(mark + filename)
    return image


def plot_spectrum(im_fft):
    from matplotlib.colors import LogNorm
    # A logarithmic colormap
    plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
    plt.colorbar()


def run(filename: str):
    data = plt.imread('./samples/' + filename) # np.asarray(img)  # 2d pixel array
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.title('Original image')

    new_image = fft.rfft2(data)
    plt.figure()
    plt.title('Fourier transform')
    plot_spectrum(new_image)
    save_new(new_image, filename, './results/fft_')

    inv = fft.irfft2(new_image)
    plt.figure()
    plt.imshow(inv, cmap='gray')
    plt.title('Reconstructed Image')
    plt.show()
    save_new(inv, filename, './results/inv_fft_')


if __name__ == '__main__':
    print('Input source file\' name here:')
    src = 'BRIDGE.BMP'
    run(src)
