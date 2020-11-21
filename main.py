from PIL import Image
from scipy import fft
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


def save_grayscale(image_name: str):
    grayscale_image = Image.open(image_name).convert('L')
    grayscale_image.save('./buffer/gray_' + image_name)
    return './buffer/gray_' + image_name


def save_new(pixels, filename, addition):
    """Save a version of the image from the pixels array"""
    image = Image.fromarray(pixels, 'L')
    image.save(addition + filename)


def plot_spectrum(im_fft):
    """A logarithmic colormap"""
    plt.imshow(np.abs(im_fft), cmap='gray', norm=LogNorm(vmin=1))
    plt.colorbar()


def run(filename: str):
    gray_img = save_grayscale(filename)

    data = plt.imread(gray_img)  # 2d pixel array
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.title('Original image')

    new_image = fft.fft2(data)  # may also use real fft here, but it will only give a half of the image
    plt.figure()
    plt.title('Pure FFT of ' + filename)
    plot_spectrum(new_image)
    plt.savefig('./results/pure_fft_' + filename + '.jpg')

    plt.figure()
    plt.title('FFT of ' + filename + ' with FFTShift')
    plot_spectrum(np.fft.fftshift(new_image))
    plt.savefig('./results/shifted_fft_' + filename + '.jpg')

    # save_new(np.abs(new_image), filename, './results/fft_')

    inv = fft.ifft2(new_image)
    plt.figure()
    plt.imshow(np.abs(inv), cmap='gray')
    plt.title('Reconstructed Image')
    plt.savefig('./buffer/reconstructed_' + filename + '.jpg')
    # save_new(inv, filename, './results/inv_fft_')
    plt.show()


if __name__ == '__main__':
    print('Input source file\'s name here:')
    src = 'jankaluza_dew_drop.jpg'
    run(src)
