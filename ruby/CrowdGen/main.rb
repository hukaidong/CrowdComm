require 'base64'
require 'securerandom'
require 'nokogiri'
require './gen'
require '../CrowdWorld/main'

include Nokogiri

dirs = Dir.glob('Projects/SteerSuite/testcases/*', :base =>Dir.home)
pos = File.join(Dir.home, 'Projects/SteerSuite/testcases/basic-office.xml')
file = File.read(pos)
SAMPLEXML = XML.parse file

gen = CrowdGen::XMLGenerator.new
world = CrowdWorld::Creater.world do |w|
  w.id = SecureRandom.random_bytes(4)
  w.config = :CREATE
  SAMPLEXML.css(:obstacle).each do |xml|
    w.cubes << gen.obstacle(xml)
  end

  SAMPLEXML.css(:agentRegion).each do |xml|
    w.agents.concat gen.agentRegion(xml)
  end
end

proto = world.to_proto
puts Base64.encode64(proto)
