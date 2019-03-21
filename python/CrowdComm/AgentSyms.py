#!/usr/bin/env python
# encoding: utf-8

# %load ~/upd.py
class AgentSyms:
    class data:
        class location:
            x = 'AGENTSYMS_DATA_LOCATION_X'
            y = 'AGENTSYMS_DATA_LOCATION_Y'
            z = 'AGENTSYMS_DATA_LOCATION_Z'
        class velocity:
            x = 'AGENTSYMS_DATA_VELOCITY_X'
            y = 'AGENTSYMS_DATA_VELOCITY_Y'
            z = 'AGENTSYMS_DATA_VELOCITY_Z'
        class forwards:
            x = 'AGENTSYMS_DATA_FORWARDS_X'
            y = 'AGENTSYMS_DATA_FORWARDS_Y'
            z = 'AGENTSYMS_DATA_FORWARDS_Z'
        class target:
            x = 'AGENTSYMS_DATA_TARGET_X'
            y = 'AGENTSYMS_DATA_TARGET_Y'
            z = 'AGENTSYMS_DATA_TARGET_Z'
    class queries:
        pass

_agent = CrowdComm.proto.Agent()
_value = _agent

_dget = {
        AgentSyms.data.location.x: (lambda :_agent.data.location.x),
        AgentSyms.data.location.y: (lambda :_agent.data.location.y),
        AgentSyms.data.location.z: (lambda :_agent.data.location.z),
        AgentSyms.data.velocity.x: (lambda :_agent.data.velocity.x),
        AgentSyms.data.velocity.y: (lambda :_agent.data.velocity.y),
        AgentSyms.data.velocity.z: (lambda :_agent.data.velocity.z),
        AgentSyms.data.forwards.x: (lambda :_agent.data.forwards.x),
        AgentSyms.data.forwards.y: (lambda :_agent.data.forwards.y),
        AgentSyms.data.forwards.z: (lambda :_agent.data.forwards.z),
        AgentSyms.data.target.x:   (lambda :_agent.data.target.x),
        AgentSyms.data.target.y:   (lambda :_agent.data.target.y),
        AgentSyms.data.target.z:   (lambda :_agent.data.target.z),
    }

_dset = {
        AgentSyms.data.location.x: lambda : exec('_agent.data.location.x = _value'),
        AgentSyms.data.location.y: lambda : exec('_agent.data.location.y = _value'),
        AgentSyms.data.location.z: lambda : exec('_agent.data.location.z = _value'),
        AgentSyms.data.velocity.x: lambda : exec('_agent.data.velocity.x = _value'),
        AgentSyms.data.velocity.y: lambda : exec('_agent.data.velocity.y = _value'),
        AgentSyms.data.velocity.z: lambda : exec('_agent.data.velocity.z = _value'),
        AgentSyms.data.forwards.x: lambda : exec('_agent.data.forwards.x = _value'),
        AgentSyms.data.forwards.y: lambda : exec('_agent.data.forwards.y = _value'),
        AgentSyms.data.forwards.z: lambda : exec('_agent.data.forwards.z = _value'),
        AgentSyms.data.target.x:   lambda : exec('_agent.data.target.x   = _value'),
        AgentSyms.data.target.y:   lambda : exec('_agent.data.target.y   = _value'),
        AgentSyms.data.target.z:   lambda : exec('_agent.data.target.z   = _value'),
    }
class AgentSymsDataUpdat:
    def updateData(proto):
        _agent.CopyFrom(proto)

    def Data():
        return _agent

    def getSyms(sym):
        return _dget[sym]()

    def setSyms(sym, val):
        global _value
        _value = val
        _dset[sym]()

    def debug():
        print([id(key) for key in _dset.keys()])


