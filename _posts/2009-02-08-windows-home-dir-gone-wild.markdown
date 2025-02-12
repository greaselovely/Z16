---
layout: post
title:  "Home Directories Gone Wild"
date:   2009-07-08 15:07:37 -0700
categories: microsoft windows
---

Ok, Windows Admins who don't know this, listen up.
 
You know the way that you add home directories to user accounts in Active Directory? 
Yeah, you're not doing it right!
 
I have to say that I cannot stand it when admins don't read AT LEAST the bare minimum of basic Windows / Active Directory management. I cannot hold it back anymore, I feel like I'm gonna lose my mind. Everytime I go to a customer site and see where some chucklehead has added the home directory in some stupid way (see below).
 
 1. Create a new directory, either by calling the same as the username or something close.
 2. Share out this directory as a normal share or a hidden share
 3. Change NTFS permissions manually, or better yet, not at all.
 4. Open the user account properties and put in the drive letter and UNC path to this new share.
 
Ok, so now if you do anything in your life the correct way, do this (bare minimum):
 
 1. Create a single directory under whatever path you like (eg...D:\Home or D:\Users)
 2. Share this new directory, usually a hidden share (home$ or users$)
 3. Allow SYSTEM and Domain Admins Full Control and Domain Users Read Only
 4. Open user account properties and add the drive letter and the UNC path:
  (eg...\\server\share\%username%)
 5. You can literally use the %username% variable if you wanna.
 
Step 4 is the only step you have to do once you have created the initial share. What happens when you do step 4? Good question. It will create the home directory for you in the share specified and it will apply proper NTFS permissions with the user account with Full Control and remove the inheritance flag.
If you have a template user account and you copy it, it will create the home directory and apply security properly for you as well based on the username.
 
From now on, do this or I will come after you with a shovel and a hayfork.




---


Other Posts You May Want To Cover in Syrup: