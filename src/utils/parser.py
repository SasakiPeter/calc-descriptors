import argparse

__all__ = ('get_parsed_args',)


def get_parsed_args():
    parser = argparse.ArgumentParser(
        description='Calculate descriptors'
    )

    parser.add_argument(
        'sdf_file',
        help='sdf file path'
    )

    parser.add_argument(
        'label_file',
        help='label file path'
    )

    parser.add_argument(
        '-o', '--out',
        type=str,
        default='./output.csv',
        help='output directory name (./output.csv)'
    )
    return parser.parse_args()
