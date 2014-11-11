codewallet
==========

Read a codewallet export file and turn it into something keepass2 can import

I had a file sitting around that was a export from CodeWallet and it needed to be imported into Keepass2.  It was in the format of something like

Category
Card Name
Username
Site
Password
Notes

Not CSV, and not all elements were present in each entry.  So I made this to go through them and turn it into a CSV that can be imported by Keepass2.
