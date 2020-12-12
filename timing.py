from transform import Transformer
import time
import sys


if __name__ == '__main__':
    try:
        screwdriver = Transformer('6A(142).BMP')  # 320x240 = 76800 p
        vase = Transformer('vase.jpg')  # 320x400 = 128000 p
        city = Transformer('DUSS.BMP')  # 672x473 = 317856 p
        round_tr = Transformer('round.jpg')  # 800x800 = 640000 p
        dew = Transformer('jankaluza_dew_drop.jpg')  # 3840x2562 = 9838080 p
        fire = Transformer('vovalente_fire.jpg')  # 5077x3385 = 17185645 p
    except FileNotFoundError as er:
        print(er)
        sys.exit()
    with open('timing-fft.txt', 'w') as out:
        out.write('# number TIME\n')
    transformers = [screwdriver, vase, city, round_tr, dew, fire]
    sizes = [76800, 128000, 317856, 640000, 9838080, 17185645]
    for size, transformer in zip(sizes, transformers):
        start = time.time()
        transformer.transform()
        end = time.time()
        with open('timing-fft.txt', 'a') as log:
            log.write(str(size) + ' ' + str(end - start) + '\n')
