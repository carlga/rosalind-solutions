#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

# Read sequences from fasta file
my %sequences = %{readFasta($fileName)};

# Retrieve sequence with highest GC%
my $topHeader;
my $topGC = 0;
foreach(keys(%sequences)) {
    my $GC = contentGC($sequences{$_}, 1, 1);
    if($GC > $topGC) {
        $topHeader = $_;
        $topGC = $GC;
    }
}

printf("%s\n%f\n", $topHeader, $topGC);

exit;

sub readFasta{
    my ($fileName) = @_;
    my %sequences;
    my $header;

    open(F, $fileName) or die "File not found\n";

    while(<F>) {
        chomp($_);
        next if($_ =~ /^\s*$/); # Skip empty lines
        if($_ =~ /^>/) {
            $header = $_;
            $header =~ s/>//;
            if (exists $sequences{$header}) {
                die "Duplicated entries in file: $header\n";
            }
        } else {
            next if(!$header);
            $sequences{$header} .= $_; # Concatenate sequence fragments
        }
    }
    close(F);
    return(\%sequences);
}

sub contentGC {
    my ($seq, $step, $window) = @_;
    my @GC;

    if($step > $window) {
        die "Step size cannot be greater than window\n";
    }

    # Whole sequence %GC with step = 1 & window = 1
    if($step == 1 && $window == 1) {
        return(($seq =~ tr/GC//) / length($seq) * 100);
    
    # Otherwise returns array with sliding window GC%
    } else {
        for (my $i = 0; $i < length($seq); $i += $step) {
            my $frag = substr($seq, $i, $window);
            push(@GC, ($frag =~ tr/GC//) / $window * 100)
        }
        return(\@GC)
    }
}