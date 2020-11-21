from PIL import Image
from scipy import fft
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


class Transformer:
    def __init__(self, filename: str):
        self.file = filename
        self.name = filename[:-3]
        self._data = None
        self._plotting = None

    def run(self):
        self.prepare()
        self.transform()
        self.inverse()
        plt.show()

    def inverse(self):
        self._data = fft.ifft2(self._data)
        self._plotting = np.abs(self._data)
        self.plot('Reconstructed image',
                  'gray',
                  False)
        self.plot()
        plt.savefig('./buffer/reconstructed_' + self.file + '.jpg',
                    bbox_inches='tight',
                    pad_inches=0)

    def transform(self):
        self._data = fft.fft2(self._data)  # may also use real fft here, but it will only give a half of the image
        self._plotting = np.abs(self._data)
        self.plot('Pure FT of ' + self.file,
                  'gray',
                  True,
                  './results/pure_fft_',
                  norm=LogNorm(vmin=1))
        self._plotting = np.abs(np.fft.fftshift(self._data))
        self.plot('FT of ' + self.file + ' with FFTShift',
                  'gray',
                  True,
                  './results/shifted_fft_',
                  norm=LogNorm(vmin=1))

    def prepare(self):
        grayscale_image = Image.open('./samples/' + self.file).convert('L')
        grayscale_image.save('./buffer/gray_' + self.file)

        self._data = plt.imread('./buffer/gray_' + self.file)
        self._plotting = self._data
        self.plot('Original image')

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
