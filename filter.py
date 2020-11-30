from transform import Transformer


# remove noise from images using FFT


class Denoiser(Transformer):
    def __init__(self, filename: str, frac=0.1):
        super().__init__(filename)
        self.fraction = frac
        self._datacopy = None
        self.rows, self.columns = 0, 0

    @staticmethod
    def method_disabled():
        raise NotImplementedError('This function is not implemented in denoiser')

    def transform(self): Denoiser.method_disabled()

    def shift(self): Denoiser.method_disabled()

    def inverse(self): Denoiser.method_disabled()

    def run(self):
        pass

    def __prepare_denoising(self):
        self._datacopy = self._data
        self.rows, self.columns = self._data.shape()

    def denoise(self):
        self.__prepare_denoising()
        self.transform()




if __name__ == '__main__':
    dn = Denoiser('mas2.jpg')
    dn.transform().shift()
