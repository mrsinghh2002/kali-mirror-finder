# Kali Mirror Finder Using Single Python File 

A python package for your Kali Linux distro that find the fastest mirror and configure your apt to use that mirror



## Supported Distros

- Kali Linux ( kali-rolling )

## Usafe

```shell
$ sudo python3 mirror-finder.py
```


## Help

Inspired from [htmm/better-mirror](https://github.com/htmm/better-mirror)

```shell
$ sudo python3 mirror-finder.py


mirror-finder 1.0.0 
https://github.com/mrsinghh2002/kali-mirror-finder

 

## Sample Output

```shell
$ sudo python3 mirror-finder.py

[*] Calculating the mirror latency...
[*] Pinging kali.download ... latency 15.65ms
[*] Pinging mirror.pyratelan.org ... latency 188.5ms
[*] Pinging mirror.karneval.cz ... latency 186.75ms
[*] Pinging ftp.free.fr ... latency 152.5ms
[*] Pinging ftp.jaist.ac.jp ... latency 193.75ms
[*] Pinging ftp.halifax.rwth-aachen.de ... latency 147.0ms
[*] Pinging ftp1.nluug.nl ... latency 145.25ms
[*] Pinging ftp2.nluug.nl ... latency 145.25ms
[*] Pinging mirrors.dotsrc.org ... latency 165.0ms
[*] Pinging mirrors.jevincanders.net ... latency 225.5ms
[*] Pinging mirror.erickochen.nl ... latency 147.25ms
[*] Pinging mirror.serverion.com ... latency 151.0ms
[*] Pinging ftp.acc.umu.se ... latency 177.75ms
[*] Pinging mirror.lagoon.nc ... latency 311.0ms
[*] Pinging mirror.serverius.net ... latency 154.75ms
[*] Pinging archive-4.kali.org ... latency 144.25ms
[*] Pinging mirror-1.truenetwork.ru ... latency 338.75ms
[*] Pinging mirror.neostrada.nl ... latency 218.25ms
[*] Pinging mirror.anquan.cl ... latency 338.5ms
[*] Pinging wlglam.fsmg.org.nz ... latency 316.0ms
[*] Pinging hlzmel.fsmg.org.nz ... latency 311.75ms
[*] Pinging ftp.harukasan.org ... latency 568.33ms
[*] finding the best mirror for you :) ....
[*] found! the selected mirror: kali.download ... latency 15.65 ms
[*] backuping original /etc/apt/sources.list to /etc/apt/sources.list.bak
[*] updating /etc/apt/source.list
[*] running apt-get update for you....
Hit:1 http://kali.download/kali kali-rolling InRelease
Reading package lists... Done
[*] Thanks For Using The Tool!

 
```


## Author
kali-mirror-finder @[MrSinghh2002](https://github.com/mrsinghh2002) , Released under the MIT License.

---


## Donation
If this project help you reduce time to develop, you can give me a cup of coffee :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/meshivanshsingh)

 
