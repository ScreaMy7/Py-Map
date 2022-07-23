<h1 align="center">
  <img src="/logo.png" alt="pymap" width="800px">
  <br>
</h1>
<p align="center">
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-_red.svg"></a>
<a href="https://github.com/ScreaMy7/Py-Map/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://twitter.com/ScreamZoro"><img src="https://img.shields.io/twitter/follow/ScreamZoro?label=Follow"></a>
<a href="https://discord.gg/bugbounty"><img src="https://img.shields.io/discord/695645237418131507.svg?logo=discord"></a>
</p>
<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#Nmap+integration">Nmap-cli integration</a> 
</p>

## About The Project

A Light weight port scanner , build to fasten the process of enumeration in CTFs and HTB machines. This tool finds open ports and passes the results to nmap for a verbose scan. This project has been inspired from [naabu](https://github.com/projectdiscovery/naabu).

# Features

<h1 align="center">
  <img src="https://user-images.githubusercontent.com/70141504/180610466-0a51e477-a34f-42f6-81cb-e2ed0375d14f.png" alt="pymap" width="700px">
  <br>
</h1>

 - Fast And Simple **SYN/CONNECT** probe based scanning
 - Optimized for ease of use and **lightweight** on resources
 - **DNS** Port scan
 - **NMAP** integration for service discovery
 - Included Nmap cli for different scans

## Getting Started

Now you may be wondering, how can I run this outstanding piece of code on my own device!?
Here's how.

### Prerequisites
* Python3

### Installation

1. Clone the repo

```sh
https://github.com/ScreaMy7/Py-Map.git
```
2. Pip3 install the requirement.txt
``
sudo pip3 install -r requirement.txt
``
# Usage

To run the tool on a target, on port range 1-10000 without nmap.
```sh
sudo python3 py_map.py -host 10.10.0.1 -ports 1-10000 
```

To run the tool on a target, on port range 1-10000 with nmap scan.
```
sudo python3 py_map.py -host 10.10.0.1 -ports 1-10000 -nmap
```
To run the tool on a target, on port range 1-10000 with nmap cli. Nmap cli gives the freedom to run nmap with any arguments.
```
sudo python3 py_map.py -host hackerone.com -ports 20-80 -cli "-T3 -sS -p21,22,80 --max-rate 60 -O"
```
# Nmap integration

I have integrated nmap support for service discovery or any additional scans supported by nmap on the found results by pyscan, without requirement of `nmap` in the terminal. When `-nmap` is included the open ports get piped to nmap for a verbose scan. Still sometimes if  you need to add arguments to namp the `-cli` help.
To use,`-cli` flag can be used followed by nmap arguments, for example:-
```
sudo python3 py_map.py -host hackerone.com -ports 20-80 -cli "-T3 -sS -p21,22,80 --max-rate 60 -O"
```
# Notes

- Py-Map is designed to scan ports on single hosts , in case solving CTFs or HTB machines.
- I suggest tuning the flags / rate if running Py-Map from local system.
- For best results, run Py-Map as **root** user. By using **sudo**

## License

Distributed under the MIT License. See [LICENSE](https://github.com/ScreaMy7/Py-Map/blob/main/LICENSE) for more information.

## Disclaimer

This repository and the data provided has been created purely for the purposes of academic research and for the development of effective security techniques and is not intended to be used to attack systems except where explicitly authorized. It is your responsibility to obey all applicable local, state and federal laws. 

Project maintainers assume no liability and are not responsible for any misuse or damage caused by the data therein.
