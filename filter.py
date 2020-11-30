from transform import Transformer
# remove noise from images using FFT


class Denoiser(Transformer):
    def __init__(self, filename: str, frac=0.1):
        super().__init__(filename)
        self.fraction = frac
        self._datacopy = None
        self.rows, self.columns = 0, 0

    def prepare_denoising(self):
        self._datacopy = self._data
        self.rows, self.columns = self._data.shape()

if __name__ == '__main__':
    pass