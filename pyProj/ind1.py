#!/usr/bin/env python3
# -*- coding: utf-8 -*-

elements = [1.989, 0.117, -1.363, 1.098, 0.039, 0.949, -0.026, 1.039, -0.842, 1.339]
sumOfOdd = 0
for i in range(len(elements)):
    if (i + 1) % 2 != 0:
        sumOfOdd += elements[i]
print(f'Сумма элементов с нечетными номерами: {round(sumOfOdd, 3)}')

indices = []
for i in elements:
    if i < 0:
        indices.append(elements.index(i))

print(f'Сумма элементов между первым и последним отрицательными значениями:'
      f' {sum(elements[(indices[0] + 1):(indices[-1])])}')
