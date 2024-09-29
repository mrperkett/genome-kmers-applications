## `build_kmers.py`

```
INFO:root:Building SequenceCollection from fasta file
INFO:root:      GCA_036323735.1_GRCr8_genomic.fna
INFO:root:      run time: 95.4
INFO:root:Building Kmers
INFO:root:      run time: 5.5
INFO:root:Sorting Kmers
INFO:root:      run time: 5978.7
INFO:root:Saving to file
INFO:root:      GRCr8-kmers.hdf5
INFO:root:      run time: 87.0
```

## `get_kmer_stats.py`

```
INFO:root:Loading saved kmers file
INFO:root:      GRCr8-kmers.hdf5
INFO:root:      min_kmer_len: 1
INFO:root:      max_kmer_len: 500
INFO:root:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500]
INFO:root:kmer_len | run_time_all | run_time_unique
INFO:root:       1 |        295.9 |            223.8
INFO:root:       2 |        220.7 |            220.8
INFO:root:       3 |        225.1 |            223.0
INFO:root:       4 |        228.5 |            226.6
INFO:root:       5 |        246.9 |            250.2
INFO:root:       6 |        247.3 |            250.4
INFO:root:       7 |        275.0 |            272.1
INFO:root:       8 |        426.5 |            453.3
INFO:root:       9 |        437.5 |            433.2
INFO:root:      10 |        438.2 |            436.0
INFO:root:      11 |        443.4 |            442.2
INFO:root:      12 |        459.5 |            490.1
INFO:root:      13 |        470.3 |            466.4
INFO:root:      14 |        488.7 |            480.7
INFO:root:      15 |        525.5 |            506.3
INFO:root:      16 |        576.5 |            557.0
INFO:root:      17 |        626.2 |            616.8
INFO:root:      18 |        651.7 |            649.4
INFO:root:      19 |        659.0 |            654.2
INFO:root:      20 |        652.7 |            663.5
INFO:root:      21 |        664.8 |            676.1
INFO:root:      22 |        681.2 |            680.8
INFO:root:      23 |        699.1 |            704.6
INFO:root:      24 |        707.5 |            698.2
INFO:root:      25 |        686.4 |            685.6
INFO:root:      26 |        688.3 |            695.3
INFO:root:      27 |        688.8 |            702.4
INFO:root:      28 |        697.1 |            701.2
INFO:root:      29 |        693.9 |            703.2
INFO:root:      30 |        701.6 |            710.6
INFO:root:      32 |        714.1 |            715.1
INFO:root:      34 |        715.3 |            723.0
INFO:root:      36 |        729.4 |            728.0
INFO:root:      38 |        724.4 |            734.3
INFO:root:      40 |        738.6 |            750.3
INFO:root:      42 |        806.1 |            822.4
INFO:root:      44 |        746.9 |            753.1
INFO:root:      46 |        747.9 |            758.9
INFO:root:      48 |        752.0 |            763.3
INFO:root:      50 |        759.2 |            766.4
INFO:root:      60 |        776.6 |            791.7
INFO:root:      70 |        817.5 |            845.5
INFO:root:      80 |        834.0 |            822.5
INFO:root:      90 |        796.1 |            799.1
INFO:root:     100 |        804.5 |            811.2
INFO:root:     150 |        866.8 |            879.7
INFO:root:     200 |       1077.3 |           1031.5
INFO:root:     250 |       1155.2 |           1177.7
INFO:root:     300 |       1197.9 |           1200.5
INFO:root:     350 |       1238.4 |           1245.0
INFO:root:     400 |       1289.2 |           1305.3
INFO:root:     450 |       1339.1 |           1353.3
INFO:root:     500 |       1418.6 |           1412.2
```