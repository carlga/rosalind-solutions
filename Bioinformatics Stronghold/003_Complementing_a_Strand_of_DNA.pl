#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $seq = <F>;
close(F);
chomp($seq);

$seq = reverse($seq);
$seq =~ tr/ATGC/TACG/;

print "$seq"