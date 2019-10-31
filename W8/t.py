w0 = -59.50
w1 = -0.15
w2 = 0.60


def t(o, a, h, p):
    d = o - p
    #print("{}\t{}\t{}\t{}\t{}".format(d, d ** 2, d, d * a, d * h))
    return [d, d ** 2, d, d * a, d * h]

data = [[37.99, 41, 138, 17.15],
        [47.34, 42, 133, 26.00],
        [44.38, 37, 151, 25.55],
        [28.17, 46, 133, 13.40],
        [27.07, 48, 126, 8.90],
        [37.85, 44, 145, 20.90],
        [44.72, 43, 158, 28.85],
        [36.42, 46, 143, 19.40],
        [31.21, 37, 138, 17.75],
        [54.85, 38, 158, 29.60],
        [39.84, 43, 143, 19.85],
        [30.83, 43, 138, 16.85]]
#use ocr tool to do that
l=list()
for i in data:
    l.append(t(i[0], i[1], i[2], i[3]))
for i in range(5):
    s=0
    for o in range(len(l)):
        s+=l[o][i]
    print("{}".format(s),end="\t")
print()
nw0 = -59.50
nw1 = -0.1313714
nw2 = 0.6627366
for i in range(len(data)):
    data[i][3]=nw0+nw1*data[i][1]+nw2*data[i][2]
l=list()
for i in data:
    l.append(t(i[0], i[1], i[2], i[3]))
for i in range(5):
    s=0
    for o in range(len(l)):
        s+=l[o][i]
    print("{}".format(s),end="\t")
