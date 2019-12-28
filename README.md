# secret-share
Sharing Secrets with SFC Cap


# Install Requirements

It requires virtualenv to be present and python3 should also be there.

## Create the virtualenv
```
virtualenv -p python3 venv
```
## Activate the virtualenv
```
. venv/bin/activate
```
## Install Requirements
```
pip install -r requirements.txt
```

# Configuring AWS credentials :

We will provide you an AWS key and secret and username. Please add them in your AWS config file (that should be in `~/.aws/credentials`). Please check this link for more information : [AWS key Management](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/)

For example : if we provide : 

username : `cliXXXXXX` 
key : `AKIAZRWLTNXXXXXXXXX`
secret : `4tA/B5uKNdKXXXXXXXXXXXXXXXXX`

Then in your `~/.aws/credentials` file, add the following line at the end : 
```

[cliXXXXXX]
aws_access_key_id = AKIAZRWLTNXXXXXXXXX
aws_secret_access_key = 4tA/B5uKNdKXXXXXXXXXXXXXXXXX

```

Make sure the name `cliXXXXXX` is unique in your system. If you already have such a name in your system, please let us know, we will provide a different name.

Then activate the profile by running : 
```
export AWS_PROFILE=cliXXXXXX
```

# Configuring the KMS key

We will also share an KMS key id. If the key id is `fb4115fd-0ab7-XXXXXXXXXXXXXXXXXXXXXXXXX` then run

```
export cmk=fb4115fd-0ab7-XXXXXXXXXXXXXXXXXXXXXXXXX
```

# Encrypt a sample file

Say we have a file `demo_secret.txt` and we want it to encrypt.

```
python encrypt.py --input_file=demo_secret.txt
```

# Things to get from SFC :

AWS credentials (username, key id and secret) and KMS key id.
