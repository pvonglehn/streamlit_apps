from random import randrange
from time import sleep

import altair as alt
import pandas as pd
import streamlit as st


def initialize_array(n_elements, lower_limit, upper_limit):
    """initialize random array"""

    return [randrange(lower_limit, upper_limit) for _ in range(n_elements)]


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


def plot_bar(source, title):
    """plot barchart of array"""

    source = pd.DataFrame(
        {"array_index": range(len(array_snapshot)), "values": array_snapshot}
    )
    source["array_index"] = source["array_index"].astype(str)
    sort_by = source["array_index"].values
    chart = (
        alt.Chart(source)
        .mark_bar()
        .encode(x=alt.X("array_index", sort=sort_by), y="values")
        .properties(title=title)
    )

    return chart


N_ELEMENTS = 20
MIN = 0
MAX = 100
FIGSIZE = (20, 10)
DELAY = 0.1

array = initialize_array(N_ELEMENTS, MIN, MAX)

array_gen = bubble_sort(array)

chart_row = st.empty()

for array_snapshot in array_gen:
    chart = plot_bar(array_snapshot, "Bubble Sort")
    chart_row.altair_chart(chart)
    sleep(DELAY)
