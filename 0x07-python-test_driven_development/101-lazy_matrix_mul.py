#!/usr/bin/python3
"""Describes matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices."""
    return (np.matmul(m_a, m_b))
