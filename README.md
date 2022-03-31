# openvpn-aws
automation of setting an openvpn server

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

```
ls -la ~/client-vpn.ovpn
scp -i ~/Downloads/private.pem ubuntu@__UBUNTU_IP__8:~/client-vpn.ovpn ./
