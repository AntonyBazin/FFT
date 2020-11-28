from transform import Transformer
import matplotlib.pyplot as plt

if __name__ == '__main__':
    tanks = ['tank1.jpg', 'tank2.jpg', 'tank3.jpg']
    planes = ['plane1.jpg', 'plane2.jpg', 'plane3.jpg']
    for tank, plane in zip(tanks, planes):
        tank_tr = Transformer(tank)
        plane_tr = Transformer(plane)
        tank_tr.prepare()
        plane_tr.prepare()
        tank_tr.transform().shift()
        plane_tr.transform().shift()
        tank_tr.plot_fft(tank)
        plane_tr.plot_fft(plane)
    shapes = ['round.jpg', 'square.png', 'triangle.png']
    # for sh in shapes:
    #     trans = Transformer(sh)
    #     trans.prepare()
    #     trans.transform().shift()
    #     trans.plot_fft(sh)
    plt.show()
