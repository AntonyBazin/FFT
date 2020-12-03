# FFT
Some experiments with the Fast Fourier Transform.

[More about FFT](https://en.wikipedia.org/wiki/Fast_Fourier_transform "Wiki")


## Timing

You can use 

```bash
gnuplot --persist -e 'plot "timing-fft.txt" u 1:2 w linespoints linestyle 1'
```
or
```bash
gnuplot --persist -e 'set logscale x; plot "timing-fft.txt" using 1:2 with linespoints'
```
to plot the timing diagrams.