from decouple import config
import boto3

class SESServices:
    def __init__(self):
        self.key = config("AWS_ACCESS_KEY")
        self.secret = config("AWS_SECRET_KEY")
        self.region = config("AWS_REGION")
        self.ses = boto3.client(
            "ses",
            region_name=self.region,
            aws_access_key_id = self.key,
            aws_secret_access_key=self.secret

        )
    def send_mail(self, subject, to_address, text_data):
        body = {"Text": {"Data": text_data, "Charset": "utf-8"}}

        self.ses.send_email(Source="lbusso55@gmail.com",
                            Destination={"ToAddresses": to_address},
                            Message = {
                                "Subject": {"Data": subject, "Charset": "utf-8"},
                                "Body": body
                            })