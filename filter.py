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

    def filter_many_times(self, fractions: list):
        super().transform()
        _data_copy = self._data.copy()
        for i, fraction in enumerate(fractions):
            self._data = _data_copy.copy()
            self._data[int(self.r * fraction):int(self.r * (1 - fraction))] = 0
            self._data[:, int(self.c * fraction):int(self.c * (1 - fraction))] = 0
            super().inverse()
            self.plot(str(i + 1) + ') Reconstruction from ' + str(fraction),
                      'gray',
                      False)

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
    # dn = Denoiser('noise_city.jpg')
    # dn.filter_many_times([0.07, 0.08, 0.09, 0.1, 0.11, 0.15])
    dn2 = Denoiser('moonlanding.png')
    dn2.filter_many_times([0.07, 0.08, 0.09, 0.1, 0.11, 0.15])
    Transformer.show_all()
