# openvpn-aws
Automation of setting up an openvpn server [author](https://linuxhint.com/vpn_amazon_ec2_setup/) 

Launch Ubuntu t2-micro in your region of choice.  SSH to box as user "ubuntu"
```
sudo apt update
sudo apt upgrade -y
mkdir vpn
cd vpn/
wget https://git.io/vpn -O openvpn-install.sh
chmod +x openvpn-install.sh
sudo ./openvpn-install.sh
```
The default values in the script work well.

Exit SSH
```
scp -i __YOUR__.pem ubuntu@__UBUNTU_IP__:~/client-vpn.ovpn ./
connect with openvpn client
