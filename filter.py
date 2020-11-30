from transform import Transformer
import numpy as np

# remove noise from images using FFT


class Denoiser(Transformer):
    def __init__(self, filename: str, frac=0.1):
        super().__init__(filename)
        self.fraction = frac
        self.r, self.c = self._data.shape

    @staticmethod
    def method_disabled():
        raise NotImplementedError('This function is not implemented in denoiser')

    def transform(self): Denoiser.method_disabled()

    def inverse(self): Denoiser.method_disabled()

    def run(self):
        self.filter_spectrum()

    def filter_spectrum(self):
        super().transform()
        self._data[int(self.r * self.fraction):int(self.r * (1 - self.fraction))] = 0
        self._data[:, int(self.c * self.fraction):int(self.c * (1 - self.fraction))] = 0
        self._plotting = np.abs(self._data)
        # self.plot_fft('Filtered Spectrum')
        super().inverse()
        self.plot('Reconstructed image',
                  'gray',
                  False)


if __name__ == '__main__':
    dn1 = Denoiser('noise_city.jpg')
    dn1.run()
    dn2 = Denoiser('noise_city.jpg', 0.07)
    dn2.run()
    # dn3 = Denoiser('noise_city.jpg', 0.2)
    # dn3.run()
    # dn4 = Denoiser('noise_city.jpg', 0.05)
    # dn4.run()
    Transformer.show_all()
