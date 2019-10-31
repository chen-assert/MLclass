import re
from math import pow

input_ = "2623 2664 2691 2423 2436 2367 2423 2399 2412 2448 2447 2440 2762 2847 2693 2435 2411 2493 2519 2516 2598 " \
        "2772 2870 2814 2601 2586 2583 2422 2414 2485 2349 2407 2472 2515 2505 2584 2548 2581 2604 2281 2277 2309 " \
        "2295 2280 2296 2570 2577 2612 2528 2510 2557 2342 2381 2421 2456 2452 2393 2451 2437 2479 2296 2307 2290 " \
        "2405 2355 2490 2389 2418 2346 2629 2582 2647 2584 2564 2546 2658 2662 2759 2482 2492 2463 2471 2478 2403 " \
        "2605 2620 2645 2442 2445 2478 "
e = re.compile(r'(\d{4})\s?(\d{4})\s?(\d{4})')
data = e.findall(input_)
totalsr = 0
sr1, sr2 = 0, 0
mean = 0
R1, R2 = 0, 0
for i in range(30):
    sr1 += .5 * pow(float(data[i][0]) - float(data[i][1]), 2)
    sr2 += .5 * pow(float(data[i][0]) - float(data[i][2]), 2)
    mean += float(data[i][0]) / 30
for i in range(30):
    totalsr += .5 * pow(float(data[i][0]) - mean, 2)
R1 = 1 - sr1 / totalsr
R2 = 1 - sr2 / totalsr

# 2.
# a)
precision_A = 407 / 515
precision_B = 160 / 253
# b)
recall_A = 407 / 500
recall_B = 160 / 268


def F1_measure(precision, recall):
    return 2 * (precision * recall) / (precision + recall)


# c)
F1_A = F1_measure(precision_A, recall_A)
F1_B = F1_measure(precision_B, recall_B)
# d)
all_accuracy = (407 + 160) / 768
