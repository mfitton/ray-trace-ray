import matplotlib.pyplot as plt
from collections import defaultdict
import re

def to_filename(dim, trial_num, using_ray):
    if using_ray:
        return f'{dim[0]}x{dim[1]}-ray-benchmark-{trial_num}.txt'
    else:
        return f'{dim[0]}x{dim[1]}-benchmark-{trial_num}.txt'

def to_label(dim):
    return f"{dim[0]}x{dim[1]}"

time_re = re.compile('(\d+)m(\d+\.\d+)s')
def extract_time_from_line_s(line):
    result = time_re.search(line)
    mins, seconds = result.group(1, 2)
    return 60 * float(mins) + float(seconds)

def main():
    dims = [(600, 450), (1200,900), (1600,1200)]
    num_trials = 5
    file_names = []
    results = []
    for result_type in (True, False):
        for dim in dims:
            for trial in range(num_trials):
                file_name = to_filename(dim, trial, result_type)
                with open(file_name) as benchmark:
                    benchmark_lines = benchmark.readlines()
                    for line in benchmark_lines:
                        if line.startswith('user'):
                            secs = extract_time_from_line_s(line)
                            results.append((result_type, dim, 'user', secs))

    grouped_results = defaultdict(list)
    for result in results:
        grouped_results[(result[1], result[0])].append(result[3])
    
    last = {}
    means = {}
    for (dim, uses_ray), ts in grouped_results.items():
        label = to_label(dim)
        xs = [label] * len(ts)
        ys = ts
        means[(dim, uses_ray)] = sum(ts)/len(ts)
        style = {'c': 'b', 'marker': 'o'} if uses_ray else {'c': 'r', 'marker': 'o'}
        figlabel = 'ray' if uses_ray else 'no ray'
        last[uses_ray] = plt.scatter(xs, ys, **style)
    plt.figlegend([last[False], last[True]], ["no ray", "ray"])
    plt.xlabel('Dimensions')
    plt.ylabel('User Execution Time (s)')
    plt.show()
    

if __name__ == '__main__':
    main()