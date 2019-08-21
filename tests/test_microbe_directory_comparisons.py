"""Test suite for experimental functions."""

import pandas as pd

from unittest import TestCase
from os.path import join, dirname

from microbe_directory.comparisons import (
    compare_microbe_directory_dataframes,
    compare_taxa_lists,
)
from microbe_directory.comparisons.statistics import (
    compare_categorical,
    compare_numeric,
)
from microbe_directory.comparisons.constants import (
    MICROBE_DIRECTORY,
)

PACKET_DIR = join(dirname(__file__), 'built_packet')


class TestMicrobeDirectoryComparisons(TestCase):
    """Test suite for comparing taxa lists using the microbe directory."""

    def test_compare_categorical_binary(self):
        """Test that we can run UMAP."""
        categorical_test = compare_categorical(
            'yes',
             pd.Series(['yes', 'yes', 'no', 'yes', 'yes']),
             pd.Series(['no', 'no', 'no', 'yes', 'yes', 'no', 'no']),
        )

    def test_compare_categorical_multi(self):
        """Test that we can run UMAP."""
        categorical_test = compare_categorical(
            'A',
            pd.Series(['A', 'B', 'D']),
            pd.Series(['B', 'C', 'D', 'E'])
        )

    def test_compare_numeric(self):
        """Test that we can run fractal."""
        numeric_test = compare_numeric(
            pd.Series([0, 1, 3, 0, 1, 1, 2, 2]),
            pd.Series([2, 2, 1, 3, 1, 3, 4]),
        )

    def test_compare_dataframes(self):
        dataframe_test = compare_microbe_directory_dataframes(
            pd.DataFrame(MICROBE_DIRECTORY.iloc[0:5, 7:30]),
            pd.DataFrame(MICROBE_DIRECTORY.iloc[9:14, 7:30]),
        )

    def test_compare_taxa_lists(self):
        taxa_list_test = compare_taxa_lists(
            MICROBE_DIRECTORY.iloc[0:5].index.tolist(),
            MICROBE_DIRECTORY.iloc[9:14].index.tolist(),
        )
    def test_compare_categorical_abundances(self):
        cat_abundances_test = compare_categorical_abundances(
            'A'
            {'A':0.2, 'B':0.3, 'C':0.5}
            {'B':0.25, 'C':0.4, 'D':0.25, 'E':0.1}
        )
    def test_compare_numerical_abundances(self):
        numeric_abundances_test = compare_numerical_abundances(
            {5:0.2, 6:0.25, 7:0.25, 8:0.1, 9:0.2},
            {4:0.2, 6:0.125, 7:0.3, 8:0.375},
        )
   
