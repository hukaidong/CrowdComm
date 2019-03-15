require "CrowdComm/ByteClient"
require 'CrowdGen/crowdgen'
require 'CrowdComm/main'
client = CrowdComm::ByteClient.new "tcp://localhost:6566"
world = CrowdGen.GenerateFromFile  "testcases/office-complex.xml";
client.send_bytes world.to_proto;
puts CrowdWorld::Proto::World.decode(client.get_bytes).to_json
