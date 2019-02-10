# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# createSharedSecret-app.py
#
# Cripto-4.1.1 - Commmad line app to exemplify the usage of createSharedSecretComponents
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
Command line app that reads the number of shares, quorum, uid and private key file
from command line. The private key passphrase and the secret are asked by the app.
The JSON Web Signature (JWS) list components are written to STDOUT and errors (if
existant) are written to STDERR.
"""

import sys
from eVotUM.Cripto import shamirsecret 


def printUsage():
    print("Usage: python createSharedSecret-app.py number_of_shares quorum uid private-key.pem")

def parseArgs():
    if (len(sys.argv) != 5):
        printUsage()
    else:
        keyPassphrase = raw_input("Private key passphrase: ")
        secret = raw_input("Secret: ")
        nShares = int(sys.argv[1])
        quorum = int(sys.argv[2])
        uid = sys.argv[3]
        privateKeyPath = sys.argv[4]
        main(secret, nShares, quorum, uid, privateKeyPath, keyPassphrase)

def readFile(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def main(secret, nShares, quorum, uid, privateKeyPath, keyPassphrase):
    pemPrivateKey = readFile(privateKeyPath)
    errorCode, shamirSecretComponents = shamirsecret.createSharedSecretComponents(secret, nShares, quorum, uid, pemPrivateKey, keyPassphrase)
    if (shamirSecretComponents is not None):
        for i in range(len(shamirSecretComponents)):
            sys.stdout.write("Component: %s\n" % (i+1))
            sys.stdout.write(shamirSecretComponents[i])
            sys.stdout.write("\n")
    else:
        sys.stderr.write("Error. " + {
            1: "At least one of the JWS objects could not be created. Your private key file may not be in PEM format or the key passphrase may be wrong.",
            11: "Invalid secret length. Maximum secret length: %s." % shamirsecret.SECRET_MAX_BYTES_LENGTH,
            12: "Invalid quorum. Minimum quorum: %s." % shamirsecret.MIN_SHARES,
            13: "Invalid quorum. Quorum must be less or equal to number of shares",
            14: "Invalid number of shares. Maximum number of shares: %s." % shamirsecret.MAX_SHARES
            }.get(errorCode, "Unknown error %s." % errorCode))

if __name__ == "__main__":
    parseArgs()
