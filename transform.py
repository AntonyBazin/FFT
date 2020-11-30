from PIL import Image
from scipy import fft
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


class Transformer:
    def __init__(self, filename: str):
        self.file = filename
        self.name = filename[:-3]
        grayscale_image = Image.open('./samples/' + self.file).convert('L')
        grayscale_image.save('./buffer/gray_' + self.file)
        self._data = plt.imread('./buffer/gray_' + self.file)
        self._plotting = self._data

    @staticmethod
    def show_all():
        plt.show()

    def run(self):
        self.plot('Original image')
        self.transform()
        self.plot_fft('Pure FT', './results/pure_fft_')
        self.shift()
        self.plot_fft('FT with FFTShift', './results/shifted_fft_')
        self.inverse()
        self.plot('Reconstructed image',
                  'gray',
                  False)
        self.save()
        plt.show()

    def save(self):
        plt.figure()
        plt.axis('off')
        plt.imshow(self._plotting, cmap='gray')
        plt.savefig('./buffer/reconstructed_' + self.file + '.jpg',
                    bbox_inches='tight',
                    pad_inches=0)

    def inverse(self):
        self._data = fft.ifft2(self._data)
        self._plotting = np.abs(self._data)

    def shift(self):
        self._plotting = np.abs(np.fft.fftshift(self._data))

    def transform(self):
        self._data = fft.fft2(self._data)  # may also use real fft here, but it will only give a half of the image
        self._plotting = np.abs(self._data)
        return self

    def plot_fft(self, name, address=''):
        self.plot(name + ' of ' + self.file,
                  'gray',
                  True,
                  address,
                  norm=LogNorm(vmin=1))

    def plot(self, title='', colormap='gray', bar=False, save='', **kwargs):
        plt.figure()
        plt.title(title)
        if kwargs:
            plt.imshow(self._plotting, cmap=colormap, norm=kwargs.get('norm'))
        else:
            plt.imshow(self._plotting, cmap=colormap)
        if bar:
            plt.colorbar()
        if save:
            plt.savefig(save + self.name + '.jpg')


if __name__ == '__main__':
    print('Input source file\'s name here:')
    src = input()
    worker = Transformer(src)
    try:
        worker.run()
    except FileNotFoundError as er:
        print(er)
