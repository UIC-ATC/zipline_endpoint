filename = '/opt/conda/envs/backtest/lib/python3.5/site-packages/zipline/data/benchmarks.py'

with open('benchmarks.py', 'r') as src:
    with open(filename, 'w') as f:
        f.write(src.read())
