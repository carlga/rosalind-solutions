#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $seq = <F>;
close(F);
chomp($seq);

$seq =~ s/T/U/gi;

print "$seq"