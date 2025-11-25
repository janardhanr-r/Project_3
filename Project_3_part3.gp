# saveing as png image
set terminal pngcairo size 800,600
set output 'vplot.png'

# setting labels
set title "V-Plot"
set xlabel "Distance"
set ylabel "Length"

# setting range for axis
set xrange [-500:500]
set yrange [0:300]

# dont need legend key
set key off

# setting colors 
set palette defined (0 "white", 1 "blue", 2 "red", 3 "black")

# plotting form file
# using col 1 2 and 3
plot 'matrix.dat' using 1:2:3 with points pt 5 ps 0.5 palette