#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $seq = <F>;
close(F);
chomp($seq);

my $A=0;
my $C=0;
my $G=0;
my $T=0;

for(my $i=0; $i<length($seq); $i++){		
	my $nt = substr($seq,$i,1);				
	if ($nt eq 'A'){$A++;}
	elsif ($nt eq 'C'){$C++;}		
	elsif ($nt eq 'G'){$G++;}
	elsif ($nt eq 'T'){$T++;}
}

print "$A $C $G $T";