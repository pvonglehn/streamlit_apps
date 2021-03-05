from random import randrange
from time import sleep
from typing import Generator, List

import altair as alt
import pandas as pd
import streamlit as st

MIN_ARRAY = 0
MAX_ARRAY = 100
FIGSIZE = (20, 10)


def initialize_array(n_elements: int, lower_limit: int, upper_limit: int) -> List:
    """Initialize random array"""

    return [randrange(lower_limit, upper_limit) for _ in range(n_elements)]


def bubble_sort(array: List) -> Generator:
    """Sort array in ascending order with bubble sort"""

    yield (array)

    max_unsorted = len(array)
    while max_unsorted > 1:
        for i in range(max_unsorted - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

                yield (array)

        max_unsorted -= 1


def plot_bar(array_snapshot: List, title: str, step: int) -> alt.Chart:
    """Plot barchart of array"""

    source = pd.DataFrame(
        {"array_index": range(len(array_snapshot)), "values": array_snapshot}
    )
    source["array_index"] = source["array_index"].astype(str)
    sort_by = source["array_index"].values
    chart = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            x=alt.X("array_index", sort=sort_by, axis=alt.Axis(tickCount=100)),
            y="values",
        )
        .properties(
            title={
                "text": title,
                "subtitle": f"step number: {step}",
            }
        )
        .configure_axisX(labelOverlap=True)
    )

    return chart


def run_algorithm(n_elements: int, chart_row: st.empty, delay: int) -> None:
    """Run algorithm and chart progress"""

    array = initialize_array(n_elements, MIN_ARRAY, MAX_ARRAY)
    bubble_sort_generator = bubble_sort(array)

    for step, array_snapshot in enumerate(bubble_sort_generator):
        chart = plot_bar(array_snapshot, "Bubble Sort", step)
        chart_row.altair_chart(chart, use_container_width=True)
        sleep(delay)


def main() -> None:
    chart_row = st.empty()
    n_elements = st.slider(value=20, min_value=0, max_value=100, label="# elements")
    speed = st.slider(value=5, min_value=2, max_value=100, step=1, label="speed")
    delay = 1 / speed

    run_algorithm(n_elements, chart_row, delay)


if __name__ == "__main__":
    main()
