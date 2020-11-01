from PIL import Image
# import matplotlib.pyp lot as plt
import numpy as np


def form_pixels(base, function):
    return list(map(function, base))


def save_new(pixels, mark, filename, size, mode='L'):
    image = Image.new(mode, size)
    image.putdata(pixels)
    image.save(mark + filename)
    return image


def get_ffts(fft_pixels):
    rl = form_pixels(fft_pixels, np.real)
    im = form_pixels(fft_pixels, np.imag)
    ab = form_pixels(fft_pixels, np.abs)
    return ab, im, rl


def fft_from_numpy(filename: str):
    img = Image.open(filename).convert('L')
    img.save('grey_' + filename)
    ab, im, rl = get_ffts(np.fft.fft(img.getdata()))

    save_new(rl, 'real_fft_', filename, img.size)
    save_new(im, 'im_fft_', filename, img.size)
    save_new(ab, 'abs_fft_', filename, img.size)


if __name__ == '__main__':
    print('Input source file\' name here:')
    src = input()
    fft_from_numpy(src)
