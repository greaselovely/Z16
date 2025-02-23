---
layout: post
title: "FVESCO and My Career Transition"
date: 2025-02-22 00:00:00 -0600
categories: blog
---

## My Career Transition
I worked for a company called `Film/Video Equipment Service Company (F/VESCO)` after I got out of school.  Fun fact, I went to Colorado Institute of Art (CIA) for Music and Video Business.  Previous to this I had worked at `Lighting Services Inc (LSI)` which used to be ridiculously large sound stage and lighting company located at the corner of Alameda and Cherokee in Denver.  I was loading trucks and doing production work.  

During my early days at F/VESCO, they were using Apple Mac II SE's and were networked together using RJ11 cable (telephone cable) and the protocol was AppleTalk.  They had dot matrix printers that were connected directly to a couple of the computers.  On these machines they were using FileMaker Pro as their rental and sales database.  Which honestly, at the time, was an amazing piece of software.  Very extensible, very easy to understand and modify.  More on that later.

When customers came in to rent, buy or have something repaired, they would use this crazy small network of Macs to print out to the dot matrix printers the customer's receipt or rental contract on multi-part carbonless paper.

At some point, Dean's `IT guy` (they weren't even called IT guys then), his name was Kevin. There was another Kevin G. who worked in the Camera Support department that I eventually took over for when he went to work for Sachtler out in New York; not the same Kevin is my point.  So, Kevin had talked Dean into converting from the Apple Mac II SEs (they were getting old for sure) and moving to a Windows based system.  Dean agreed and Kevin went to a local computer store over on S Broadway called Sileo Computers (pronounced sil-ee-oh). He had Sileo build the machines, install Windows 95 on the desktops, and a server installed with NT 4.0.  Kevin then eventually picked up all of these machines and brought them to the office, placing them all in the conference room right behind the reception desk.  There they sat for what now feels like forever. 

Now, we had heard there was going to be a migration to a Windows network, but it just never happened.  There was a really smart video engineer who worked on all of the broadcast and ENG video cameras named Tom S.  Tom and I eventually got tired of waiting for this to happen, so we went to Dean and told him that we would get this done.  He said fine.  Actually, he probably said something to the effect of `you're fucking me, you're all fucking me`, which is a classic Dean-ism, and then agreed to `let` us do it.  

This was the actual moment that I began my career transition.

While all of the computers sat in the conference room, we got some of them turned on and started trying to understand what we just got ourselves into.  Ultimately the main project was to get FileMaker Pro to function no different than it had before.  We were able to figure out how to get the database copied over onto the Windows machines and started working in FileMaker to get formatting correct.  Primarily as it relates to the printers.  Dean very much wanted to maintain the use of the multi-part carbonless paper on the dot matrix printers.  The paper that he had was also pre-printed with the company graphics and had lines printed on them for each line item of the contracts that were printed.  Each line contained the description of what was being rented or what item was in for repair and what to do with it during repair.  So we needed to get the lines correct within the software.  And you'd think that it would be a straight copy and it would just work.  Not the case, but it saved us a lot of time to get it done, but it was a lot of fine tuning.  It allowed me to understand the software a lot and made me realize what else we could do with it.  So it was mostly formatting the pages that I worked on initially prior to migrating.  But I got it.

I'll spare many details of my recollection of the work performed even though it was very interesting to me that I got to do some new things.  The work is still very vivid in my head.  However, I recognize that it's actually uninteresting to you the reader to have me blather on about how I had to figure out what CAT5 was, how we ran the CAT5, how I had to go learn to terminate CAT5, how I had to learn to test CAT5 after learning about 568A and 568B wiring standards, and realizing I had not terminated them correctly and had to re-terminate over half.  How I had to learn what a network hub was (long before we had switches).  And then how I had to quickly try to figure out subnetting and why some of the new network laser printers didn't work over the network since, as I quickly learned, they were not on the same network subnet.  I'll also spare some details of the DSL we had (very new internet technology for our office) and how we had to figure out how to allow internet access from all of the computers out this DSL line (I can even still see the UFO like shape of the DSL modem).  I'll continue to spare some details on learning how to get NT 4.0 operational, how to get this new server and its operational role as a `Primary Domain Controller (PDC)` understood, and then install MS Proxy 2.0, which was still in the box, onto the PDC and then get it connected as the gateway for the rest of the network.  I did all of that without any formal training. 


## Um, what?!
"Sorry, did you say that you placed your PDC directly on the internet with only MS Proxy 2.0 to allow traffic out?"  

You read what you read.  That happened.  I exercise my right to the brief ignorance I had of network security.  Almost up until I was on a friends house where they had Comcast Cable (the name may have been something different, I can't recall).  But these were the days where it was a giant broadcast domain and you could see a variety of things on the cable network, including network printers.  This is where my eyes opened, and when you start sending print jobs to printers in someone else's home, that's a thing.

And let me tell you what, it's the EXACT same thing that New Horizons in Denver did with their network.  I know because I also worked there during Y2K.  

Solid tip for you; MS Proxy 2.0 doesn't care if you want to get into the admin share of the PDC from the internet.  Ask me how I know.  

Hint: Setting the boot timer in the boot.ini file to -1 halts the boot of NT 4.0 and it just sits on the boot screen until a selection is made.  Where if you are crafty enough, you can place a message there for the next person at the console to give them the ultimate pucker.



---

Other Posts You May Want To Cover in Syrup:
