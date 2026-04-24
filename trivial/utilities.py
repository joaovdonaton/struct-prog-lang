#
# Utility functions for matrix-related things
#
import numpy as np

def format_matrix(matrix):
    lines = []
    for row in matrix:
        lines.append("  ".join(str(value) for value in row))
    return "\n".join(lines)

