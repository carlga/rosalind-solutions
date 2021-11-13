#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my @sequences = <F>;
close(F);
chomp(@sequences);

print(hammingDist($sequences[0], $sequences[1]));

exit;

sub hammingDist {
    my ($seq1, $seq2) = @_;
    my $diff;

    if (length($seq1) != length($seq2)) {
        die "Input sequences have different length\n";
    }

    for (my $i = 0; $i < length($seq1); $i++){
        if ((substr($seq1, $i, 1)) ne (substr($seq2, $i, 1))) {
            $diff++;
        }
    }
    return($diff);
}