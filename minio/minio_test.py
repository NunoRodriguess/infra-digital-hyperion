from minio import Minio
from minio.error import S3Error
import os

# ---- Configuration ----
MINIO_ENDPOINT = "localhost:9000"   # e.g. "minio.mycompany.com:9000"
ACCESS_KEY = "rootuser"
SECRET_KEY = "rootpass123"
BUCKET_NAME = "my-bucket"
OBJECT_NAME = "example/hello.txt"
FILE_PATH = "hello.txt"
SECURE = False  # True if using HTTPS

def main():
    # Create MinIO client
    client = Minio(
        MINIO_ENDPOINT,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=SECURE,
    )

    # Ensure bucket exists
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)
        print(f"Created bucket: {BUCKET_NAME}")

    # Upload file
    client.fput_object(
        bucket_name=BUCKET_NAME,
        object_name=OBJECT_NAME,
        file_path=FILE_PATH,
        content_type="text/plain",
    )

    print(f"Uploaded '{FILE_PATH}' to '{BUCKET_NAME}/{OBJECT_NAME}'")

if __name__ == "__main__":
    try:
        main()
    except S3Error as e:
        print("MinIO error:", e)
