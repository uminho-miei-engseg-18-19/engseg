#  Virtual Machine

**Notice**: As the semester goes by, software can be added to the virtual machine, so you will have to update it. So, it is better to save your work outside the virtual machine - for that you can use the shared directory with the *host* system.


The provided virutal machine  (Debian 9.7 Stretch 64 bits) has the following users/password:
+ root / root
+ user / user

The user *user* has sudo privileges, and should be used to solve the worksheets of the TP classes.

This VM uses the *MATE  Desktop Environment*. The following packages and applications that should be needed during this semester are installed:
+ eVotUM Cripto-py
+ Oracle JDK 9
+ Python 2 e 3
+ PHP 7
+ openssl
+ IDE PyCharm community
+ IDE atom
+ tor
+ secure-delete
+ curl
+ torbrowser-launcher
+ gdb
+ docker
+ WebGoat (on docker)

In addition, in the user "user", in the Tools directory, are installed:
+ ssh-audit (https://github.com/arthepsy/ssh-audit)
+ kali-anonsurf (https://github.com/Und3rf10w/kali-anonsurf.git)
+ GDB-Peda (https://github.com/longld/peda.git)

You can download the **.ova** file from the virtual machine at https://meocloud.pt/link/f188f15b-7145-4e11-b59e-6a64f61084a6/CSI.EngSeg.ova/ .


## VM Installation

   1. Install the latest version of OracleVM VirtualBox including the Extention Pack
   2. download the .ova file
   3. Import this file into Virtual Box; menu `File >> Import Appliance`
   4. Use the `Start` command, to boot the machine.
