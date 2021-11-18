#!/usr/bin/perl
use warnings;
use strict;

my $fileName = shift or die "No file provided\n";

open(F, $fileName) or die "File not found\n";
my @data = <F>;
close(F);
chomp(@data);

# Find motif locations
my @positions = @{findSubstr($data[0],$data[1])}; 
print(join(" ", @positions));

exit;


sub indexSeq {
    my ($seq) = @_;
    my @idx_mat;

    my %row_n = ('A'=>'0', 'C'=>'1', 'G'=>'2', 'T'=>'3');

    # Read motif backwards and store positions of closest nucleotides (A,C,G,T)
    for (my $i = length($seq)-1; $i >= 0; $i--) {
        my $n = $row_n{substr($seq, $i, 1)};
        
        for (my $ii = $i-1; $ii >= -1; $ii--) {
            $idx_mat[$n][$i] = '-';

            # Skip to next position if closest nucleotides are set in index
            last if ((defined $idx_mat[0][$i])
                && (defined $idx_mat[1][$i])
                && (defined $idx_mat[2][$i])
                && (defined $idx_mat[3][$i]));
            
            # Save distance of nucleotide with respect to current position
            if (($n!=0) && (substr($seq,$ii,1) eq 'A') && (!defined $idx_mat[0][$i])) {
                $idx_mat[0][$i] = $i-$ii-1;
            } elsif (($n!=1) && (substr($seq,$ii,1) eq 'C') && (!defined $idx_mat[1][$i])) {
                $idx_mat[1][$i] = $i-$ii-1;
            } elsif (($n!=2) && (substr($seq,$ii,1) eq 'G') && (!defined $idx_mat[2][$i])) {
                $idx_mat[2][$i] = $i-$ii-1;
            } elsif (($n!=3) && (substr($seq,$ii,1) eq 'T') && (!defined $idx_mat[3][$i])) {
                $idx_mat[3][$i] = $i-$ii-1;
            }
            
            # Store max distance for nucleotides which are not found
            if ($ii == -1) {
                for (my $w = 0; $w < 4; $w++) {
                    if (!defined $idx_mat[$w][$i]) {
                        $idx_mat[$w][$i] = $i-$ii-1;
                    }
                }
            }
        }
    }
    return(\@idx_mat);
}

sub findSubstr {
    my ($seq, $motif) = @_;
    my @motif_idx = @{indexSeq($motif)};
    my %row_n = ('A'=>'0', 'C'=>'1', 'G'=>'2', 'T'=>'3');
    my @positions;

    for (my $i = length($motif)-1; $i <= length($seq); $i++) {
	    my $ct = length($motif)-1;
	
        for (my $j = $i; $j > ($i-length($motif)); $j--) {
            if (substr($seq,$j,1) ne substr($motif,$ct,1)){
                $i += ($motif_idx[$row_n{substr($seq,$j,1)}][$ct]);
                last;}
            else{
                if ($ct == 0){
                    # Add 1 to have 1-base position
                    push(@positions, $j+1);
                }
                $ct--;
            }
        }
    }
    return(\@positions)
}