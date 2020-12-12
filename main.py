import filter as fl
from transform import Transformer
import time
import sys
import tkinter as tk


class Application(tk.Frame):
    """The Application class provides the GUI for working with FFT"""
    def __init__(self, master=None):
        """The constructor of the class objects, initializes items on the window"""
        super().__init__(master)
        self.master = master
        self.pack()
        master.title('Main dialog')

        no_file_label = tk.Label(self, text='No input is needed to run these:')
        run_show_primitives = tk.Button(self, text='Run primitives transform',
                                        command=self.run_show_primitives)
        run_comp = tk.Button(self, text='Run face and vase spectra comparison',
                                        command=self.run_comp)
        run_timing_button = tk.Button(self, text='Run timing',
                                      command=self.run_timing)

        file_label = tk.Label(self, text='Functions below need a file to work on:')
        self.box = tk.Entry(self, textvariable=tk.StringVar)
        self.box.insert(0, 'File\'s name')
        run_transform_button = tk.Button(self, text='Run fft and inverse fft',
                                         command=self.run_transform)
        file_and_frac_label = tk.Label(self,
                                       text='Different filters function needs a fraction to work with:')
        self.fracbox = tk.Entry(self, textvariable=tk.StringVar)
        self.fracbox.insert(0, '0.1')
        run_filter_button = tk.Button(self, text='Run different filters',
                                      command=self.run_filter)

        fraction_list_label = tk.Label(self,
                                       text='Filtering with many fractions requires a list to work with:')
        self.many_fractions = tk.Entry(self, textvariable=tk.StringVar)
        self.many_fractions.insert(0, '0.05 0.07 0.1 0.2 0.3')
        run_list_filter_button = tk.Button(self, text='Run filter with list',
                                           command=self.run_list_filter)

        quit_button = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)

        self.items = [no_file_label,
                      run_comp,
                      run_show_primitives,
                      run_timing_button,
                      file_label, self.box,
                      run_transform_button,
                      file_and_frac_label,
                      self.fracbox,
                      run_filter_button,
                      fraction_list_label,
                      self.many_fractions,
                      run_list_filter_button,
                      quit_button]
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets"""
        for item in self.items:
            item.pack()

    def run_transform(self):
        """Runs the basic FFT demonstration"""
        name = self.box.get()
        try:
            worker = Transformer(name)
            worker.run()
        except FileNotFoundError as er:
            print(er)

    def run_filter(self):
        """Runs the filter class work demonstration"""
        name = self.box.get()
        try:
            fraction = float(self.fracbox.get())
            fl1 = fl.Filter(name, fraction)
            fl1.plot(name)
            fl1.low_pass_filter()

            fl2 = fl.Filter(name, fraction)
            fl2.high_pass_filter()
            Transformer.show_all()
        except Exception as er:
            print(er)

    def run_list_filter(self):
        """Runs filtering the image with many fraction parameters"""
        name = self.box.get()
        try:
            fractions = self.many_fractions.get().split()
            fractions = [float(fraction) for fraction in fractions]
            fil = fl.Filter(name)
            fil.plot(name)
            fil.series_lpf(fractions)
            fl.Transformer.show_all()
        except Exception as er:
            print(er)

    @staticmethod
    def run_show_primitives():
        """Demonstrates the FT images of primitive forms"""
        shapes = ['round.jpg', 'square.png', 'triangle.png']
        for sh in shapes:
            trans = Transformer(sh)
            trans.plot()
            trans.transform().shift()
            trans.plot_fft('Shifted FT of')
        Transformer.show_all()

    @staticmethod
    def run_comp():
        """Demonstrates the FT images of complex forms"""
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

    @staticmethod
    def run_timing():
        """Runs a timing analysis of the FTT algorithm"""
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
        print('Timing completed successfully')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('450x400')
    app = Application(master=root)
    app.mainloop()
