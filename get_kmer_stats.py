"""
Load the sorted k-mers from file and calculate the k-mer count distribution
for a range of k values saving analysis results to a shelve db file.
"""

import argparse
import logging
import shelve
import time
from pathlib import Path

import numpy as np
from genome_kmers.kmers import Kmers, gen_no_ambiguous_bases_filter
from numba import jit
from scipy import sparse


def existing_file_path(file_path_str):
    file_path = Path(file_path_str)
    if file_path.is_file():
        return file_path
    else:
        raise ValueError(f"file path does not exist: '{file_path_str}'")


def file_path(file_path_str):
    return Path(file_path_str)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input-kmers",
        "-i",
        dest="kmers_input_file_path",
        type=existing_file_path,
        required=True,
        help="input kmers file path (kmers are assumed to be sorted)",
    )

    parser.add_argument(
        "--output",
        "-o",
        dest="output_file_path",
        type=file_path,
        required=True,
        help="analysis output file path (shelve .db file)",
    )

    args = parser.parse_args()

    return args


def main():

    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    # load saved kmers file
    logging.info("Loading saved kmers file")
    logging.info(f"\t{args.kmers_input_file_path}")

    kmers = Kmers()
    kmers.load(args.kmers_input_file_path, format="hdf5")

    logging.info(f"\tmin_kmer_len: {kmers.min_kmer_len}")
    logging.info(f"\tmax_kmer_len: {kmers.max_kmer_len}")

    # define the k-mer lengths for which to run
    kmer_len_list = (
        list(range(1, 30))
        + list(range(30, 50, 2))
        + list(range(50, 100, 10))
        + list(range(100, 501, 50))
    )
    logging.info(kmer_len_list)

    group_hist_list = []
    total_kmers_list = []
    group_hist_unique_list = []
    total_kmers_unique_list = []
    run_times_all_list = []
    run_times_unique_list = []

    # for each kmer_len, generate stats for all k-mers and unique k-mers
    logging.info(f"kmer_len | run_time_all | run_time_unique")
    for kmer_len in kmer_len_list:

        # filter k-mers by length and do not allow any amibuous bases
        no_ambiguous_bases_filter = gen_no_ambiguous_bases_filter(kmer_len)

        @jit
        def filter_func(sba: np.array, sba_strand: str, kmer_sba_start_idx: int) -> bool:
            try:
                passes = no_ambiguous_bases_filter(sba, sba_strand, kmer_sba_start_idx)
            except:  # NOTE: bare except used for use with numba jit
                passes = False

            return passes

        # generate stats for all k-mers
        start_time = time.time()
        group_hist, total_kmers = kmers.get_kmer_group_counts(
            kmer_len=kmer_len, kmer_filter_func=filter_func, min_group_size=1, max_group_size=None
        )
        run_time_all = time.time() - start_time

        # generate stats for "unique" k-mers
        start_time = time.time()
        group_hist_unique, total_kmers_unique = kmers.get_kmer_group_counts(
            kmer_len=kmer_len, kmer_filter_func=filter_func, min_group_size=1, max_group_size=1
        )
        run_time_unique = time.time() - start_time

        # convert arrays to sparse arrays to save space
        group_hist_sparse = sparse.csr_array(group_hist)
        group_hist_unique_sparse = sparse.csr_array(group_hist_unique)

        # add stats to lists
        group_hist_list.append(group_hist_sparse)
        total_kmers_list.append(total_kmers)
        run_times_all_list.append(run_time_all)

        group_hist_unique_list.append(group_hist_unique_sparse)
        total_kmers_unique_list.append(total_kmers_unique)
        run_times_unique_list.append(run_time_unique)

        # save checkpoint to file
        with shelve.open(args.output_file_path) as db:
            db["kmer_len_list"] = kmer_len_list

            db["group_hist_list"] = group_hist_list
            db["total_kmers_list"] = total_kmers_list
            db["run_times_all_list"] = run_times_all_list

            db["group_hist_unique_list"] = group_hist_unique_list
            db["total_kmers_unique_list"] = total_kmers_unique_list
            db["run_times_unique_list"] = run_times_unique_list

        # log run time information
        run_time_all_str = f"{run_time_all:.1f}".rjust(12)
        run_time_unique_str = f"{run_time_unique:.1f}".rjust(16)
        logging.info(f"{str(kmer_len).rjust(8)} | {run_time_all_str} | {run_time_unique_str}")


if __name__ == "__main__":
    main()
