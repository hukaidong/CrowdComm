module CrowdGen

  require 'pry'
  class XMLGenerator
    require '../CrowdWorld/main'
    require 'securerandom'
    include CrowdWorld

    attr_reader :xml

    def params(array)
      array.each do |attr|
        self.class.define_method(attr.sub(' ', '_')) do
          self.xml.at_css(attr).text.to_f
        end
      end
    end

    def self.group(gname, &block)
      self.define_method(gname) do |xml|
        @xml = xml
        instance_eval(&block)
      end
    end

    group :obstacle do

      params %w[xmin xmax ymin ymax zmin zmax]
      Creater.cube do |c|
        c.id = SecureRandom.random_bytes(4)
        c.config = :CREATE
        c.data = Creater.cube_data do |data|
          data.center = Vec3[
            (xmin + xmax) / 2,
            (ymin + ymax) / 2,
            (zmin + zmax) / 2
          ]

          data.scale = Vec3[
            xmax - xmin,
            ymax - ymin,
            zmax - zmin
          ]
          data.forward = Vec3.forward
        end
      end
    end

    group :targetLocation do 
      params %w[x y z]
      Vec3[x, y, z]
    end

    group :agentRegion do
      tempxml = xml
      tloc = targetLocation(xml.at_css("targetLocation"))
      @xml = tempxml
      params %w[numAgents xmin xmax ymin ymax zmin zmax]
      (1..numAgents).map do
        Creater.agent do |a|
          a.id = SecureRandom.random_bytes(4)
          a.config = :CREATE
          a.data << Creater.agent_data do |d|
            d.target = tloc
          end
          a.query << Creater.query do |q|
            q.name = "regionBounds"
            q.args.concat [xmin, xmax, ymin, ymax, zmin, zmax]
          end
        end
      end
    end

  end
end
