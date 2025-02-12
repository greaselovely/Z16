---
layout: post
title: "T1 Utilization Questions..."
date: 2007-11-14 00:00:00 -0600
categories: blog
---

The goal was to put to bed the final question that everyone asks and no one ever has a solid answer for, can you get 1.5Mbps up and 1.5Mbps down on a data T1. We have had multiple customers ask us this question recently, so I fired up two routers today to get solid results with empirical evidence to show everyone that has asked.

Here's what I had; a Crisco 1720, a Juniper J2300, one laptop (WinXP) and one desktop (WinXP). Both machines are running WSFTP Server and I used the FTP client via CLI in Windows.

Both T1 interfaces are configured with the IP's shown in the diagram, and encapsulation set to PPP.

![Test Network Image]({{ site.baseurl }}/images/1.jpg "Test Network")



Using PRTG we sampled the T1 interfaces for traffic utilization via SNMP. Sampling rate was set to every 10 seconds with averaging set to 1 minute. The defaults are 60 seconds and 5 minutes respectively.

The graphs below shows traffic utilization while a FTP transfer of a 593+ MB ISO to the laptop from the desktop was underway. This is to simply show traffic being transferred in one direction only. And obviously you can see the end of the transfer complete just under an hour. During this transfer I kept Task Mangler open to watch utilization on the NIC on the laptop. The NIC was negotiated at 100-Full and during this transfer the low average that was reported was 1%.



![Juniper]({{ site.baseurl }}/images/2300-1.jpg "Juniper")

Juniper J2300

![Crisco]({{ site.baseurl }}/images/1720-1.jpg "Crisco")

Crisco 1720

The second set of graphs show our next test. We opened a FTP session to each machine from each machine, set the hash on to watch the transfer and prepared to hit the enter key at the same time to begin both transfers simultaneously. (I also found it interesting how on the Juniper router I received the blip on the proverbial radar every 5 minutes. At first I thought this was a framing issue with relation to clocking as I had left clocking on both routers to internal. So after the 4th blip I flipped the Juniper's T1 clock over to external. There was no drop in traffic but also didn't 'fix' the issue. Interesting at least to see that compared to the Crisco.)



![Juniper]({{ site.baseurl }}/images/2300-2.jpg "Juniper")

Juniper J2300

![Crisco]({{ site.baseurl }}/images/1720-2.jpg "Crisco")

Crisco 1720

And the test went as expected, which is to see 100% utilization bidirectionally. Note (on the close up images) the difference between the first transfer and the second transfer. You can clearly see the input and the output lines not match during the first transfer and then match on the second.

![Juniper]({{ site.baseurl }}/images/Closeup-2300-2.jpg "Juniper")

Juniper J2300

![Crisco]({{ site.baseurl }}/images/Closeup-1720-2.jpg "Crisco")

Crisco 1720


Watching Task Mangler on the laptop and the desktop showed an increase from a loose report of 1% to 3%, and can be safely assumed that since Task Mangler obviously rounds the percentage up / down that the first transfer was at least 1.49% utilization. At 100 Mbps this would effectively equal 1.49 Mbps, which is about the available bandwidth across a T1. (24 channels x 64 kb per channel) + 8 bits signaling = 1544 kbps; aka T1.
PRTG reported an average of 2.976 kbps.

The result is an obvious yes, you do get 1.5 up and 1.5 down. But this DOES NOT mean a T1 is 3 Mbps connection, it means you are utilizing 24 channels up on one pair of wires, and 24 channels down on the second pair of wires. (no comments from the "Well sort of" crowd). Don't get crazy and start thinking you are Stephen Hawking and adding 1.5 + 1.5, don't do it or I'm coming after ya. I'm honestly sick of this question and the assumed 3Mbps of bandwidth. Geez people.


I have also read all over the net and seen some really stupid comments about how this isn't possible and then others who have the right answers with no solid data. There is also something I read on the net about how this was 'theoretically possible'. Well, sleep tight everyone because the theorem has been proven.





---


Other Posts You May Want To Cover in Syrup: