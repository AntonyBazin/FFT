import filter as fl

if __name__ == '__main__':
    print('Input source file\'s name here:')
    src = input()
    print('Input the fraction to filter, default is 0.1:')
    fraction = input()
    if not fraction:
        fraction = 0
    else:
        fraction = float(fraction)
    try:
        filter1 = fl.Filter(src, fraction)
        filter2 = fl.Filter(src, fraction)
        filter1.plot(src)
        filter1.low_pass_filter()
        filter2.high_pass_filter()
        fl.Transformer.show_all()
    except FileNotFoundError as er:
        print(er)
