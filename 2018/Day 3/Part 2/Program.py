grid = []
for i in range(0, 2000):
    grid.append([])
    for r in range(0, 2000):
        grid[i].append(0)
input = [[257, 829, 10, 23], [902, 685, 10, 20], [107, 733, 20, 25], [186, 421, 20, 11], [360, 229, 29, 10], [362, 248, 24, 10], [922, 250, 13, 26], [256, 742, 18, 14], [344, 569, 28, 15], [381, 793, 13, 16], [456, 936, 28, 27], [110, 25, 21, 13], [974, 739, 12, 12], [364, 641, 17, 7], [223, 935, 24, 25], [803, 147, 20, 17], [928, 694, 13, 12], [549, 438, 13, 29], [836, 706, 18, 25], [890, 557, 25, 18], [790, 671, 16, 19], [433, 548, 22, 20], [341, 291, 21, 5], [324, 168, 12, 21], [696, 677, 12, 12], [480, 769, 16, 25], [966, 125, 13, 26], [889, 760, 18, 26], [708, 275, 19, 13], [581, 706, 25, 12], [334, 387, 29, 23], [292, 246, 29, 22], [299, 500, 24, 23], [834, 644, 28, 27], [510, 172, 27, 14], [24, 35, 27, 15], [801, 484, 22, 28], [974, 891, 22, 26], [633, 281, 27, 10], [523, 582, 19, 28], [417, 878, 13, 21], [712, 897, 12, 27], [899, 927, 16, 27], [269, 693, 16, 28], [42, 356, 11, 15], [547, 849, 24, 27], [706, 394, 29, 27], [768, 325, 10, 27], [289, 823, 11, 11], [561, 758, 4, 3], [193, 226, 27, 19], [501, 584, 21, 25], [481, 898, 11, 12], [516, 588, 23, 29], [2, 952, 28, 22], [238, 706, 14, 23], [28, 782, 10, 28], [642, 873, 28, 20], [853, 310, 12, 26], [889, 242, 21, 20], [351, 305, 16, 21], [799, 981, 10, 13], [276, 590, 19, 18], [645, 874, 21, 24], [276, 886, 22, 22], [874, 840, 24, 10], [700, 653, 18, 29], [853, 676, 21, 13], [763, 53, 10, 14], [17, 887, 11, 15], [876, 860, 20, 15], [930, 561, 11, 11], [299, 467, 26, 16], [233, 741, 29, 13], [388, 776, 13, 27], [310, 521, 29, 25], [644, 963, 29, 18], [238, 804, 13, 25], [8, 767, 18, 26], [936, 237, 27, 12], [866, 607, 13, 16], [500, 917, 20, 15], [176, 579, 22, 22], [294, 251, 19, 12], [500, 169, 21, 16], [704, 954, 14, 11], [890, 741, 24, 19], [49, 956, 21, 25], [544, 270, 19, 18], [324, 911, 29, 26], [100, 615, 16, 18], [656, 946, 25, 21], [537, 169, 13, 22], [201, 303, 22, 22], [579, 753, 12, 10], [853, 554, 23, 27], [393, 731, 29, 19], [955, 618, 24, 10], [79, 64, 15, 16], [277, 408, 26, 27], [770, 263, 29, 24], [408, 812, 18, 10], [907, 612, 10, 28], [28, 701, 20, 16], [290, 821, 16, 27], [632, 698, 17, 20], [901, 513, 10, 26], [316, 580, 14, 22], [501, 383, 25, 10], [125, 212, 28, 19], [296, 379, 14, 29], [63, 253, 21, 11], [234, 490, 28, 10], [526, 481, 12, 29], [963, 620, 28, 10], [484, 759, 14, 13], [831, 423, 11, 11], [223, 156, 16, 22], [842, 698, 25, 20], [472, 809, 24, 28], [118, 488, 16, 14], [202, 818, 18, 23], [633, 564, 20, 20], [787, 611, 20, 22], [687, 49, 16, 27], [157, 617, 26, 10], [349, 266, 22, 13], [203, 455, 15, 14], [747, 335, 24, 26], [288, 709, 24, 16], [256, 565, 27, 24], [246, 698, 14, 11], [403, 860, 14, 13], [451, 715, 14, 18], [956, 933, 24, 14], [231, 565, 17, 29], [597, 138, 23, 14], [653, 607, 27, 15], [560, 977, 22, 10], [636, 360, 13, 20], [931, 520, 19, 20], [725, 714, 23, 24], [881, 852, 18, 23], [626, 342, 15, 23], [521, 338, 15, 12], [100, 651, 18, 11], [498, 172, 29, 18], [12, 975, 22, 24], [516, 783, 23, 21], [406, 434, 28, 20], [25, 598, 17, 10], [460, 321, 14, 29], [667, 324, 20, 14], [444, 439, 28, 17], [275, 388, 20, 17], [624, 265, 14, 17], [892, 770, 11, 11], [6, 769, 16, 19], [621, 733, 29, 21], [368, 884, 24, 16], [108, 167, 26, 19], [955, 730, 11, 12], [639, 717, 15, 26], [89, 329, 20, 28], [183, 616, 21, 11], [161, 499, 27, 29], [506, 934, 11, 12], [879, 309, 13, 10], [562, 663, 24, 14], [663, 57, 27, 14], [746, 43, 27, 10], [588, 389, 11, 14], [516, 953, 17, 13], [678, 676, 13, 25], [869, 624, 26, 15], [953, 876, 24, 22], [328, 743, 25, 20], [629, 805, 21, 24], [650, 601, 14, 20], [496, 804, 29, 28], [281, 54, 15, 22], [112, 632, 13, 21], [206, 399, 11, 13], [952, 608, 20, 15], [27, 279, 26, 27], [534, 182, 17, 26], [924, 720, 13, 20], [487, 980, 12, 11], [793, 171, 20, 13], [930, 971, 17, 10], [824, 947, 27, 12], [474, 777, 29, 11], [655, 830, 18, 28], [508, 540, 21, 12], [85, 70, 29, 14], [498, 929, 19, 16], [267, 394, 15, 20], [438, 891, 13, 24], [372, 433, 19, 29], [22, 932, 16, 6], [835, 568, 28, 10], [889, 893, 15, 22], [534, 181, 15, 13], [206, 213, 10, 22], [947, 764, 14, 25], [332, 830, 28, 26], [664, 677, 12, 11], [804, 602, 12, 11], [385, 483, 26, 24], [806, 372, 12, 15], [880, 841, 29, 13], [354, 253, 24, 26], [367, 695, 21, 27], [388, 617, 28, 22], [292, 112, 16, 15], [61, 787, 25, 17], [428, 862, 16, 25], [23, 265, 17, 11], [717, 960, 11, 13], [416, 776, 20, 24], [29, 230, 18, 11], [681, 11, 24, 25], [930, 517, 19, 14], [801, 256, 15, 12], [218, 948, 27, 18], [697, 406, 23, 27], [201, 761, 11, 17], [692, 278, 17, 17], [454, 330, 22, 18], [161, 743, 11, 7], [51, 213, 15, 25], [182, 979, 15, 13], [737, 0, 27, 18], [404, 631, 21, 29], [263, 356, 26, 27], [24, 799, 29, 16], [881, 328, 10, 12], [960, 759, 8, 7], [12, 987, 26, 12], [642, 886, 18, 28], [180, 817, 26, 20], [824, 428, 13, 11], [204, 784, 11, 27], [495, 789, 10, 18], [96, 826, 14, 24], [758, 677, 16, 22], [935, 834, 12, 26], [151, 741, 26, 12], [554, 595, 26, 14], [623, 284, 19, 10], [574, 255, 16, 10], [886, 881, 13, 16], [476, 0, 17, 11], [805, 100, 12, 16], [383, 500, 23, 26], [155, 452, 15, 12], [310, 694, 28, 28], [518, 788, 17, 10], [897, 862, 13, 16], [269, 395, 26, 15], [766, 978, 10, 22], [935, 962, 19, 23], [700, 282, 25, 23], [342, 6, 20, 24], [818, 661, 27, 29], [816, 809, 23, 28], [813, 848, 11, 12], [112, 285, 10, 24], [38, 272, 16, 18], [277, 361, 16, 10], [421, 687, 17, 11], [942, 827, 12, 12], [331, 913, 15, 19], [880, 218, 25, 21], [655, 587, 24, 27], [537, 739, 13, 12], [759, 812, 13, 29], [926, 238, 15, 25], [229, 482, 15, 21], [917, 772, 21, 27], [390, 706, 3, 18], [972, 703, 14, 16], [412, 614, 7, 4], [583, 135, 12, 28], [516, 908, 27, 17], [20, 930, 22, 12], [318, 394, 25, 12], [677, 665, 29, 29], [345, 404, 15, 11], [83, 48, 26, 28], [298, 125, 22, 19], [509, 929, 28, 17], [549, 927, 27, 13], [801, 644, 22, 22], [552, 560, 24, 24], [809, 100, 16, 23], [105, 686, 12, 20], [620, 612, 15, 17], [739, 707, 13, 13], [853, 627, 24, 21], [244, 149, 21, 27], [265, 582, 13, 12], [945, 184, 18, 29], [808, 418, 15, 28], [221, 762, 13, 17], [612, 684, 21, 17], [445, 758, 28, 21], [950, 273, 15, 16], [850, 303, 12, 15], [394, 285, 16, 10], [327, 5, 22, 29], [69, 435, 24, 20], [0, 532, 14, 14], [373, 950, 13, 15], [170, 89, 21, 27], [754, 36, 15, 22], [680, 266, 29, 22], [388, 450, 29, 21], [867, 471, 25, 28], [336, 278, 27, 14], [880, 816, 14, 28], [547, 278, 24, 29], [762, 824, 6, 4], [179, 492, 13, 13], [382, 289, 17, 27], [867, 461, 17, 16], [246, 495, 10, 16], [960, 200, 12, 15], [766, 19, 23, 12], [158, 119, 10, 24], [385, 919, 11, 19], [804, 637, 27, 11], [539, 841, 19, 23], [115, 963, 26, 28], [864, 465, 22, 10], [325, 679, 23, 10], [716, 414, 11, 21], [599, 636, 13, 22], [202, 816, 23, 16], [596, 652, 24, 17], [897, 253, 18, 14], [558, 192, 11, 24], [277, 839, 20, 14], [271, 671, 17, 16], [315, 407, 19, 27], [217, 934, 11, 20], [50, 336, 27, 17], [286, 823, 23, 21], [145, 351, 24, 10], [681, 802, 11, 27], [482, 240, 24, 21], [544, 629, 17, 22], [418, 511, 15, 26], [301, 251, 14, 20], [196, 969, 27, 26], [314, 687, 16, 19], [713, 10, 25, 21], [963, 626, 20, 13], [831, 771, 24, 18], [853, 546, 14, 13], [843, 804, 23, 13], [22, 941, 22, 10], [720, 967, 18, 15], [718, 956, 27, 25], [131, 975, 25, 21], [216, 668, 16, 20], [370, 902, 21, 10], [794, 694, 27, 14], [669, 220, 27, 24], [89, 659, 23, 12], [283, 257, 11, 18], [240, 306, 19, 20], [941, 160, 29, 18], [421, 709, 18, 18], [655, 603, 20, 27], [290, 879, 17, 20], [873, 598, 10, 22], [555, 653, 28, 19], [91, 666, 20, 16], [263, 488, 26, 27], [596, 330, 22, 23], [237, 773, 27, 19], [351, 76, 14, 25], [129, 221, 25, 27], [424, 820, 11, 23], [225, 952, 12, 18], [215, 869, 20, 25], [405, 644, 19, 19], [858, 19, 17, 28], [829, 252, 22, 10], [119, 167, 27, 19], [335, 196, 27, 11], [97, 677, 14, 13], [588, 931, 27, 27], [606, 293, 20, 24], [930, 964, 20, 20], [12, 273, 24, 23], [567, 107, 15, 18], [150, 354, 24, 10], [913, 732, 25, 19], [916, 960, 29, 13], [443, 924, 28, 16], [354, 158, 11, 29], [364, 471, 26, 22], [603, 132, 14, 29], [60, 548, 13, 23], [399, 453, 16, 11], [964, 728, 11, 13], [8, 1, 23, 15], [18, 491, 23, 11], [641, 948, 11, 22], [367, 359, 18, 29], [624, 694, 18, 24], [670, 939, 20, 24], [665, 500, 20, 29], [525, 881, 23, 14], [317, 737, 16, 24], [651, 151, 17, 12], [479, 84, 14, 17], [684, 820, 12, 29], [491, 618, 20, 15], [718, 880, 11, 23], [831, 404, 15, 25], [381, 950, 12, 20], [606, 634, 10, 17], [227, 786, 18, 18], [536, 180, 25, 22], [859, 177, 20, 12], [460, 534, 20, 25], [884, 940, 22, 24], [171, 836, 22, 21], [32, 355, 11, 27], [157, 828, 15, 28], [636, 468, 16, 29], [883, 511, 16, 27], [51, 331, 15, 12], [807, 501, 18, 12], [62, 180, 13, 12], [312, 528, 19, 15], [166, 511, 13, 14], [482, 611, 12, 12], [210, 579, 11, 22], [728, 625, 14, 17], [456, 717, 13, 21], [606, 273, 12, 21], [303, 466, 22, 15], [976, 355, 19, 12], [720, 771, 11, 13], [290, 274, 12, 24], [11, 807, 12, 25], [409, 660, 15, 12], [913, 523, 26, 14], [438, 897, 10, 11], [50, 270, 17, 21], [290, 423, 15, 16], [688, 235, 10, 15], [982, 343, 16, 26], [714, 779, 27, 13], [655, 667, 13, 24], [877, 221, 10, 15], [695, 674, 17, 22], [804, 159, 15, 17], [935, 682, 28, 23], [32, 190, 25, 14], [917, 691, 24, 25], [440, 369, 25, 12], [125, 193, 23, 24], [362, 638, 24, 29], [686, 89, 28, 15], [899, 495, 23, 19], [760, 679, 29, 22], [727, 206, 7, 10], [406, 446, 21, 24], [26, 333, 17, 29], [913, 952, 20, 24], [548, 628, 16, 10], [155, 872, 24, 28], [389, 904, 22, 23], [539, 210, 16, 12], [871, 680, 13, 19], [556, 595, 13, 11], [129, 531, 19, 16], [671, 637, 25, 25], [323, 698, 21, 29], [591, 617, 15, 14], [343, 252, 20, 18], [437, 206, 15, 10], [291, 408, 23, 29], [678, 92, 17, 28], [888, 233, 10, 29], [215, 831, 14, 17], [570, 752, 24, 13], [751, 331, 18, 27], [715, 956, 16, 19], [300, 679, 17, 16], [500, 392, 20, 17], [332, 704, 24, 17], [505, 499, 27, 20], [318, 473, 13, 28], [961, 528, 14, 15], [572, 190, 20, 29], [668, 762, 12, 19], [784, 38, 27, 13], [31, 253, 29, 12], [940, 849, 26, 14], [877, 88, 17, 26], [740, 714, 20, 23], [671, 373, 21, 16], [418, 713, 23, 12], [731, 649, 24, 24], [32, 279, 29, 21], [712, 907, 27, 23], [948, 516, 19, 24], [372, 177, 13, 20], [746, 936, 11, 13], [102, 828, 4, 18], [445, 18, 19, 22], [371, 84, 18, 26], [882, 80, 21, 26], [337, 906, 17, 28], [559, 749, 11, 17], [947, 303, 24, 29], [504, 945, 17, 23], [24, 801, 15, 22], [527, 810, 15, 28], [382, 305, 12, 10], [248, 568, 15, 24], [931, 735, 10, 20], [468, 773, 10, 23], [616, 255, 19, 22], [529, 873, 19, 25], [548, 799, 15, 24], [377, 165, 28, 13], [200, 638, 21, 17], [178, 758, 16, 17], [65, 940, 22, 20], [229, 679, 24, 10], [196, 906, 7, 7], [167, 518, 15, 10], [974, 455, 26, 28], [756, 49, 17, 21], [844, 632, 21, 10], [44, 532, 11, 22], [153, 612, 19, 10], [756, 34, 17, 14], [507, 233, 11, 26], [983, 759, 12, 11], [600, 41, 25, 18], [350, 403, 17, 19], [392, 624, 26, 10], [725, 862, 28, 21], [808, 315, 11, 21], [848, 771, 29, 10], [193, 954, 26, 22], [869, 909, 14, 10], [569, 677, 26, 28], [482, 11, 24, 16], [974, 474, 23, 26], [932, 830, 16, 19], [14, 262, 16, 19], [367, 902, 28, 26], [169, 485, 16, 11], [724, 637, 25, 15], [371, 609, 26, 11], [6, 829, 17, 20], [887, 827, 22, 17], [22, 31, 19, 12], [268, 702, 23, 18], [98, 232, 14, 14], [446, 700, 10, 29], [774, 780, 12, 27], [624, 168, 20, 14], [814, 297, 23, 23], [419, 526, 25, 27], [441, 885, 13, 20], [890, 698, 25, 21], [1, 900, 21, 29], [328, 917, 13, 20], [963, 189, 26, 22], [858, 87, 16, 12], [954, 816, 19, 29], [566, 129, 23, 18], [888, 811, 19, 27], [753, 313, 29, 21], [414, 71, 29, 10], [734, 423, 23, 13], [445, 315, 23, 13], [834, 295, 23, 16], [545, 172, 13, 25], [201, 280, 22, 18], [876, 825, 24, 15], [877, 665, 12, 27], [940, 800, 19, 11], [101, 144, 27, 25], [940, 459, 19, 26], [800, 588, 23, 20], [204, 886, 10, 21], [873, 891, 15, 19], [59, 329, 25, 15], [681, 847, 22, 18], [86, 624, 11, 29], [901, 600, 23, 13], [562, 257, 25, 19], [960, 818, 10, 23], [885, 298, 29, 18], [370, 149, 27, 24], [706, 395, 16, 17], [920, 22, 27, 19], [407, 612, 20, 12], [494, 596, 23, 15], [36, 597, 17, 27], [92, 233, 23, 15], [537, 457, 13, 21], [835, 125, 29, 14], [918, 724, 20, 13], [242, 925, 18, 14], [209, 859, 17, 17], [466, 140, 17, 21], [415, 777, 21, 28], [490, 7, 13, 20], [423, 913, 26, 23], [296, 599, 10, 28], [498, 577, 26, 16], [773, 659, 13, 15], [263, 847, 13, 17], [741, 375, 28, 26], [100, 808, 4, 3], [525, 308, 18, 26], [955, 940, 15, 28], [432, 367, 22, 24], [580, 693, 6, 3], [483, 628, 10, 11], [822, 479, 25, 25], [533, 561, 12, 23], [711, 270, 13, 24], [932, 951, 23, 24], [684, 683, 17, 26], [236, 537, 19, 28], [953, 217, 21, 23], [248, 155, 14, 18], [761, 627, 20, 23], [343, 864, 13, 13], [8, 538, 20, 19], [568, 547, 17, 25], [20, 945, 18, 23], [612, 256, 25, 12], [302, 964, 6, 17], [570, 901, 11, 22], [184, 429, 25, 13], [257, 224, 25, 24], [63, 448, 29, 11], [927, 499, 11, 23], [501, 228, 11, 23], [291, 606, 20, 20], [857, 26, 16, 16], [648, 779, 13, 22], [216, 304, 10, 15], [349, 856, 18, 29], [10, 939, 21, 26], [287, 894, 18, 17], [888, 680, 13, 15], [288, 358, 19, 29], [106, 203, 22, 25], [387, 268, 25, 27], [466, 122, 20, 29], [590, 650, 25, 12], [978, 488, 22, 11], [112, 861, 19, 14], [20, 885, 22, 12], [820, 99, 13, 21], [420, 898, 23, 27], [869, 605, 29, 26], [123, 471, 25, 23], [652, 564, 17, 28], [414, 883, 23, 11], [890, 529, 22, 27], [406, 372, 25, 29], [39, 180, 27, 20], [12, 928, 16, 29], [516, 301, 10, 21], [681, 314, 25, 28], [980, 764, 18, 29], [879, 571, 16, 12], [561, 511, 22, 24], [226, 257, 16, 10], [269, 580, 11, 16], [217, 473, 20, 26], [493, 587, 21, 27], [19, 767, 27, 23], [369, 802, 14, 11], [656, 976, 25, 22], [504, 592, 11, 24], [143, 677, 11, 22], [554, 971, 12, 25], [968, 698, 28, 29], [290, 838, 23, 18], [572, 419, 28, 19], [459, 554, 13, 17], [393, 375, 29, 14], [646, 968, 12, 22], [917, 18, 25, 24], [534, 921, 20, 23], [217, 679, 18, 19], [476, 792, 22, 28], [844, 833, 7, 13], [215, 583, 18, 23], [688, 18, 8, 14], [974, 916, 25, 18], [214, 842, 12, 18], [254, 316, 24, 22], [831, 722, 8, 15], [217, 256, 23, 20], [956, 281, 12, 16], [923, 797, 16, 11], [788, 40, 11, 18], [422, 193, 22, 17], [475, 84, 17, 18], [869, 61, 24, 29], [266, 189, 12, 21], [514, 472, 18, 10], [344, 314, 13, 12], [43, 679, 26, 28], [943, 845, 26, 12], [287, 235, 28, 27], [503, 615, 24, 24], [436, 37, 10, 18], [312, 576, 23, 10], [934, 178, 21, 29], [925, 693, 16, 12], [272, 722, 19, 18], [66, 539, 12, 14], [117, 429, 14, 23], [213, 557, 23, 17], [293, 70, 18, 28], [804, 578, 19, 10], [683, 694, 28, 24], [14, 280, 18, 6], [134, 197, 22, 12], [928, 398, 12, 12], [407, 48, 14, 29], [440, 702, 14, 16], [173, 504, 20, 24], [572, 559, 29, 20], [421, 890, 23, 28], [605, 628, 21, 26], [497, 940, 18, 19], [61, 99, 24, 20], [50, 212, 11, 28], [314, 185, 28, 15], [190, 897, 22, 25], [97, 75, 16, 29], [287, 369, 15, 11], [435, 218, 11, 25], [403, 720, 22, 15], [353, 696, 19, 17], [323, 2, 25, 20], [744, 581, 19, 26], [294, 962, 26, 22], [567, 7, 13, 27], [974, 116, 21, 13], [781, 767, 22, 27], [790, 657, 24, 21], [860, 622, 11, 15], [547, 163, 24, 26], [794, 156, 12, 20], [691, 836, 13, 16], [576, 118, 27, 26], [841, 132, 29, 11], [210, 582, 24, 24], [377, 703, 20, 25], [844, 558, 15, 19], [860, 636, 18, 23], [246, 788, 23, 28], [894, 567, 15, 17], [284, 892, 26, 15], [931, 479, 12, 26], [116, 684, 26, 13], [345, 855, 21, 10], [725, 204, 13, 16], [781, 257, 23, 19], [677, 959, 28, 14], [535, 813, 17, 19], [538, 806, 12, 19], [184, 501, 22, 17], [596, 661, 12, 15], [3, 784, 16, 21], [556, 880, 16, 23], [626, 896, 17, 11], [944, 823, 16, 13], [13, 357, 20, 15], [363, 73, 18, 22], [896, 304, 28, 26], [455, 519, 16, 14], [2, 957, 14, 26], [148, 552, 28, 15], [880, 397, 13, 17], [759, 676, 11, 26], [957, 733, 5, 5], [450, 892, 26, 12], [877, 203, 23, 22], [500, 533, 17, 23], [533, 474, 21, 24], [169, 797, 17, 26], [283, 367, 25, 27], [797, 325, 25, 17], [114, 214, 22, 19], [462, 317, 15, 11], [416, 530, 28, 16], [562, 167, 17, 21], [472, 73, 27, 14], [397, 669, 29, 19], [267, 690, 16, 18], [412, 567, 21, 18], [43, 458, 11, 16], [350, 236, 28, 24], [746, 35, 17, 27], [665, 176, 7, 5], [482, 3, 10, 15], [877, 908, 15, 18], [537, 210, 27, 12], [41, 795, 29, 20], [560, 174, 10, 10], [267, 380, 15, 10], [852, 584, 25, 22], [955, 937, 17, 21], [212, 232, 10, 21], [396, 498, 27, 10], [176, 285, 25, 29], [96, 460, 28, 11], [132, 56, 23, 29], [457, 85, 22, 14], [832, 949, 22, 14], [745, 615, 14, 10], [295, 879, 11, 16], [357, 451, 21, 18], [74, 944, 13, 26], [943, 124, 24, 16], [202, 641, 19, 26], [877, 276, 22, 19], [14, 546, 13, 21], [925, 699, 29, 16], [55, 205, 28, 18], [45, 526, 14, 19], [270, 692, 22, 15], [375, 916, 12, 18], [463, 311, 12, 20], [754, 348, 15, 12], [348, 433, 14, 27], [69, 335, 29, 22], [205, 611, 23, 12], [333, 514, 17, 27], [557, 905, 25, 24], [824, 785, 10, 17], [983, 494, 13, 16], [391, 926, 12, 24], [369, 366, 12, 7], [370, 456, 19, 12], [106, 729, 11, 13], [126, 420, 12, 18], [968, 504, 23, 18], [887, 140, 20, 26], [780, 696, 14, 28], [405, 753, 22, 20], [965, 899, 17, 21], [855, 56, 12, 25], [225, 149, 23, 28], [834, 829, 10, 25], [205, 133, 23, 10], [219, 125, 27, 15], [267, 819, 28, 28], [583, 172, 15, 28], [320, 52, 20, 28], [380, 675, 25, 29], [440, 199, 10, 28], [553, 927, 29, 12], [124, 458, 10, 17], [326, 7, 25, 29], [933, 165, 14, 28], [440, 707, 24, 21], [870, 803, 22, 17], [134, 899, 10, 15], [378, 951, 13, 18], [908, 745, 14, 13], [144, 202, 26, 11], [685, 363, 10, 21], [327, 159, 3, 10], [215, 569, 18, 17], [872, 308, 13, 14], [55, 894, 18, 27], [697, 899, 21, 29], [447, 954, 20, 25], [76, 330, 28, 13], [817, 378, 12, 25], [696, 235, 21, 20], [121, 460, 10, 29], [307, 76, 19, 23], [99, 346, 14, 11], [534, 170, 16, 28], [180, 474, 11, 27], [315, 159, 25, 21], [975, 107, 14, 21], [116, 277, 27, 17], [959, 516, 20, 20], [495, 749, 17, 16], [334, 230, 10, 26], [742, 822, 21, 18], [138, 886, 11, 22], [30, 442, 24, 19], [922, 571, 17, 17], [276, 572, 19, 21], [878, 408, 18, 14], [665, 726, 11, 17], [73, 260, 20, 13], [956, 897, 15, 15], [891, 321, 28, 23], [185, 266, 29, 24], [648, 160, 14, 19], [670, 760, 14, 14], [9, 659, 16, 22], [145, 680, 5, 9], [527, 439, 26, 22], [599, 592, 26, 29], [208, 204, 22, 19], [588, 42, 15, 20], [904, 500, 28, 21], [792, 116, 29, 27], [7, 656, 29, 11], [704, 920, 12, 29], [122, 528, 19, 15], [92, 637, 23, 15], [867, 756, 22, 28], [190, 489, 11, 22], [207, 604, 14, 18], [712, 273, 29, 17], [961, 18, 21, 29], [447, 318, 14, 23], [519, 912, 18, 19], [515, 589, 29, 22], [648, 818, 21, 22], [368, 415, 26, 24], [16, 345, 14, 13], [634, 708, 13, 10], [843, 667, 26, 23], [373, 459, 16, 19], [899, 873, 22, 22], [256, 480, 10, 19], [505, 236, 19, 10], [571, 530, 22, 28], [333, 771, 15, 28], [230, 923, 17, 13], [786, 566, 28, 29], [541, 274, 14, 11], [889, 85, 27, 22], [603, 445, 26, 27], [888, 458, 28, 14], [165, 123, 14, 16], [721, 81, 22, 23], [621, 470, 19, 20], [290, 391, 17, 28], [363, 617, 22, 17], [527, 198, 17, 22], [945, 851, 17, 11], [549, 864, 28, 28], [833, 863, 19, 20], [960, 603, 18, 26], [506, 131, 5, 21], [592, 630, 14, 15], [72, 429, 13, 24], [553, 153, 16, 25], [776, 601, 29, 21], [904, 460, 7, 7], [423, 498, 29, 27], [12, 953, 12, 13], [198, 664, 21, 24], [765, 636, 21, 19], [787, 299, 29, 29], [966, 495, 10, 27], [314, 546, 28, 26], [810, 316, 15, 20], [725, 778, 24, 13], [829, 414, 15, 10], [739, 928, 12, 14], [656, 98, 28, 27], [146, 74, 3, 6], [642, 791, 20, 11], [887, 281, 26, 23], [511, 373, 18, 26], [13, 538, 19, 15], [845, 249, 29, 12], [205, 466, 11, 28], [12, 494, 19, 19], [508, 936, 3, 5], [543, 268, 20, 18], [955, 29, 29, 10], [925, 780, 10, 12], [412, 168, 23, 26], [719, 957, 14, 27], [809, 833, 18, 27], [800, 404, 18, 29], [225, 935, 14, 17], [638, 566, 11, 12], [140, 72, 29, 12], [217, 755, 17, 16], [508, 608, 18, 12], [546, 720, 15, 25], [502, 380, 29, 19], [429, 524, 27, 19], [334, 787, 15, 18], [217, 949, 14, 26], [288, 523, 26, 22], [534, 936, 24, 22], [314, 404, 13, 15], [50, 228, 21, 25], [584, 124, 15, 28], [882, 110, 17, 25], [208, 955, 12, 25], [30, 347, 27, 25], [371, 898, 21, 14], [756, 388, 20, 28], [184, 889, 27, 16], [964, 461, 17, 13], [389, 764, 21, 29], [712, 706, 15, 22], [420, 191, 11, 20], [711, 650, 11, 29], [361, 847, 21, 16], [722, 418, 24, 20], [598, 690, 25, 28], [753, 978, 18, 17], [251, 676, 18, 14], [191, 405, 24, 13], [830, 870, 24, 10], [373, 801, 21, 17], [956, 593, 14, 23], [380, 949, 29, 17], [703, 765, 19, 29], [82, 672, 10, 11], [17, 228, 20, 17], [531, 343, 25, 23], [197, 282, 13, 15], [169, 580, 27, 14], [340, 156, 20, 18], [328, 820, 14, 12], [187, 565, 29, 19], [872, 178, 13, 22], [810, 502, 29, 14], [543, 519, 22, 25], [460, 726, 19, 24], [191, 904, 16, 14], [190, 198, 23, 22], [666, 197, 13, 22], [356, 789, 14, 22], [639, 181, 17, 14], [596, 643, 27, 11], [961, 317, 10, 18], [433, 768, 17, 20], [52, 795, 28, 10], [352, 801, 12, 17], [669, 738, 20, 16], [101, 863, 22, 15], [803, 141, 17, 23], [198, 472, 22, 16], [642, 518, 24, 15], [440, 273, 27, 19], [588, 927, 16, 24], [303, 563, 27, 22], [689, 721, 28, 16], [836, 874, 19, 15], [752, 809, 21, 28], [790, 242, 22, 26], [435, 204, 11, 29], [608, 291, 25, 12], [176, 419, 18, 28], [598, 372, 12, 26], [890, 293, 19, 14], [569, 33, 20, 25], [127, 803, 29, 17], [552, 169, 24, 14], [983, 484, 15, 27], [772, 662, 12, 28], [678, 178, 19, 23], [277, 899, 29, 21], [588, 229, 12, 29], [844, 229, 25, 25], [688, 913, 22, 26], [470, 882, 22, 21], [813, 678, 10, 29], [427, 181, 23, 19], [8, 941, 26, 19], [946, 802, 16, 10], [646, 610, 17, 14], [701, 281, 26, 10], [240, 217, 22, 18], [120, 214, 29, 18], [854, 794, 18, 19], [179, 767, 13, 11], [250, 383, 23, 29], [519, 277, 13, 10], [395, 618, 11, 10], [886, 893, 17, 23], [429, 436, 19, 17], [200, 938, 29, 10], [124, 794, 24, 14], [874, 265, 10, 15], [483, 784, 20, 29], [489, 933, 13, 28], [222, 932, 23, 27], [714, 633, 21, 29], [761, 322, 15, 20], [83, 347, 24, 12], [523, 889, 23, 28], [101, 672, 16, 23], [936, 704, 16, 27], [861, 236, 17, 25], [951, 125, 24, 26], [688, 681, 15, 11], [391, 758, 27, 23], [808, 778, 9, 5], [831, 238, 10, 25], [204, 474, 9, 10], [625, 813, 16, 15], [45, 886, 17, 23], [561, 938, 18, 13], [350, 880, 27, 14], [628, 401, 18, 22], [488, 807, 27, 28], [848, 947, 14, 11], [863, 76, 15, 28], [174, 893, 27, 29], [894, 483, 22, 29], [680, 78, 22, 27], [748, 604, 21, 11], [855, 759, 14, 13], [953, 117, 12, 27], [930, 402, 3, 4], [663, 174, 12, 10], [396, 869, 18, 16], [451, 559, 12, 13], [709, 79, 16, 11], [804, 970, 10, 25], [339, 287, 27, 13], [181, 961, 25, 13], [553, 208, 11, 26], [192, 417, 10, 28], [77, 92, 19, 27], [796, 121, 22, 24], [194, 616, 11, 14], [595, 147, 15, 29], [84, 437, 26, 28], [338, 87, 16, 29], [806, 774, 14, 13], [841, 880, 15, 16], [650, 491, 15, 29], [501, 498, 22, 20], [611, 632, 15, 11], [753, 732, 28, 26], [199, 966, 23, 14], [873, 812, 14, 3], [25, 12, 16, 15], [96, 800, 16, 22], [354, 716, 12, 18], [612, 404, 25, 13], [193, 897, 12, 11], [284, 376, 16, 19], [203, 636, 16, 25], [797, 583, 28, 22], [558, 259, 29, 23], [391, 930, 17, 11], [120, 459, 18, 18], [708, 270, 23, 14], [474, 974, 29, 20], [872, 333, 24, 15], [67, 183, 16, 19], [915, 799, 23, 14], [662, 437, 17, 15], [925, 831, 20, 22], [977, 500, 20, 11], [475, 766, 25, 21], [281, 677, 17, 28], [425, 562, 17, 29], [542, 568, 10, 22], [702, 684, 28, 11], [157, 221, 25, 29], [490, 606, 28, 18], [654, 432, 17, 21], [523, 271, 23, 26], [15, 937, 28, 13], [379, 196, 18, 21], [337, 730, 26, 11], [840, 256, 16, 13], [651, 955, 13, 13], [174, 225, 10, 16], [188, 212, 27, 20], [553, 184, 11, 10], [504, 129, 10, 28], [344, 568, 10, 10], [951, 788, 23, 22], [212, 552, 28, 28], [775, 577, 26, 22], [957, 757, 15, 29], [56, 956, 15, 10], [833, 931, 16, 19], [880, 447, 14, 23], [430, 840, 23, 25], [673, 641, 14, 28], [242, 187, 28, 18], [757, 7, 20, 28], [149, 450, 12, 27], [37, 248, 23, 20], [335, 712, 21, 23], [839, 767, 27, 24], [721, 605, 27, 15], [611, 334, 11, 26], [515, 933, 25, 13], [210, 772, 29, 10], [492, 789, 16, 16], [188, 82, 24, 15], [877, 304, 26, 14], [829, 713, 15, 29], [172, 510, 23, 28], [842, 828, 15, 23], [88, 161, 24, 13], [463, 290, 13, 22], [682, 230, 22, 12], [713, 911, 29, 25], [317, 157, 26, 16], [894, 150, 16, 28], [906, 551, 14, 23], [131, 562, 23, 28], [127, 33, 22, 23], [134, 50, 14, 24], [591, 409, 12, 20], [218, 554, 18, 26]]
for item in input:
    for l in range(0, int(item[2])):
        for i in range(0, item[3]):
            obj1 = item[0] + l
            obj2 = item[1] + i
            grid[obj1][obj2] += 1

for item in input:
    score = 0
    for l in range(0, int(item[2])):
        for i in range(0, item[3]):
            obj1 = item[0] + l
            obj2 = item[1] + i
            if grid[obj1][obj2] == 1:
                score += 1
    if score == item[2] * item[3]:
        print(input.index(item)+1)
