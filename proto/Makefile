PROTOSOURCE = $(wildcard *.proto)
PROTORB = $(addprefix ruby/, \
	$(addsuffix _pb.rb, $(basename $(PROTOSOURCE)) ) )
PROTOCS = $(addprefix cs/, \
	$(addsuffix .cs, $(basename $(PROTOSOURCE)) ) )
PROTOPY = $(addprefix python/, \
	$(addsuffix .py, $(basename $(PROTOSOURCE)) ) )


$(PROTORB): $(PROTOSOURCE)
	-protoc $^ --ruby_out=ruby

$(PROTOCS): $(PROTOSOURCE)
	-protoc $^ --csharp_out=cs

$(PROTOPY): $(PROTOSOURCE)
	-protoc $^ --python_out=python

all: ruby cs python

ruby: $(PROTORB)

cs: $(PROTOCS)

python: $(PROTOPY)


clean: 
	@echo
	-rm $(PROTORB) $(PROTOCS) $(PROTOPY)

.PHONY:
	all clean ruby cs python
