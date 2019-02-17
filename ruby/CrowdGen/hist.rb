require '../CrowdWorld/main'
require 'nokogiri'

include CrowdWorld
include Nokogiri

Dir.glob('Projects/SteerSuite/testcases/*', :base =>Dir.home)
pos = File.join(Dir.home, 'Projects/SteerSuite/testcases/hallway-four-way-2.xml')
file = File.read(pos)
xml = XML.parse file

c = xml.css('obstacle').to_a

a = c[1].dup
pp a.elements.map(&:text).map(&:to_f)

xml.css('orientedobstacle')
xml.elements.map(&:name)
pp xml.first.elements.map(&:name)
pp xml.first_element_child.elements.map(&:name)
pp xml.css("agentRegion")
pp xml.css("agentRegion").map(&:serialize)
