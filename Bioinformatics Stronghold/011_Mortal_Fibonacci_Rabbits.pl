#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $data = <F>;
close(F);
chomp($data);

my ($n,$m) = split(' ', $data);

print(fib($n,$m,1,2));

exit;

# Recursive approach is quite slow for large numbers
sub fib {
    my ($n,$m,$k,$g) = @_;
	if ($n == 0) {
        return 0;
    
    } elsif ($n < $g) {
        return 1;

    # Fn = Fn-1 + F(n-g)*k before F0 dies
    } elsif ($n <= $m) {
        return fib($n-1,$m,$k,$g) + fib($n-$g,$m,$k,$g)*$k;

    # Fn = Fn-1 + F(n-g)*k - 1 when F0 dies
    } elsif ($n == $m+1) {
        return fib($n-1,$m,$k,$g) + fib($n-$g,$m,$k,$g)*$k - 1;
    
    # Fn = Fn-1 + F(n-g)*k - Fn-(n-m-1) after F0 dies
    } else {
        return fib($n-1,$m,$k,$g) + fib($n-$g,$m,$k,$g)*$k - fib($n-$m-1,$m,$k,$g);
    }
}