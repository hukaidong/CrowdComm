require 'CrowdComm/proto/utils_pb'
require 'CrowdComm/proto/elements_pb'

module CrowdWorld
  class Vec3
    attr_reader :proto

    def initialize(x, y, z)
      @proto = CrowdWorld::Proto::Vec3.new(x: x, y: y, z: z, hasValue: true)
    end

    class << self
      def [](x, y, z)
        CrowdWorld::Proto::Vec3.new(x: x, y: y, z: z, hasValue: true)
      end

      def up
        Vec3[0, 1, 0]
      end

      def forward
        Vec3[1, 0, 0]
      end

    end
  end

  class Creater
    keywords = %w[World Agent Cube Agent_Data Cube_Data Query]

    keywords.each do |keyword|
      class_eval <<-Method
        def self.#{keyword.downcase}
          pb = CrowdWorld::Proto::#{keyword}.new
          yield pb
          pb
        end
      Method
    end
  end
end

module CrowdComm
  require 'ffi-rzmq'

  module Utils

    def got_error(rc)
      unless ZMQ::Util.resultcode_ok?(rc)
        STDERR.puts "Operation failed, errno [#{ZMQ::Util.errno}] description [#{ZMQ::Util.error_string}]"
        caller(1).each { |callstack| STDERR.puts(callstack) }
        return true
      end
      false
    end

  end
end
