import sys

# creating a empty dictinary to store data
results = {}

# loop thru every line in  the file
for line in sys.stdin:
    # clean the line
    line = line.strip()
    
    # spliting by tab 
    cols = line.split("\t")
    
    # check if we have enough cloumns or not
    if len(cols) < 12:
        continue

    # getting the motif postions (col 3 and 4)
    m1 = int(cols[2])
    m2 = int(cols[3])
    
    # getting fragment positions (col 9 and 10)
    f1 = int(cols[8])
    f2 = int(cols[9])
    
    # get length from column 12
    length = int(cols[11])

    # finding the centers
    # averaging start and end
    center_m = (m1 + m2) / 2
    center_f = (f1 + f2) / 2

    # calulating x (offset) and y (length)
    # x is distance
    x = int(center_f - center_m)
    y = length
    
    # making a key for dict
    key = (x, y)
    
    # counting
    if key in results:
        results[key] = results[key] + 1
    else:
        results[key] = 1

# printing output
for key in results:
    x_val = key[0]
    y_val = key[1]
    count = results[key]
    
    # print with tabs
    print(str(x_val) + "\t" + str(y_val) + "\t" + str(count))