from utils import get_parsed_args, get_df_with_descs
from logger import setup_logger


def main():
    logger = setup_logger(__name__)
    args = get_parsed_args()
    sdf_file = args.sdf_file
    label_file = args.label_file
    output_path = args.out
    df = get_df_with_descs(sdf_file, label_file)
    logger.info(f'df shape: {df.shape}')
    df.to_csv(output_path, encoding='utf-8', index=False)


if __name__ == '__main__':
    main()
