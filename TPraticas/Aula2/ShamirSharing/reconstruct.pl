#! /usr/bin/perl -w

# An implementation of key reconstruction from

# Shamir A.,
# How to Share a Secret,
# Communications of the ACM, 22, 1979, pp. 612--613.

# This implementation was written by Charles Karney <charles@karney.com>
# in 2001 and is licensed under the GPL.  For more information, see
# http://charles.karney.info/misc/secret.html

# l = 8 = number of bits in subkey
# n = number of shares
my $q = 257; # prime > max(2^l, n)
my @invtab = ();

sub modq {			# Mod q
    return ($_[0] % $q);
}

sub calcinvtab {		# Calculate y=1/x and store in table
    my ($x, $y) = (1, 1);
    $invtab[0] = 0;
    for (my $i = 1; $i < $q; $i++) {
	$invtab[$x] = $y;
	# work with powers of 3.  This marches thru all the values of q = 257
	$x = modq(3 * $x);
	$y = modq(86 * $y); # 3 * 86 = 1
    }
    die "inverse screw up" if $x != 1;
}

sub inv {			# Look up inverse
    return ($_[0] < 0 ? modq(- $invtab[- $_[0]]) : $invtab[$_[0]]);
}

my $count = 0;
my $quorum;
my @shx = ();
my @shy = ();
my $usage = "usage: $0
share1
share2
...
";

die "$usage" if $#ARGV != -1;

while (<STDIN>) {
    chomp;
    my ($k, $j, $sh) = split(/:/);
    if ($count == 0) {
	$quorum = $k;
	$keylen = length($sh);
	die 'share not of even length' if $keylen % 2 != 0;
	die "bad quorum value $quorum" if $quorum < 1 or $quorum > 256;
    } else {
	die "mismatched quorum $k" if $k != $quorum;
	die "mismatched key lengths" if $keylen != length($sh);
    }
    $count++;
    die "bad share index $j" if $j < 1 or $j > 256;
    if ($count > $quorum) {
	print "Ignoring share $j...\n";
	next;
    }
    push @shx, $j;
    for (my $i = 0; $i < $keylen; $i += 2) {
	my $t = substr $sh, $i, 2;
	die "bad hex pair $t" if (($t !~ /[0-9a-f][0-9a-f]/) and ($t ne "g0"));
	push(@shy, ($t eq "g0") ? 256 : hex $t);
    }
}

die "$usage" if $count == 0;
die "too few shares" if $count < $quorum;
$keylen /= 2;

calcinvtab;			# Initialize inverse table

my @shcoef = ();
# Calculate common coeeficients
for (my $j = 0; $j < $quorum; $j++) {
    my $temp = 1;
    for (my $l = 0; $l < $quorum; $l++) {
	if ($l != $j) {
	    $temp = modq(- $temp * $shx[$l] * inv($shx[$j] - $shx[$l]));
	}
    }
    die "repeated share" if ($temp == 0);
    push @shcoef, $temp;
}
    
my @ans = ();
for (my $i = 0; $i < $keylen; $i++) {
    my $temp = 0;
    for (my $j = 0; $j < $quorum; $j++) {
	$temp = modq($temp + $shy[$keylen * $j + $i] * $shcoef[$j]);
    }
    die "bad result" if ($temp == 256);
    push @ans, chr($temp);
}
print join("", @ans),"\n";
