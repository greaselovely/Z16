---
layout: post
title: "OpenVAS On Kali"
date: 2025-02-22 00:00:00 -0600
categories: security vulnerability scanning
tags: openvas
---
Today I decided it was time to take a slightly more proactive approach to vulnerability scanning my network at home.  

Like most I have IOT, and while I don't think I win the award for most ridiculous amount of gear, I'm no slouch either.  I also have invested in Control4 for some home automation, and Home Assistant for other integrations.  Now, I know I could do some of the things that Control4 does with a little more effort, but I like how it works for some of my solutions.  And while it's a black box with a partner holding the keys, for now I live with it.  

But I've been growing angry at the idea that I'm no longer in control of software upgrades, and the partner doesn't give a damn if there's new CVEs in the software / modules in use.  That's not their expertise and so I'm going to do a bit more work on that on my own.

So the setup I have is simple.  A Kali VM on Proxmox that I have had for a while, so I have to get it updated first.

`sudo apt update`

`sudo apt upgrade`

`sudo reboot`

Referencing the setup from Greenbone's Github page: 
`https://greenbone.github.io/docs/latest/22.4/kali/index.html`

`sudo apt install gvm`

This ran fine, no problem!  Nice.

Next step, let's get it operational 

`sudo gvm-setup`

No joy

```
sudo gvm-setup

[>] Starting PostgreSQL service
[-] ERROR: The default PostgreSQL version (16) is not 17 that is required by libgvmd
[-] ERROR: libgvmd needs PostgreSQL 17 to use the port 5432
[-] ERROR: Use pg_upgradecluster to update your PostgreSQL cluster
```

So PostgreSQL on my box is running version 16 and vesion 17.  How do I know?  Run the following:

```
┌──(kali㉿kali)-[~]
└─$ pg_lsclusters

Ver Cluster Port Status Owner    Data directory              Log file
16  main    5432 online postgres /var/lib/postgresql/16/main /var/log/postgresql/postgresql-16-main.log
17  main    5433 online postgres /var/lib/postgresql/17/main /var/log/postgresql/postgresql-17-main.log

```

But as the error above indicates, version 16 is my default.  And becuase my GAF is low, I don't care about keeping 16.  Let's ravage this thing as if it were a lone pillow in a bachelor's one room apartment.

First, stop PostrgreSQL.
`sudo systemctl stop postgresql`

I attempted to upgrade to 17 without thinking it through.  Don't be me.

```
sudo pg_upgradecluster 16 main

Error: target cluster 17/main already exists
```

Ok, let's get rid of 17 and drop it like it's <redacted>

`sudo pg_dropcluster 17 main --stop`

Let's now take the default version of 16 and upgrade it.

`sudo pg_upgradecluster 16 main`

This is going to run a bit so let it do its thing.  Once it's done, you should see this:

```
Success. Please check that the upgraded cluster works. If it does,
you can remove the old cluster with
    pg_dropcluster 16 main
```

My friend told me I should so I did!

`pg_dropcluster 16 main`

Now, do this!

```
pg_lsclusters

Ver Cluster Port Status Owner    Data directory              Log file
17  main    5432 online postgres /var/lib/postgresql/17/main /var/log/postgresql/postgresql-17-main.log
```

Boom goes the dynamite.  We have ugpraded.  Now let's get rid of version 16 for good.

`sudo apt remove postgresql-16`


For the hell of it, let's bounce the database.

`sudo systemctl restart postgresql`

We are now good to go get OpenVAS setup.

`sudo gvm-setup`

It's going to do a lot of things to get it operational, here's an edited output of the beginning and end of the process.

```
[>] Starting PostgreSQL service

[>] Creating GVM's certificate files

~ truncated

[*] Creating extension pg-gvm
CREATE EXTENSION
[>] Migrating database
[>] Checking for GVM admin user
[*] Creating user admin for gvm
[*] Please note the generated admin password

~ truncated

[*] Checking Default scanner
[*] Modifying Default Scanner
Scanner modified.

[>] You can now run gvm-check-setup to make sure everything is correctly configured
```

In the output, you'll be provided an admin password, make note of it or something.  Ya know, or don't.

Finally, we can test that it is setup correctly using the following command

`sudo gvm-check-setup`

At the end of the output, you should see:

`It seems like your GVM-23.11.0 installation is OK.`

This is good news for us.  And Kali continues to appear stable as well.

It's accessible from the local machine by default.  Simply go to `https://localhost:9392`

![OpenVAS_Login]({{ site.baseurl }}/images/OpenVASLogin.png "OpenVAS_Login")


The team at Greenbone also gives us the instructions on allowing remote access to the web interface.  

Edit `/usr/lib/systemd/system/gsad.service` and update this line 

`ExecStart=/usr/local/sbin/gsad --foreground --listen=127.0.0.1 --port=9392`

Changing the binding from only listening on the loopback to listening to all IPs (0.0.0.0) and change it to listen on the default SSL/TLS port of TCP/443 (if you want), you can also choose to keep it on the default alternate port if you want or if you have other things bound to TCP/443.

`ExecStart=/usr/local/sbin/gsad --foreground --listen=0.0.0.0 --port=443`

Restart the `gsad` service

```
sudo systemctl daemon-reload
sudo systemctl restart gsad
```

Now, here's the thing, the above commands were taken from their page as of this writing.  
However, looking at the file itself, the file does not contain the `=` sign.  

If you want to be lazy like me, here's a one-liner to edit and restart for you.

`sudo sed -i 's|--listen [^ ]*|--listen 0.0.0.0|; s|--port [0-9]*|--port 443|' /usr/lib/systemd/system/gsad.service && sudo systemctl daemon-reload && sudo systemctl restart gsad`

Access it from a remote machine if nothing went wrong!

![OpenVASRemoteLogin]({{ site.baseurl }}/images/OpenVASRemoteLogin.png "OpenVASRemoteLogin")


Hell yeah.  Now scan the network and resolve the CVEs!



---

Other Posts You May Want To Cover in Syrup:
