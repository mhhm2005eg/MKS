#!/usr/bin/perl
 

 

##
 

## SETTINGS
 

##
 

 

$HEADER = <<EOH;
 

 

Microsoft Visual Studio Solution File, Format Version 11.00
 

# Visual Studio 2010
 

EOH
 

 

##
 

## END SETTINGS
 

##
 

 

print <<EOT;
 

Visual Studio Solution File Merge
 

By Tedd Hansen <tedd\@konge.net> Jan 2011
 

 

EOT
 

 

if ($#ARGV <= 0) {
 

  print "Required parameters: input1.sln,input2.sln output.sln\n";
 

  exit;
 

}
 

 

my %PROJECTS;
 

my %GLOBALSECTIONS;
 

my %GLOBALSECTIONSHEADER;
 

 

$INPUT = @ARGV[0];
 

$OUTPUT = @ARGV[1];
 

 

@INPUTS = split /,/, $INPUT;
 

print "Merging ".($#INPUTS+1)." files: ".$INPUT."\n";
 

print "Output: ".$OUTPUT."\n";
 

print "\n";
 

 

foreach my $file (@INPUTS)
 

{
 

  &READ($file);
 

}
 

&WRITE($OUTPUT);
 

 

sub WRITE
 

{
 

  open (OF, "> $OUTPUT");
 

    print OF $HEADER."\r\n";
 

    foreach my $proj (sort keys %PROJECTS)
 

    {
 

      print OF $PROJECTS{$proj};
 

    }
 

    print OF "Global\r\n";
 

    foreach $glob (keys %GLOBALSECTIONS)
 

    {
 

      print OF $GLOBALSECTIONSHEADER{$glob};
 

      my %tmp = map { $_ => 1 } split /\t/, $GLOBALSECTIONS{$glob};
 

      foreach my $line (keys %tmp)
 

      {
 

        print OF $line;
 

      }
 

      print OF "EndGlobalSection\r\n";
 

    }
 

    print OF "EndGlobal\r\n";
 

  close(OF);
 

}
 

 

sub READ
 

{
 

  #local $\ = "\r\n";
 

  my $file = shift;
 

 

  open (IF, "< $file");
 

    my $root = $file;
 

    $root =~ s/[^\\\/]+\.sln(_deploy)?$//i;
 

    while ($line = <IF>)
 

    {
 

       #$line =~ s/(\r|\n)$//mg;
 

       next if ($line =~ m/^(Microsoft Visual|# Visual Studio)/);
 

 

       ##
 

       ### SECTION: PROJECT
 

       ##
 

       #Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "PGSA.Contracts"
 

       if ($line =~ m/^\s*Project[^=]+=\s*"([^"]+)"/)
 

       {
 

         unless (exists($PROJECTS{lc($1)}))
 

         {
 

           $in_project = lc($1);
 

           #replace file
 

           $line =~ m/(^\s*Project[^=]+=\s*"[^"]+"\s*,\s*")([^"]+)(".*)/;
 

           my $loc = $root.$2;
 

           my $p1 = $1;
 

           my $p2 = $3;
 

           $loc =~ s/\//\\/g;
 

           $loc =~ s/\\\\+/\\/g;
 

           $loc =~ s/[^\\]+\\\.\.\\//g;
 

           $line = $p1.$loc.$p2;
 

         }
 

       }
 

       $PROJECTS{$in_project} .= $line if ($in_project);
 

       undef $in_project if ($line =~ m/^\s*EndProject/);
 

       ##
 

       ### END SECTION: PROJECT
 

       ##
 

 

       ##
 

       ### SECTION: GLOBALSECTION
 

       ##
 

       if ($line =~ m/^\s*GlobalSection\(([^\)]+)\)/)
 

       {
 

         $in_global = lc($1);
 

         $GLOBALSECTIONSHEADER{$in_global} .= $line;
 

       }
 

       undef $in_global if ($line =~ m/^\s*EndGlobalSection/);
 

       if ($in_global) {
 

         unless ($in_global eq "teamfoundationversioncontrol")
 

         {
 

           $line =~ s/\t/ /g;
 

           $GLOBALSECTIONS{$in_global} .= "\t".$line;
 

         }
 

       }
 

       ##
 

       ### END SECTION: GLOBALSECTION
 

       ##
 

 

    }
 

  close(IF);
 

}
 