#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my $data = <F>;
close(F);
chomp($data);

my @data = split(' ', $data);

# Calculate probability of F1 with dominant phenotype
my $A_prob = @{inheritProb(@data)}[0] + @{inheritProb(@data)}[1];
print($A_prob);

exit;

# Calculates genotype probabilities for F1 offspring
sub inheritProb {
    my ($k,$n,$m) = @_;
	my $pop_n = eval(join('+', ($k,$n,$m)));
    
    # Offspring n for F1 = C(P,2) * 4 (matings x F1 genotypes)
    my $f1_n = $pop_n*($pop_n-1)/2 * 4;

    # Homozygous dominiant (AA) F1 offspring n
    my $AA_f1_n = 4*$k*($k-1)/2 + 2*$k*$n + $n*($n-1)/2;

    # Homozygous recessive (aa) F1 offspring n
    my $aa_f1_n = 4*$m*($m-1)/2 + 2*$m*$n + $n*($n-1)/2;

    # Heterozygous (Aa) F1 offspring n
    my $Aa_f1_n = $f1_n - $AA_f1_n - $aa_f1_n;
    # my $Aa_f1_n = 4*$k*$m + 2*$n*($n-1)/2 + 2*$k*$n + 2*$n*$m;
    
    my @f1_probs = ($AA_f1_n/$f1_n, $Aa_f1_n/$f1_n, $aa_f1_n/$f1_n);
    return(\@f1_probs);
}