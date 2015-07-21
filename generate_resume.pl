#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

use JSON::Parse 'json_file_to_perl';
use Data::Dumper;
use Template;

my $resume = json_file_to_perl("./resume.json");
my $template = Template->new({ RELATIVE => 1,
                               ENCODING => 'utf8' });
$template->process("./resume.tt",
                   $resume,
                   "./resume.tex",
                   { binmode => ':utf8' }) || die $template->error();

1;
