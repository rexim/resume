#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

use JSON::Parse 'json_file_to_perl';
use Storable qw(dclone);
use Data::Dumper;
use Template;

sub match_tags($$) {
    my ($tags, $filter_tags) = @_;
    foreach (@$filter_tags) {
        if (not $_ ~~ $tags) {
            return 0;
        }
    }
    return 1;
}

sub filter_entries_by_tags($$) {
    my ($entries, $tags) = @_;
    my @filtered_entries = grep {
        (not defined $_->{tags}) || match_tags($_->{tags}, $tags);
    } @$entries;
    return \@filtered_entries;
}

sub filter_sections_by_tags($$) {
    my ($sections, $tags) = @_;
    foreach (@$sections) {
        $_->{entries} = filter_entries_by_tags($_->{entries}, $tags)
    }
}

sub filter_resume_by_tags($$) {
    my ($resume, $tags) = @_;
    filter_sections_by_tags($resume->{sections}, $tags);
}

my $resume = json_file_to_perl("./resume.json");
filter_resume_by_tags($resume, \@ARGV);
my $template = Template->new({ RELATIVE => 1,
                               ENCODING => 'utf8' });
$template->process("./resume.tt",
                   $resume,
                   "./resume.tex",
                   { binmode => ':utf8' }) || die $template->error();

1;
