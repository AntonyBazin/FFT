import filter as fl


if __name__ == '__main__':
    # example: moonlanding.png;  0.05 0.07 0.1 0.2 0.3
    print('Input source file\'s name here:')
    src = input()
    print('Input the fractions list to filter with,\nseparate with whitespaces:')
    fractions = input().split()
    fractions = [float(fraction) for fraction in fractions]
    try:
        fil = fl.Filter(src)
        fil.plot(src)
        fil.series_lpf(fractions)
        fl.Transformer.show_all()
    except FileNotFoundError as er:
        print(er)
