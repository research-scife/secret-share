import os
import base64
import boto3
from cryptography.fernet import Fernet
import sys
import click


@click.command()
@click.option('--input_file', default='test', help='path to file containing secret msg')
def encrypt(input_file):
	cmk_id = os.environ["cmk"]
	encrypted_secret_file_path = input_file.split(".")[0] + "_cipher"
	encrypted_data_key_file_path = input_file.split(".")[0] + "_data_key_cipher"

	kms_client = boto3.client('kms', region_name='eu-west-1')


	data_key = kms_client.generate_data_key(KeyId=cmk_id, KeySpec="AES_256")

	with open(encrypted_data_key_file_path, 'wb') as fp:
		fp.write(base64.b64encode(data_key["CiphertextBlob"]))

	with open(input_file, 'rb') as fp:
		file_contents = fp.read()            

	f = Fernet(base64.b64encode(data_key['Plaintext']))
	with open(encrypted_secret_file_path, 'wb') as fp:
		fp.write(f.encrypt(file_contents))
	return


if __name__ == '__main__':
	encrypt()