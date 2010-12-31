QCL = qcl -c y

all: \
	test-narrow 				\
	test-compose-norecurse		\
	test-compose-recurse-helper	\
	test-compose-recurse		\
	test-encoded				\
	test-parallel-iterate		\
	test-parallel-add			\
	test-subtract				\
	test-subtract-encoded		\
	test-subtract-encoded-n2	\
	test-add-multiple			\
	test-copy-n2				\
	scratch-bit-dump			\

test-narrow:
	$(QCL) -b 37 adder/test-narrow.qcl

test-compose-norecurse:
	$(QCL) adder/test-compose-norecurse.qcl

test-compose-recurse-helper:
	$(QCL) adder/test-compose-recurse-helper.qcl

test-compose-recurse:
	$(QCL) adder/test-compose-recurse.qcl

test-encoded:
	$(QCL) adder/test-encoded.qcl

test-parallel-iterate:
	$(QCL) -b 43 adder/test-parallel-iterate.qcl

test-parallel-add:
	$(QCL) -b 43 adder/test-parallel-add.qcl

test-subtract:
	$(QCL) -b 43 adder/test-subtract.qcl

test-subtract-encoded:
	$(QCL) -b 109 adder/test-subtract-encoded.qcl

test-subtract-encoded-n2:
	$(QCL) -b 31 -f x adder/test-subtract-encoded-n2.qcl

test-add-multiple:
	$(QCL) -b 134 adder/test-add-multiple.qcl

test-copy-n2:
	$(QCL) -b 133 magic-state/test-copy-n2.qcl

scratch-bit-dump:
	$(QCL) -f x scratch/bit-dump.qcl
