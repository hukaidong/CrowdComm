$: << Dir.pwd
require 'pry'
require 'rake'
require 'nokogiri'
require 'CrowdComm/mdlgen'


Rake.application.init 

fvalid = FileList[eval(File.read("dumps").lines[-2..-1].join)['Valid xml']]

fvalid.each do |fsource|
  ftarget = fsource.gsub(/xmlcases/, 'proto').ext('.proto')
  ftarget_path = ftarget.pathmap('%d')

  task :default => ftarget
  directory ftarget_path
  file ftarget => [fsource, ftarget_path] do |t|
    xml = Nokogiri::XML.parse File.read fsource
    res = CrowdWorld::XMLReader.world xml
    File.open(ftarget, 'wb') do |f|
      f.write res.to_proto
    end
    rescue
  end
end


Rake.application.top_level
