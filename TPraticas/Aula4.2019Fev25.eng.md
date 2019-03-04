# TP  Class Assignment - 25/Feb/2019

Each group must answer the questions of the following exercises in the Github area of their group until the end of 05/Mar/2019\. For each day of delay, 0.15 points will be deducted from the grade of this assignment.

Note that the virtual machine provided for this course can be used to solve these exercises.


## Exercises

### 1\. TOR (The Onion Router)


To answer to this exercise, you'll need to install **tor**, **secure-delete**, **curl**, and **anonsurf** in the user account _user_ on the virtual machine. It is suggested that you perform the following sequence of commands:

> `sudo apt-get install tor secure-delete curl`

> `cd ~/Tools`

> `git clone https://github.com/Und3rf10w/kali-anonsurf.git`

> `cd kali-anonsurf`

> `sudo ./installer.sh`

Note: if you are using the virtual machine provided for this course, these tools may already be installed.


#### Experience 1.1

Let's use TOR (via the `anonsurf` command line interface) to change your geographic location.


1. Open the browser and go to <http://myiplocator.net/>

    - Write down your IP address and location (you can also get it via the `sudo anonsurf myip` command)

2. On the command line run `sudo anonsurf start`
3. Reload (shift-reload) the webpage you were on

    - Write down your IP address and location (if it has not changed, it's because there was an error)

4. On the command line run  `sudo anonsurf change`
5. Reload (shift-reload) the webpage you were on

    - Write down your IP address and location (if it has not changed, it's because there was an error)

6. On the command line run  `sudo anonsurf stop`
7. Reload (shift-reload) the webpage you were on

    - Write down your IP address and location (if it is not the initial one, it's because there was an error)

#### Question P1.1

To access some sites in the USA you must be located in the USA.

1. Does the command `sudo anonsurf start` guarantee that you are located in the USA?
2. Why? Use TOR features to justify.

#### Experience 1.2

We will use the "TOR Browser" to navigate anonymously in the network. For this you need to install the **torbrowser-launcher** in the user account _user_ in the virtual machine.

It is suggested that you perform the following sequence of commands:

> `sudo su`

> `echo "deb http://deb.debian.org/debian stretch-backports main contrib" > /etc/apt/sources.list.d/stretch-backports.list`

> `exit`

> `sudo apt-get update`

> `sudo apt-get install torbrowser-launcher`

> In the top menu bar of the virtual machine, go to Applications / Internet / Tor Browser, in order to finish the browser installation

> If after finishing the installation the TOR browser doesn't open, select Applications / Internet / Tor Browser again

Note: if you are using the virtual machine provided for this course, the TOR browser may already be installed.


A. In the TOR browser go to the <https://blog.torproject.org/italian-anti-corruption-authority-anac-adopts-onion-services> page. Click on the left side of the URL bar and check the circuit to reach the site.

B. Open another tab in the TOR browser and go to the <https://www.expressvpn.com/blog/best-onion-sites-on-dark-web/> page. Click on the left side of the URL bar and check the circuit to reach the site.

What is your conclusion?

#### Question P1.2

In the light of the previous experience, go to <http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page> or <https://www.facebookcorewwwi.onion/>.

1. Click on the left side of the URL bar and check the circuit to reach the site.

2. Why are there 6 "jumps" to the Onion site, 3 of which are "_relay_"? Use TOR features to justify.


----

##  Engenharia de Segurança course - Project

You can use the rest of the class for the Engenharia de Segurança project.
