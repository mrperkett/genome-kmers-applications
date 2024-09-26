## `build_kmers.py`

```
INFO:root:Building SequenceCollection from fasta file
INFO:root:      GCA_000001635.9_GRCm39_genomic.fna
INFO:root:      run time: 95.1
INFO:root:Building Kmers
INFO:root:      run time: 4.8
INFO:root:Sorting Kmers
INFO:root:      run time: 6277.9
INFO:root:Saving to file
INFO:root:      GRCm39-kmers.hdf5
INFO:root:      run time: 41.8
```

## `get_kmer_stats.py`

```
INFO:root:Loading saved kmers file
INFO:root:      GRCm39-kmers.hdf5
INFO:root:      min_kmer_len: 1
INFO:root:      max_kmer_len: 500
INFO:root:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500]
INFO:root:kmer_len | run_time_all | run_time_unique
INFO:root:       1 |        297.0 |            224.8
INFO:root:       2 |        229.3 |            218.7
INFO:root:       3 |        206.9 |            206.3
INFO:root:       4 |        210.0 |            210.4
INFO:root:       5 |        227.5 |            228.9
INFO:root:       6 |        226.7 |            231.8
INFO:root:       7 |        351.6 |            255.7
INFO:root:       8 |        390.9 |            390.8
INFO:root:       9 |        395.4 |            394.7
INFO:root:      10 |        404.7 |            399.3
INFO:root:      11 |        403.9 |            402.8
INFO:root:      12 |        416.9 |            415.9
INFO:root:      13 |        427.2 |            424.3
INFO:root:      14 |        444.7 |            437.1
INFO:root:      15 |        473.7 |            460.4
INFO:root:      16 |        518.5 |            505.2
INFO:root:      17 |        564.8 |            560.8
INFO:root:      18 |        587.0 |            602.5
INFO:root:      19 |        593.5 |            593.9
INFO:root:      20 |        594.3 |            602.4
INFO:root:      21 |        606.1 |            612.0
INFO:root:      22 |        612.3 |            619.6
INFO:root:      23 |        616.0 |            640.8
INFO:root:      24 |        620.7 |            627.1
INFO:root:      25 |        619.4 |            627.0
INFO:root:      26 |        628.3 |            635.2
INFO:root:      27 |        670.5 |            634.0
INFO:root:      28 |        631.5 |            640.2
INFO:root:      29 |        633.0 |            641.4
INFO:root:      30 |        638.6 |            665.7
INFO:root:      32 |        651.4 |            657.1
INFO:root:      34 |        651.1 |            659.9
INFO:root:      36 |        654.3 |            662.0
INFO:root:      38 |        658.6 |            666.4
INFO:root:      40 |        667.8 |            673.7
INFO:root:      42 |        668.1 |            677.4
INFO:root:      44 |        672.0 |            685.6
INFO:root:      46 |        677.3 |            688.4
INFO:root:      48 |        680.2 |            694.9
INFO:root:      50 |        685.6 |            697.6
INFO:root:      60 |        705.8 |            716.0
INFO:root:      70 |        722.1 |            748.4
INFO:root:      80 |        706.9 |            711.5
INFO:root:      90 |        713.6 |            722.5
INFO:root:     100 |        726.7 |            733.2
INFO:root:     150 |        782.7 |            788.9
INFO:root:     200 |        945.6 |           1007.3
INFO:root:     250 |       1092.3 |           1102.4
INFO:root:     300 |       1157.2 |           1161.0
INFO:root:     350 |       1198.0 |           1221.4
INFO:root:     400 |       1259.3 |           1232.7
INFO:root:     450 |       1241.2 |           1253.7
INFO:root:     500 |       1286.0 |           1351.0
```