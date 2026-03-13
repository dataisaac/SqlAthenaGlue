import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq
import boto3

def process_csv(csv_file: str, output_dir: str, bucket_name: str, s3_key: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    s3 = boto3.client(
        's3',
        aws_access_key_id = 'AKIAQMPUDRMOEUHZRAGJ',
        aws_secret_access_key = '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',    
        region_name = 'sa-east-1'
    )

    df = pd.read_csv(csv_file)

    json_file = os.path.join(output_dir, "moviesAndTv.json")

    df.to_json(json_file, orient='records', lines=False)

    parquet_file = os.path.join(output_dir, "moviesAndTv.parquet")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_file)

    s3.upload_file(parquet_file, bucket_name, s3_key)

