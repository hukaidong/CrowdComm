PROTOSOURCE = $(wildcard *.proto)
PROTORB = $(addprefix ruby/, \
	$(addsuffix _pb.rb, $(basename $(PROTOSOURCE)) ) )
PROTOCS = $(addprefix cs/, \
	$(addsuffix .cs, $(basename $(PROTOSOURCE)) ) )


$(PROTORB): $(PROTOSOURCE)
	-protoc $^ --ruby_out=ruby

ruby: $(PROTORB)
cs: $(PROTOCS)

all:


clean: 
	@echo
	-rm $(PROTORB)

.PHONY:
	all clean ruby cs
