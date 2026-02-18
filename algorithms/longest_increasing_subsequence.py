from bisect import bisect


def patience_sorting(array):
    patient_result_sorted = []
    active_indices = []
    for i, number in enumerate(array):
        index = bisect.bisect_left(patient_result_sorted, number)
        if index == len(patient_result_sorted):
            patient_result_sorted.append(number)
            active_indices.append(i)
        else:
            patient_result_sorted[index] = number
            active_indices[index] = i

    # Rebuild
    print(active_indices)
    print(patient_result_sorted)
array = [-5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
assert patience_sorting(array) == [-24, 2, 3, 5, 6, 35]
