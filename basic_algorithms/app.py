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


def plot_bar(array_snapshot, title):
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
        .properties(title=title, width=640)
    )

    return chart


N_ELEMENTS = st.sidebar.slider(value=20, min_value=0, max_value=100, label="# elements")
SPEED = st.sidebar.slider(
    value=5, min_value=2, max_value=100, step=1, label="steps per second"
)
DELAY = 1 / SPEED
MIN = 0
MAX = 100
FIGSIZE = (20, 10)


array = initialize_array(N_ELEMENTS, MIN, MAX)

array_gen = bubble_sort(array)

chart_row = st.empty()

for array_snapshot in array_gen:
    chart = plot_bar(array_snapshot, "Bubble Sort")
    chart_row.altair_chart(chart)
    sleep(DELAY)
