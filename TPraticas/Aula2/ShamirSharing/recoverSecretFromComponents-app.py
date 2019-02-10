# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# recoverSecretFromComponents-app.py
#
# Cripto-4.2.1 - Commmad line app to exemplify the usage of recoverSecretFromComponents
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
Command line app that reads the number of shares, uid and certificate file from command
line. The app starts asking for the input of the shares and prints
the recovered secret to STDOUT or appropriate error to STDERR.
"""

import sys, colored
from eVotUM.Cripto import shamirsecret 


def printUsage():
    print("Usage: python recoverSecretFromComponents-app.py number_of_shares uid cert.pem")

def parseArgs():
    if (len(sys.argv) != 4):
        printUsage()
    else:
        nShares = int(sys.argv[1])
        uid = sys.argv[2]
        certificatePath = sys.argv[3]
        main(nShares, uid, certificatePath)

def readFile(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def showResults(errorCode, secret, uid):
    if (errorCode is None):
        sys.stdout.write("%sRecovered secret:%s %s" % (colored.fg("green"), colored.attr("reset"), secret))
    else:
        sys.stderr.write({
            1: "%sError: The certificate is not within the validity period %s" % (colored.fg("red"), colored.attr("reset")),
            2: "%sError: The certificate format is invalid (not PEM) %s" % (colored.fg("red"), colored.attr("reset")),
            3: "%sError: It was not possible to retrieve the public key from the certificate %s" % (colored.fg("red"), colored.attr("reset")),
            4: "%sError: One of the components/parts is not well formated or was not signed with the private key associated to the certificate's public key %s" % (colored.fg("red"), colored.attr("reset")),
            10: "%sError: There are repeated components %s" % (colored.fg("red"), colored.attr("reset")),
            11: "%sError: The number of shares is less than quorum %s" % (colored.fg("red"), colored.attr("reset")),
            12: "%sError: One of the components/parts has not the usage id %s %s" % (colored.fg("red"), uid, colored.attr("reset")),
            13: "%sError: The recovered secret has an invalid length %s" % (colored.fg("red"), colored.attr("reset")),
            14: "%sError: Invalid number of components %s" % (colored.fg("red"), colored.attr("reset")),
            15: "%sError: Invalid hash %s" % (colored.fg("red"), colored.attr("reset"))
            }.get(errorCode, "%sUnknown error: %s %s" % (colored.fg("red"), errorCode, colored.attr("reset"))))

def main(nShares, uid, certificatePath):
    pemCertificate = readFile(certificatePath)

    shamirSecretComponents = []
    for i in range(nShares):
        shamirSecretComponents.append(raw_input("Component %s: " % (i+1)))

    errorCode, secret = shamirsecret.recoverSecretFromComponents(shamirSecretComponents, uid, pemCertificate)
    showResults(errorCode, secret, uid)

if __name__ == "__main__":
    parseArgs()
