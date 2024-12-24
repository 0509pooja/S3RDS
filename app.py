import boto3
import pymysql

# S3 client
s3 = boto3.client('s3')

# RDS connection details
rds_host = "<endpoint>"
rds_user = "<user>."
rds_password = "<pass>"
rds_database = "database-1"

# Event object for testing
bucket_name = "pooja23-12"
object_key = "test-data.txt"

def handler(event, context):
    print(f"Fetching data from S3: Bucket: {bucket_name}, Key: {object_key}")

    try:
        # Fetch data from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = response['Body'].read().decode('utf-8')
        print("Data fetched from S3.")

        # Connect to RDS
        conn = pymysql.connect(
            host=rds_host,
            user=rds_user,
            password=rds_password,
            database=rds_database
        )
        print("Connected to RDS.")

        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO mytable (data) VALUES (%s)"
                cursor.execute(sql, (data,))
            conn.commit()
            print("Data inserted into RDS.")
        
        finally:
            # Ensure connection is closed after the operations
            conn.close()
            print("RDS connection closed.")
        
        # Add success message after the operations are complete
        print("Lambda function completed successfully.")
        return {"status": "Data pushed to RDS"}

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"status": "Error", "message": str(e)}

if _name_ == "_main_":
    handler(None, None)
