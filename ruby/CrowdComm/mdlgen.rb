require 'CrowdComm/proto_template'

module CrowdGen
  SBTC = 'SteerBenchTestCase'

  def cube(xml)
    cb = init_cube

    xmin = xml.at('xmin').content.to_f
    xmax = xml.at('xmax').content.to_f
    ymin = xml.at('ymin').content.to_f
    ymax = xml.at('ymax').content.to_f
    zmin = xml.at('zmin').content.to_f
    zmax = xml.at('zmax').content.to_f

    cb.data.center.x = (xmin+xmax)/2
    cb.data.center.y = (ymin+ymax)/2
    cb.data.center.z = (zmin+zmax)/2
    cb.data.center.hasValue = true

    cb.data.scale.x = xmax - xmin
    cb.data.scale.y = ymax - ymin
    cb.data.scale.z = zmax - zmin
    cb.data.scale.hasValue = true

    cb.data.forward.x = 1.0
    cb.data.forward.y = 0.0
    cb.data.forward.z = 0.0
    cb.data.forward.hasValue = true

    return cb
  end

  def agent(xml)
    ag = init_agent

    name = xml.at('name').content

    posx = xml.at('initialConditions position x').content.to_f
    posy = xml.at('initialConditions position y').content.to_f
    posz = xml.at('initialConditions position z').content.to_f

    fwdx = xml.at('initialConditions direction x').content.to_f
    fwdy = xml.at('initialConditions direction y').content.to_f
    fwdz = xml.at('initialConditions direction z').content.to_f

    targetLoc = xml.at('goalSequence seekStaticTarget targetLocation')
    goalx = targetLoc.at('x').content.to_f
    goaly = targetLoc.at('y').content.to_f
    goalz = targetLoc.at('z').content.to_f

    ag.nickname = name or ""

    ag.data.location.x = posx
    ag.data.location.y = posy
    ag.data.location.z = posz
    ag.data.location.hasValue = true

    ag.data.velocity = nil

    ag.data.forwards.x = fwdx
    ag.data.forwards.y = fwdy
    ag.data.forwards.z = fwdz
    ag.data.forwards.hasValue = true

    ag.data.target.x = goalx
    ag.data.target.y = goaly
    ag.data.target.z = goalz
    ag.data.target.hasValue = true

    return ag
  end

  def agentregion(xml)
    begin
      num = xml.at('numAgents').content.to_i
      regargs = xml.at('regionBounds').elements.map do |elem|
        elem.content.to_f
      end

      unless xml.at('initialConditions direction x').nil?
        fwd_hasvalue = true
        fwdx = xml.at('initialConditions direction x').content.to_f
        fwdy = xml.at('initialConditions direction y').content.to_f
        fwdz = xml.at('initialConditions direction z').content.to_f
      end

      targetLoc = xml.at('goalSequence seekStaticTarget targetLocation')
      if targetLoc.nil?
        return []
      end

      goalx = targetLoc.at('x').content.to_f
      goaly = targetLoc.at('y').content.to_f
      goalz = targetLoc.at('z').content.to_f

      num.times.map do 
        ag = init_agent

        ag.data.location = nil
        ag.data.velocity = nil

        if fwd_hasvalue
          ag.data.forwards.x = fwdx
          ag.data.forwards.y = fwdy
          ag.data.forwards.z = fwdz
          ag.data.forwards.hasValue = true
        else
          ag.data.forwards = nil
        end

        ag.data.target.x = goalx
        ag.data.target.y = goaly
        ag.data.target.z = goalz
        ag.data.target.hasValue = true

        rb = CrowdWorld::Proto::QueryArgs.new
        rb.args.concat(regargs)
        ag.queries['agentRegion.regionBounds'] = rb

        ag
      end
    rescue Exception => e
      puts "Error: Failed to parse following element"
      puts xml.to_html(indent: 0)
      raise e
    end
  end

  def world(xml)
    wd = init_world
    xml.css("#{SBTC} agent").each { |elem| wd.agents.push agent elem }
    xml.css("#{SBTC} agentRegion").each { |elem| wd.agents.concat agentregion elem }
    xml.css("#{SBTC} obstacle").each { |elem| wd.cubes.push cube elem }
    wd
  end

end

module CrowdWorld
  class XMLReader
    extend CrowdGen
  end
end
