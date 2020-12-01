from transform import Transformer

if __name__ == '__main__':
    shapes = ['round.jpg', 'square.png', 'triangle.png']
    for sh in shapes:
        trans = Transformer(sh)
        trans.transform()
        trans.plot_fft('FT of')
        trans.shift()
        trans.plot_fft('Shifted FT of')
    Transformer.show_all()

    tanks = ['tank1.jpg', 'tank2.jpg', 'tank3.jpg']
    planes = ['plane1.jpg', 'plane2.jpg', 'plane3.jpg']
    for tank, plane in zip(tanks, planes):
        tank_tr = Transformer(tank)
        plane_tr = Transformer(plane)
        tank_tr.transform().shift()
        plane_tr.transform().shift()
        tank_tr.plot_fft('Shifted FT of')
        plane_tr.plot_fft('Shifted Ft of')
    Transformer.show_all()

    tr = Transformer('vase.jpg')
    tr2 = Transformer('face.jpg')
    tr.plot('Original vase')
    tr2.plot('Original face')
    tr.transform()
    tr.plot_fft('FT')
    tr2.transform()
    tr2.plot_fft('FT')
    tr.shift()
    tr.plot_fft('Shifted FT')
    tr2.shift()
    tr2.plot_fft('Shifted FT')
    Transformer.show_all()
