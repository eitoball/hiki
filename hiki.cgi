#!/usr/bin/env ruby
# $Id: hiki.cgi,v 1.11 2004-02-15 03:09:04 hitoshi Exp $
# Copyright (C) 2002-2004 TAKEUCHI Hitoshi <hitoshi@namaraii.com>

BEGIN { $defout.binmode }

$SAFE     = 0
$KCODE    = 'e'

$path  = File::dirname(__FILE__)

HIKI_VERSION  = '0.7-devel-20040215'

begin
  require 'cgi'
  require './hikiconf'
  require 'hiki/global'
  require 'hiki/command'
  require 'hiki/util'
  require "hiki/db/#{$database_type}"
  include Hiki::Util

  load_config

  cgi = CGI::new
  db = Hiki::HikiDB::new
  db.open_db {
    cmd = Hiki::Command::new( cgi, db )
    cmd.dispatch
  }
rescue Exception
  print "Content-Type: text/plain\n\n"
  puts "#$! (#{$!.class})\n\n"
  puts $@.join( "\n" )
end
