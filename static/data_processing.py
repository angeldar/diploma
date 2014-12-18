def read_data(filename):
    f = open(filename)
    data = []
    for row in f:
        data.append(int(row.strip()))
    return data

# TODO: Move to data processing helpers
def convert_time_between_errors_to_time_of_errors(time_between_errors):
    res = time_between_errors[:]
    for i in range(1, len(res)):
        res[i] += res[i-1]
    return res

def time_of_last_error(time_between_errors):
    return sum(time_between_errors)