from transform import Transformer

if __name__ == '__main__':
    tanks = ['tank1.jpg', 'tank2.jpg', 'tank3.jpg']
    planes = ['plane1.jpg', 'plane2.jpg', 'plane3.jpg']
    # for tank, plane in zip(tanks, planes):
    #     tank_tr = Transformer(tank)
    #     plane_tr = Transformer(plane)
    #     tank_tr.transform().shift()
    #     plane_tr.transform().shift()
    #     tank_tr.plot_fft(tank)
    #     plane_tr.plot_fft(plane)
    shapes = ['round.jpg', 'square.png', 'triangle.png']
    # for sh in shapes:
    #     trans = Transformer(sh)
    #     trans.transform().shift()
    #     trans.plot_fft(sh)
    tr = Transformer('mas2.jpg')
    lol = tr.transform()
    lol.plot_fft('1st FT')
    lol.shift()
    lol.plot_fft('1st FT shifted')
    tr.transform().shift()
    tr.plot_fft('2nd shifted FT')
    tr.transform().shift()
    tr.plot_fft('3rd shifted FT')
    tr.transform().shift()
    tr.plot_fft('4th shifted FT')
    tr.transform().shift()
    tr.plot_fft('5th shifted FT')
    tr.transform().shift()
    tr.plot_fft('6th shifted FT')
    tr.transform().shift()
    tr.plot_fft('7th shifted FT')
    Transformer.show_all()
