#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $seq = <F>;
close(F);
chomp($seq);

print(translate($seq));

exit;

sub translate {
    my ($seq) = @_;
    my %codon_table = (
    'UCA' => 'S', # Serine
    'UCC' => 'S', # Serine
    'UCG' => 'S', # Serine
    'UCU' => 'S', # Serine
    'UUC' => 'F', # Phenylalanine
    'UUU' => 'F', # Phenylalanine
    'UUA' => 'L', # Leucine
    'UUG' => 'L', # Leucine
    'UAC' => 'Y', # Tyrosine
    'UAU' => 'Y', # Tyrosine
    'UAA' => '_', # Stop
    'UAG' => '_', # Stop
    'UGC' => 'C', # Cysteine
    'UGU' => 'C', # Cysteine
    'UGA' => '_', # Stop
    'UGG' => 'W', # Tryptophan
    'CUA' => 'L', # Leucine
    'CUC' => 'L', # Leucine
    'CUG' => 'L', # Leucine
    'CUU' => 'L', # Leucine
    'CCA' => 'P', # Proline
    'CAU' => 'H', # Histidine
    'CAA' => 'Q', # Glutamine
    'CAG' => 'Q', # Glutamine
    'CGA' => 'R', # Arginine
    'CGC' => 'R', # Arginine
    'CGG' => 'R', # Arginine
    'CGU' => 'R', # Arginine
    'AUA' => 'I', # Isoleucine
    'AUC' => 'I', # Isoleucine
    'AUU' => 'I', # Isoleucine
    'AUG' => 'M', # Methionine
    'ACA' => 'T', # Threonine
    'ACC' => 'T', # Threonine
    'ACG' => 'T', # Threonine
    'ACU' => 'T', # Threonine
    'AAC' => 'N', # Asparagine
    'AAU' => 'N', # Asparagine
    'AAA' => 'K', # Lysine
    'AAG' => 'K', # Lysine
    'AGC' => 'S', # Serine
    'AGU' => 'S', # Serine
    'AGA' => 'R', # Arginine
    'AGG' => 'R', # Arginine
    'CCC' => 'P', # Proline
    'CCG' => 'P', # Proline
    'CCU' => 'P', # Proline
    'CAC' => 'H', # Histidine
    'GUA' => 'V', # Valine
    'GUC' => 'V', # Valine
    'GUG' => 'V', # Valine
    'GUU' => 'V', # Valine
    'GCA' => 'A', # Alanine
    'GCC' => 'A', # Alanine
    'GCG' => 'A', # Alanine
    'GCU' => 'A', # Alanine
    'GAC' => 'D', # Aspartic Acid
    'GAU' => 'D', # Aspartic Acid
    'GAA' => 'E', # Glutamic Acid
    'GAG' => 'E', # Glutamic Acid
    'GGA' => 'G', # Glycine
    'GGC' => 'G', # Glycine
    'GGG' => 'G', # Glycine
    'GGU' => 'G'  # Glycine
    );
    my $prot;

    for(my $i = 0; $i < (length($seq)); $i += 3) {
        my $codon = substr($seq, $i, 3);
        if ($codon =~ /UAG|UGA|UAA/) {
            last;
        } elsif (exists $codon_table{$codon}) {
            $prot .= $codon_table{$codon};
        } else {
            die("Incorrect codon found\n");
        }
    }
    return($prot)
}