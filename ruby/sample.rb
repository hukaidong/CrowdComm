require "CrowdComm/ByteClient"
require 'CrowdGen/crowdgen'
require 'CrowdWorld/main'
client = CrowdComm::ByteClient.new "tcp://localhost:6566"
world = CrowdGen.GenerateFromFile  "testcases/office-complex.xml";
client.send_bytes world.to_proto;
puts client.get_bytes
