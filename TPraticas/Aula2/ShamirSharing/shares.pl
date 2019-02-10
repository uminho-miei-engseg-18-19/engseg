#! /usr/bin/perl -w

# An implementation of key sharing from

# Shamir A.,
# How to Share a Secret,
# Communications of the ACM, 22, 1979, pp. 612--613.

# This implementation was written by Charles Karney <charles@karney.com>
# in 2001 and is licensed under the GPL.  For more information, see
# http://charles.karney.info/misc/secret.html

# To keep the arithmetic simple, the algorithm is applied to the key one
# byte at a time.

# l = 8 = number of bits in subkey
# n = number of shares
my $q = 257; # prime > max(2^8, n)

sub modq {
    return ($_[0] % $q);
}

# random num in [0, 257)
# note 257 * 255 = 65535, so
# first generate random num in [0, 65535)
sub randq {
    my @num;
    do {
	my $temp = `dd if=/dev/random bs=1 count=2 2> /dev/null`;
	@num = unpack('S',$temp);
    } until $num[0] < 65535;
    return modq($num[0]);
}

# print a hex number using g0 for 256.
sub hexq {
    if ( $_[0] < 256 ) {
	return sprintf("%02x", $_[0]);
    } else {
	return "g0"
	}
}

sub horner {
    # Evaluate polynomial via Horner's rule.  Indep var is first,
    # then the coeffs starting with the leading one.
    my $x  = shift @_;
    my @coeffs = @_;
    my $val = 0;
    foreach $c (@coeffs) {
	$val = modq( $x * $val + $c );
    }
    return $val;
}

sub thresh {
    my ($b, $k, $n) = @_;
    my @coeffs = ();
    for (my $i = 1; $i < $k; $i++) {
	push(@coeffs, randq);
    }
    # const coeff goes last
    push(@coeffs, $b);
    my @res = ();
    for (my $i = 0; $i < $n; $i++) {
	push(@res, horner($i+1, @coeffs));
    }
    return @res;
}

my $usage = "usage: echo KEY | $0 K N
where
    N = number of shares
    K = quorum
    0 < K <= N <= 256

output is N lines.  Store each line separately together with a copy of
reconstruct.pl.  Restore with any K of the lines fed to reconstruct.pl.
";

die $usage if $#ARGV != 1;

my $n = $ARGV[1];
die "bad value of shares: $n\n$usage" if $n < 1 or $n > 256;

my $k = $ARGV[0];
die "bad value of quorum: $k\n$usage" if $k < 1 or $k > $n;

$_ = <STDIN>;
chomp;
my $len = length($_);		# number of subkeys
my @key = unpack('C*',$_);

@result = ();
foreach $key (@key) {
    push(@result, thresh($key, $k, $n));
}

for (my $i = 0; $i < $n; $i++) {
    printf "%d:%d:", $k, $i+1;
    for (my $j = 0; $j < $len; $j++) {
	print hexq($result[$j * $n + $i]);
    }
    print ":\n";
}
