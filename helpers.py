import sys
import os
import glob
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'name' not in kw:
            kw['name'] = method.__name__
        if 'log_time' in kw:
            name = kw.get('log_name', kw['name'])
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' %
                  (kw['name'], (te - ts) * 1000))
        return result
    return timed


@timeit
def run(algorithm, dataset, file=sys.stdout, **kwargs):
    if file is None:
        file = open(os.devnull, 'w')
    with open(dataset) as f:
        print(*algorithm(f.read()), file=file)


def run_and_measure(algorithm, data_file_pattern, file=None):
    for data_file in sorted(glob.glob(data_file_pattern)):
        print('Processing {}'.format(data_file))
        run(algorithm, data_file, name=algorithm.__name__, file=file)
