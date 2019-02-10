# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateSecret-app.py
#
# Cripto-4.4.1 - Commmad line app to exemplify the usage of generateSecret
#       function (see shamirsecret.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that generates a random string with length characters.
"""

import sys
from eVotUM.Cripto import shamirsecret 


def printUsage():
    print("Usage: python generateSecret-app.py length")

def parseArgs():
    if (len(sys.argv) != 2):
        printUsage()
    else:
        length = int(sys.argv[1])
        main(length)

def main(length):
    sys.stdout.write("%s\n" % shamirsecret.generateSecret(length))

if __name__ == "__main__":
    parseArgs()
