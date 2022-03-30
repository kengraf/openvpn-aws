# Template to start OpenVPN Access server
import boto3

# Amazon Linux 2 AMI in London
londonaws='''
{ "region": "eu-west-2",
                 "sg": ["sg-0c51113a91a64fa42",], # change this
                 "sshkey": "london2", # change this
                 "ami": "ami-0015a39e4b7c0966f" # This is an Ubuntu AMI
                 }
'''
REGION='eu-west-2'  # For a London based deploy
SG='sg-05a87a5fbfd0fd5ae'
SSHKEY='london2'
AMI='ami-064ff912f78e3e561'

# IT666 lab wants a London based deployment
openvpn = { "local": londonaws,
            "tags": [
                {
                     'Key': 'Name',
                     'Value': 'openvpn'
                     },
            ]
            }

# EC2 user-data to install OpenVPN Access Server on a Amazon Linux AMI
USERDATA='''#! /bin/bash
sudo -i
yum -y update
yum -y install ncurses-compat-libs
yum -y install https://as-repository.openvpn.net/as-repo-centos7.rpm
yum -y install openvpn-as

# access server config
passwd openvpn << EOF
strongpassword
strongpassword
EOF

'''
# pick the location specification to use
spec = openvpn
ec2 = boto3.resource('ec2', region_name=spec['local']['region'])

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId=spec['local']['ami'], 
     MinCount=1,
     MaxCount=1, # if more than 1 AWS will create that many
     InstanceType='t2.micro',
     KeyName=spec['local']['sshkey'],
     UserData=openvpnas_userdata, # userdata is executed once the instance is started
     SecurityGroupIds=spec['local']['sg'], # your defined security group
     TagSpecifications=[{ 'ResourceType': 'instance', 'Tags': spec['tags'] },]
)
