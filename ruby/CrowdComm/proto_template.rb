require "securerandom"
require "CrowdComm/main"

module CrowdGen
  QA = CrowdWorld::Proto::QueryArgs

  def init_cube
    cd = CrowdWorld::Proto::Cube_Data.new.to_h

    CrowdWorld::Proto::Cube.new(
      id: SecureRandom.hex,
      config: :CREATE, 
      data: cd.update(cd) {|k, _| Hash.new }
    )
  end

  def init_agent
    ad = CrowdWorld::Proto::Agent_Data.new.to_h

    CrowdWorld::Proto::Agent.new(
      id: SecureRandom.hex,
      config: :CREATE, 
      data: ad.update(ad) {|k, _| Hash.new }
    )
  end

  def init_world
    CrowdWorld::Proto::World.new(
      id: SecureRandom.hex,
      config: :CREATE, 
    )
  end
end
