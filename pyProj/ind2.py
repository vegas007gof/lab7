#!/usr/bin/env python3
# -*- coding: utf-8 -*-

algebra = [
    [4, 3, 2, 4, 3, 3, 4, 4],
    [4, 2, 4, 5, 4, 2, 4, 3],
    [5, 5, 4, 5, 3, 3, 4, 3],
    [5, 5, 3, 4, 2, 4, 4, 3],
    [2, 5, 4, 2, 3, 4, 5, 5],
    [5, 5, 3, 5, 4, 3, 3, 3]
]
geometry = [
    [3, 3, 3, 5, 2, 5, 3, 2],
    [3, 4, 2, 2, 3, 4, 5, 5],
    [5, 5, 5, 4, 3, 5, 3, 5],
    [2, 2, 3, 2, 3, 3, 3, 5],
    [2, 3, 2, 3, 4, 5, 3, 5],
    [4, 4, 4, 3, 3, 3, 4, 5]
]
physics = [
    [3, 5, 2, 3, 5, 3, 5, 4],
    [3, 4, 2, 5, 5, 5, 2, 4],
    [5, 3, 3, 5, 4, 5, 3, 4],
    [5, 2, 3, 3, 5, 4, 4, 4],
    [5, 5, 3, 3, 4, 3, 3, 2],
    [5, 3, 5, 3, 4, 3, 3, 4]
]
average = 0
numberOfRations = 0
for i in algebra:
    average += sum(i)
    numberOfRations += len(i)
print(f'Средняя оценка по алгебре среди учеников: {average / numberOfRations}')

noDeuce = 0
for i in range(6):
    if not (2 in algebra[i] or 2 in geometry[i] or 2 in physics[i]):
        noDeuce += 1
print(f'Учеников, не имеющих двойки по предметам: {noDeuce}')