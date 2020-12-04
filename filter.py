from transform import Transformer
import numpy as np


class Filter(Transformer):
    """The Filter class is used for filtering images via removing
    some parts of their Fourier transform. If the low pass filter is used,
    only the low frequencies of the transform are conserved,
    leading to blurring the image but also removing some periodic noises
    The high pass filter, on the contrary, conserves the high frequencies,
    detecting the edges of the image.
    """
    def __init__(self, filename: str, fraction=0.1):
        """The class is derived from the Transformer class, but provides
        additional functionality"""
        super().__init__(filename)
        self.fraction = fraction
        self.r, self.c = self._data.shape

    @staticmethod
    def method_disabled():
        """This method is used to protect the image inside from
        any Fourier transformations, unless called from inside
        the class's own methods"""
        raise AttributeError('This function is not implemented in denoiser')

    def transform(self): Filter.method_disabled()

    def inverse(self): Filter.method_disabled()

    def series_lpf(self, fractions: list):
        """This method can be used for convenience when denoising images"""
        super().transform()
        self.shift()
        self.plot_fft('FT of')
        _data_copy = self._data.copy()
        for i, fraction in enumerate(fractions):
            self._data = _data_copy.copy()
            self._data[int(self.r * fraction):int(self.r * (1 - fraction))] = 0
            self._data[:, int(self.c * fraction):int(self.c * (1 - fraction))] = 0
            super().inverse()
            self.plot(str(i + 1) + ') Reconstruction from ' + str(fraction),
                      'gray',
                      False)

    def low_pass_filter(self):
        """This method applies the low pass filter to the image"""
        super().transform()
        self._data[int(self.r * self.fraction):int(self.r * (1 - self.fraction))] = 0
        self._data[:, int(self.c * self.fraction):int(self.c * (1 - self.fraction))] = 0
        self._plotting = np.abs(self._data)
        self.plot_fft('Low pass filtered spectrum')
        self.shift()
        self.plot_fft('Low pass filtered spectrum with shift')
        super().inverse()
        self.plot('Low pass filtered image',
                  'gray',
                  False)

    def high_pass_filter(self):
        """This method applies the high pass filter to the image"""
        super().transform()
        self._data[0:int(self.r * self.fraction), 0:int(self.c * self.fraction)] = 0
        self._data[int(self.r * (1 - self.fraction)):self.r, 0:int(self.c * self.fraction)] = 0
        self._data[0:int(self.r * self.fraction), int(self.c * (1 - self.fraction)):self.c] = 0
        self._data[int(self.r * (1 - self.fraction)):self.r, int(self.c * (1 - self.fraction)):self.c] = 0
        self._plotting = np.abs(self._data)
        self.plot_fft('High pass filtered spectrum')
        self.shift()
        self.plot_fft('High pass filtered spectrum with shift')
        super().inverse()
        self.plot('High pass filtered image',
                  'gray',
                  False)


if __name__ == '__main__':
    fl1 = Filter('6A(142).BMP', 0.07)
    fl1.plot('6A(142).BMP')
    fl1.low_pass_filter()

    fl2 = Filter('6A(142).BMP', 0.07)
    fl2.high_pass_filter()
    Transformer.show_all()
