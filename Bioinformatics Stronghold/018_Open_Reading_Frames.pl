#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $seq;
while (<F>) {				
	chomp ($_);
	if ($_=~/^[ATGC]+$/i) {
	$seq.=$_;
    }
}				
close(F);

my @peptides;
my $eq="first";
for (my $x=0; $x<2; $x++) {
	if ($x==1) {				
	$seq=reverse($seq);
	$seq=~tr/ATGC/TACG/;
    }

	for (my $i=0; $i<3;$i++) {
	my $start;
		for(my $z=$i; $z<length($seq) ;$z+=3) {
			my $cod= substr ($seq,$z,3);
			if (($cod eq 'ATG') and (!defined $start)) {
				$start=$z;
            }
			
			elsif ((defined $start) and ($cod=~/TAG|TGA|TAA/)) {
				if ($eq eq "first") {
					push (@peptides,translate($seq, $start));
					$eq = "false";
                } 
                else {
					foreach (@peptides) {
						if ($_ eq translate($seq, $start)) {
							$eq="true";
                        } 
                        else { next; } 
                    }
					if ($eq ne "true"){
						push (@peptides,translate($seq, $start)); 
                    }			
					$eq ="false";
					$z=$start;
					undef $start;
                }
			}
		}
	}
}

foreach (@peptides) {
	print"$_\n";
}

				
exit;


sub translate {
    my ($seq, $start) = @_;
    my %genetic_code = (
    'TCA' => 'S', # Serine
    'TCC' => 'S', # Serine
    'TCG' => 'S', # Serine
    'TCT' => 'S', # Serine
    'TTC' => 'F', # Phenylalanine
    'TTT' => 'F', # Phenylalanine
    'TTA' => 'L', # Leucine
    'TTG' => 'L', # Leucine
    'TAC' => 'Y', # Tyrosine
    'TAT' => 'Y', # Tyrosine
    'TAA' => '_', # Stop
    'TAG' => '_', # Stop
    'TGC' => 'C', # Cysteine
    'TGT' => 'C', # Cysteine
    'TGA' => '_', # Stop
    'TGG' => 'W', # Tryptophan
    'CTA' => 'L', # Leucine
    'CTC' => 'L', # Leucine
    'CTG' => 'L', # Leucine
    'CTT' => 'L', # Leucine
    'CCA' => 'P', # Proline
    'CAT' => 'H', # Histidine
    'CAA' => 'Q', # Glutamine
    'CAG' => 'Q', # Glutamine
    'CGA' => 'R', # Arginine
    'CGC' => 'R', # Arginine
    'CGG' => 'R', # Arginine
    'CGT' => 'R', # Arginine
    'ATA' => 'I', # Isoleucine
    'ATC' => 'I', # Isoleucine
    'ATT' => 'I', # Isoleucine
    'ATG' => 'M', # Methionine
    'ACA' => 'T', # Threonine
    'ACC' => 'T', # Threonine
    'ACG' => 'T', # Threonine
    'ACT' => 'T', # Threonine
    'AAC' => 'N', # Asparagine
    'AAT' => 'N', # Asparagine
    'AAA' => 'K', # Lysine
    'AAG' => 'K', # Lysine
    'AGC' => 'S', # Serine
    'AGT' => 'S', # Serine
    'AGA' => 'R', # Arginine
    'AGG' => 'R', # Arginine
    'CCC' => 'P', # Proline
    'CCG' => 'P', # Proline
    'CCT' => 'P', # Proline
    'CAC' => 'H', # Histidine
    'GTA' => 'V', # Valine
    'GTC' => 'V', # Valine
    'GTG' => 'V', # Valine
    'GTT' => 'V', # Valine
    'GCA' => 'A', # Alanine
    'GCC' => 'A', # Alanine
    'GCG' => 'A', # Alanine
    'GCT' => 'A', # Alanine
    'GAC' => 'D', # Aspartic Acid
    'GAT' => 'D', # Aspartic Acid
    'GAA' => 'E', # Glutamic Acid
    'GAG' => 'E', # Glutamic Acid
    'GGA' => 'G', # Glycine
    'GGC' => 'G', # Glycine
    'GGG' => 'G', # Glycine
    'GGT' => 'G'  # Glycine
    );
    my $protein;

    for(my $i=$start; $i<(length($seq)-2); $i+=3) {
        my $codon=substr($seq,$i,3);
        if ($codon=~/TAG|TGA|TAA/) { last; }
        elsif (exists $genetic_code{$codon}) {
            $protein.=$genetic_code{$codon};
        }
        else {
            print"Codon $codon is not recognized\n";
        }
    }

    return($protein);
}