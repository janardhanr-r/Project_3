Project 3

My code for V-plot assignment. reads data and make matrix for plot.

Files

vplot_generate.py: python script to read data and count length.

plot_vplot.gp: script for gnuplot graph.

plot_vplot.py: script for python graph (extra).

How to run

Make data file
run this to unzip and send to python:

zcat mapped.bed.gz | python vplot_generate.py > matrix.dat


Make graph
run this for png:

gnuplot plot_vplot.gp
