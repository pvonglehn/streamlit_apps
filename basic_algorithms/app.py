from random import randrange
from time import sleep

import matplotlib.pyplot as plt
import streamlit as st


def initialize_array(n_elements, lower_limit, upper_limit):
    """initialize random array"""

    return [randrange(lower_limit, upper_limit) for _ in range(n_elements)]


def plot(array):
    """plot a barchart of array"""

    fig, ax = plt.subplots(figsize=(FIGSIZE))
    ax.bar(range(len(array)), array)

    return fig


def bubble_sort(array):
    """sort array in ascending order with bubble sort"""

    yield (array)

    max_unsorted = len(array)
    while max_unsorted > 1:
        for i in range(max_unsorted - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

                yield (array)

        max_unsorted -= 1


N_ELEMENTS = 20
MIN = 0
MAX = 100
FIGSIZE = (20, 10)
DELAY = 0.1

array = initialize_array(N_ELEMENTS, MIN, MAX)

array_gen = bubble_sort(array)

chart = st.empty()

for array_snapshot in array_gen:
    chart.bar_chart(array_snapshot)
    sleep(DELAY)
