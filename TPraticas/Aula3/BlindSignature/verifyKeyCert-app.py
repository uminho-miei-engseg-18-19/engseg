# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# verifyKeyCert-app.py
#
# Cripto-7.5.0 - Commmad line app to verify if the private key has the correspondant
#           certificate.
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
Command line app that verifies if the private key has the correspondant certificate..
"""

import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import shamirsecret
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verifyKeyCert-app.py private-key.pem public-key.pem")

def parseArgs():
    if (len(sys.argv) != 3):
        printUsage()
    else:
        eccPrivateKeyPath = sys.argv[1]
        eccPublicKeyPath = sys.argv[2]
        main(eccPrivateKeyPath, eccPublicKeyPath)

def showResults(errorCode, validSignature):
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPrivateKeyPath, eccPublicKeyPath):
    initComponents, pRDashComponents = eccblind.initSigner()
    data = shamirsecret.generateSecret(80)
    errorCode, [blindComponents, pRComponents, blindM] = eccblind.blindData(pRDashComponents, data)
    pemKey = utils.readFile(eccPrivateKeyPath)
    passphrase = raw_input("Passphrase: ")
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, initComponents)
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
