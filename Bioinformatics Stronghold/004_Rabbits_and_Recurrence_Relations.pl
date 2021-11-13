#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $data = <F>;
close(F);
chomp($data);

my @data = split(' ', $data);

print(fib($data[0],$data[1]));

# Alter fibonacci to Fn = Fn-1 + Fn-2*k
sub fib {
    my ($n,$k) = @_;
	if ($n <= 1) {
        return $n;
    } else {
        return fib($n-1,$k) + fib($n-2,$k)*$k;
    }
}