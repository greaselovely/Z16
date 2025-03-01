---
layout: post
title: "My Garage Doors and RATGDO"
date: 2025-03-01 00:00:00 -0600
categories: blog
---

If you're like me and like nerd things and IOT devices then you may have bought the Chamberlain MyQ garage door opener for the ability to get notified, control the door remotely, and maybe even spent the duckets on the one with the camera.

I, like many other people, got the rug pulled out from under us when Chamberlain decided to tell their more technical user base to suck it.  A large majority of their user base, I guarantee, doesn't care about using home automation or other interesting things.  There's a very small part of their user base that likes to play, and I'm one of them. 

What Chamberlain did was remove API access to their backend.  That shutdown access via their cloud server farm for this arguably small user base.  

In comes Paul Weiland, who did the world an amazing favor of building out RATDGO (official initialism seems to be ratgdo but I'm a stickler for uniform initialisms, or what is a combination of an acryonym and initialism).  I'm not going to get into the history if this amazing work he did, that's what DDG is for.  

I'm going to say that I spent my Saturday morning getting both of my openers connected to Home Assistant via RATGDO.  I had ordered these many months ago, then also ordered the little tiny holder that they decided to also sell.  And then they sat in a drawer for a long time.  Sometimes I do this thing where it feels daunting to start a project.  This is a project / product that comes very bare bones and has none of the standard over-produced packaging and quick start docs.  It comes in bubble wrap and necessary wires.   So there's nothing to do the soft hand holding to getting it done.  

And of course the simplest of a DDG will get the necessary information in my hands.  And sometimes I forget that while I'm in the middle of analysis paralysis.  

So, I did a quick video look up and saw how quick it was.  Now, my only complaint, which is barely that, is that Firefox can't be used for the install.  And there may be other ways to do this, I just haven't look it up.  Chrome is the supported browser for today.

-Get them powered up via the micro-usb connector to your machine.  
-Go to the [website](https://ratgdo.github.io/esphome-ratgdo/){:target=blank}
-Figure out which opener you have, and choose it on the page
-Figure out which RATGDO board you have, and choose it on the page
-Click the Connect button, follow the instructions on the pop up and install the software to the board
-Once that is done, it will then help you get it connected to your wireless network
-Once that is done, it will ask you what SSID to connect it to
-Once that is done, it will walk you through adding it to Home Assistant

If you have the MyQ with the yellow learn button like I do, then it's stupid simple.  There is included a small guage three conductor with connector that comes with it.  This is all you need.  The colors, red, white and black align with the colors on the opener's terminals that the sensors and button(s) connect to.  Mount your RATGDO, plug it in to a USB power supply, and plug in those wires. Red > red, white > white, black > black.

Then go play with Home Assistant.  I setup a new dashboard with only a couple of buttons.  Setup notifications via the app to all registered mobile devices (the `notify.notify` was the secret).  If you want custom / interesting notifications and you don't know all the options, your favorite AI chatbot will help you with creating a YAML for it.

The features that RATGDO bring compared to what MyQ wanted for their limited ad-ladened app is amazing.  My new favorite is the ability to open the garage door to a specific height that I want instead of a full travel using the slider within Home Assistant.  Dude!  I can also turn the light on and off via the dashboard.  Something that MyQ never gave you, but the opener clearly has the functionality to do so.  

I got this working in less than 90 minutes.  This includes me submitting a form to delete my account from Chamberlain.

---

Other Posts You May Want To Cover in Syrup:
