# openvpn-aws
Automation of setting up an openvpn server [author](https://linuxhint.com/vpn_amazon_ec2_setup/) 

This repo is used to teach college students new to AWS various deployment approaches.

### Method #1
Using the AWS console to launch Ubuntu t2-micro in your region of choice.  
- Set your region
- In the EC2 console, click "launch instance"
- Pick Ubuntu, SG should be limited to your private IP, create an SSH keypair if you don't have one ready.
- Complete the form as needed.
- SSH to box as user "ubuntu"

Update the OS
```
sudo apt update -y
sudo apt upgrade -y
```

Install and configure OpenVPN
```
#!/bin/sh
mkdir vpn
cd vpn/
wget https://git.io/vpn -O openvpn-install.sh
chmod +x openvpn-install.sh
# The default values in the script work well.
sudo ./openvpn-install.sh  <<EOF





EOF
cp /root/client.ovpn /home/ubuntu/
```


Exit SSH
```
scp -i __YOUR__.pem ubuntu@__UBUNTU_IP__:~/client.ovpn ./
```

connect with openvpn client
```
AMI=ami-08b6f2a5c291246a0 # AWS instance March 8, 2022  
TYPE=t2.medium # A t2.micro is slow but will work   
KEYNAME=ohio # EDIT this for your value  
SG=sg-05a87a5fbfd0fd5ae # EDIT this for your value  
INSTANCE_ID=`aws ec2 run-instances --image-id $AMI --count 1 \
  --instance-type $TYPE --key-name $KEYNAME --security-group-ids $SG \
  --output text --query 'Instances[0].InstanceId'`
aws iam attach-role-policy --role-name FullAdminRole \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam create-instance-profile --instance-profile-name FullAdminRole
aws iam add-role-to-instance-profile --role-name FullAdminRole \
  --instance-profile-name FullAdminRole
aws ec2 associate-iam-instance-profile --instance-id $INSTANCE_ID \
  --iam-instance-profile Name=FullAdminRole
```
