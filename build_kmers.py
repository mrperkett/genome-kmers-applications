"""
Build a Kmers object for a fasta file input, sort them lexicographically, and save
them to file.
"""

import argparse
import logging
import time
from pathlib import Path

from genome_kmers.kmers import Kmers
from genome_kmers.sequence_collection import SequenceCollection


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
        "--fasta-input",
        "-i",
        dest="fasta_input_file_path",
        type=existing_file_path,
        required=True,
        help="input fasta file path",
    )

    parser.add_argument(
        "--output",
        "-o",
        dest="output_file_path",
        type=file_path,
        required=True,
        help="output kmers file path (.hdf5 file)",
    )

    args = parser.parse_args()

    return args


def main():
    """ """
    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    logging.info("Building SequenceCollection from fasta file")
    logging.info(f"\t{args.fasta_input_file_path}")
    start_time = time.time()
    seq_coll = SequenceCollection(fasta_file_path=Path(args.fasta_input_file_path))
    run_time = time.time() - start_time
    logging.info(f"\trun time: {run_time:.1f}")

    logging.info("Building Kmers")
    min_kmer_len = 1
    max_kmer_len = 500
    start_time = time.time()
    kmers = Kmers(
        seq_coll,
        min_kmer_len=min_kmer_len,
        max_kmer_len=max_kmer_len,
        source_strand="forward",
        track_strands_separately=False,
    )
    run_time = time.time() - start_time
    logging.info(f"\trun time: {run_time:.1f}")

    logging.info("Sorting Kmers")
    start_time = time.time()
    kmers.sort()
    run_time = time.time() - start_time
    logging.info(f"\trun time: {run_time:.1f}")

    logging.info("Saving to file")
    logging.info(f"\t{args.output_file_path}")
    start_time = time.time()
    kmers.save(args.output_file_path, include_sequence_collection=True, format="hdf5")
    run_time = time.time() - start_time
    logging.info(f"\trun time: {run_time:.1f}")

    return


if __name__ == "__main__":
    main()
