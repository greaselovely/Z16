---
layout: post
title:  "NetScreen SSG 20 Dual WAN"
date:   2007-09-24 15:07:37 -0700
categories: Juniper NetScreen
---


Something I did recently using a SSG 20 with commercial T1 and Comcast and both default virtual routers. (You don't have to use two virtual routers, but here's why I did this at first). Initially, my client reported that Comcast was assigning DHCP to the firewall's interface. When DHCP is used, the default route created from DHCP cannot be modifed and will show up as a directly connected route, so it will have a higher metric (unless you modify your preference / metric settings, but I have not tried that) So, if Comcast is supposed to be the backup route, placing it in the untrust-vr and controlling traffic in the trust-vr worked great. This works fine with a static IP as well.

Here we go:

Here are the default zones in the default trust-vr.

```
set zone "Trust" vrouter "trust-vr"
set zone "Untrust" vrouter "trust-vr"
```

I created a new custom zone and placed it in the untrust-vr

```
set zone id 101 "Comcast"
set zone "Comcast" vrouter "untrust-vr"
```

I set int Ethernet0/1 in the Comcast zone. You will have to do this or track-ip will not fail the interface back. You have to setup a manage IP on the Ethernet0/0 (untrust) interface. See the the track-ip section below.

```
set interface "ethernet0/0" zone "Untrust"
set interface "ethernet0/1" zone "Comcast"
set interface "ethernet0/2" zone "Trust"
set interface ethernet0/0 ip 1.1.1.1/24
set interface ethernet0/1 ip 2.2.2.1/24
set interface ethernet0/2 ip 192.168.1.1/24
```

I then setup the track-ip option. Track-ip will use the manage ip to ping. Why? Because if track-ip can't ping the remote IP (usually a device a couple of hops from you) it brings down the interface (in software only) and thus can't monitor the remote IP if the interface is down. Track-ip uses the manage ip for those tests. If the interface link goes down, whether you unplug the cable or the upstream device goes offline, then track-ip does not play a role, but since the link is down so is the first default route and thus the second default route comes up.

`set interface ethernet0/0 monitor track-ip ip`

The default weight is 255, which means that -this- test has to fail 255 times before the track-ip test causes the interface to go down. If you have multiple tests, the sum of all tests must equal the weight before it drops the interface and thus the route. This only happens in software, you probably will not see the link drop or the status of the interface go down.

`set interface ethernet0/0 monitor track-ip weight 1`

The following interval is in seconds.

`set interface ethernet0/0 monitor track-ip ip 4.2.2.2 interval 5`

The threshold is the number of tests that must fail before track-ip drops the interface. So, in this scenario, track-ip will monitor the remote ip every 5 seconds (interval), if it fails twice (threshold) then the weight equals 1, and brings the interface down.

`set interface ethernet0/0 monitor track-ip ip 4.2.2.2 threshold 2`




Set a new default route in the untrust-vr and then set route's back to the network in the trust-vr. The default route in the untrust-vr will be active but traffic won't hit this VR until the track-ip option disables the interface located in the trust-vr. When that happens, the default route in the trust-vr becomes inactive and the second route comes up, sending traffic to the untrust-vr. Note the preference on the two default routes in the trust-vr.

```
set vrouter "untrust-vr"
set route 0.0.0.0/0 interface ethernet0/1 gateway 2.2.2.2
set route 192.168.1.0/24 vrouter "trust-vr" preference 20
exit
set vrouter "trust-vr"
unset add-default-route
set route 0.0.0.0/0 interface ethernet0/0 gateway 1.1.1.2 preference 10
set route 0.0.0.0/0 vrouter "untrust-vr" preference 20 metric 1
exit
```




---


Other Posts You May Want To Cover in Syrup: