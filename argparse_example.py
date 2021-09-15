

def list_s3_bucket(bucket_key, directory):
    print(bucket_key)
    print(directory)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("bucket_key",
                        help="A bucket key, e.g. 'nonpii-sanbox-creditrisk-pro-s3'",
                        type=str)
    parser.add_argument("directory",
                        help="Directory within the bucket (aka prefix), e.g. 'Credit Risk/ifrs9/temp_files_v2'",
                        type=str)
    args = parser.parse_args()

    list_s3_bucket(args.bucket_key, args.directory)