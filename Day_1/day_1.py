#!/usr/bin/python

import sys


def measurement_increase(
    measurements: list,
    window_size: int = 1,
) -> int:
    """
    Provide a list of measurements in order and a sliding window size.
    Return an int quantifying the number of times the sliding window sum
    is greater than the prior window.
    """

    count = sum(m2 > m1 for m1, m2 in zip(measurements, measurements[window_size:]))

    return count


if __name__ == "__main__":
    measurements = []
    with open("1_input.txt") as file:
        for line in file:
            if not line.strip() == "":
                measurements.append(line.strip())
    measurements = [int(i) for i in measurements]

    print(
        "Number of measurement windows greater than the prior:",
        measurement_increase(measurements, window_size=int(sys.argv[1])),
    )
