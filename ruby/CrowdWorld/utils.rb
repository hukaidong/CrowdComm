require 'utils_pb'
require 'elements_pb'

module CrowdWorld
  class Vec3
    attr_reader :proto

    def initialize(x, y, z)
      @proto = CrowdWorld::Proto::Vec3.new(x: x, y: y, z: z)
    end

    class << self
      def [](x, y, z)
        CrowdWorld::Proto::Vec3.new(x: x, y: y, z: z)
      end

      def up
        Vec3[0, 1, 0]
      end
    end
  end

  class Creater
    class << self
      keywords = %w[World Agent Cube Agent_Data Cube_Data]

      keywords.each do |keyword|
        class_eval <<-Method
          def #{keyword.downcase}
            pb = CrowdWorld::Proto::#{keyword}.new
            yield pb
            pb
          end
        Method
      end
    end
  end
end
