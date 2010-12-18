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
	qcl -b 37 adder/test-narrow.qcl

test-compose-norecurse:
	qcl adder/test-compose-norecurse.qcl

test-compose-recurse-helper:
	qcl adder/test-compose-recurse-helper.qcl

test-compose-recurse:
	qcl adder/test-compose-recurse.qcl

test-encoded:
	qcl adder/test-encoded.qcl

test-parallel-iterate:
	qcl -b 43 adder/test-parallel-iterate.qcl

test-parallel-add:
	qcl -b 43 adder/test-parallel-add.qcl

test-subtract:
	qcl -b 43 adder/test-subtract.qcl

test-subtract-encoded:
	qcl -b 109 adder/test-subtract-encoded.qcl

test-subtract-encoded-n2:
	qcl -b 31 -f x adder/test-subtract-encoded-n2.qcl

test-add-multiple:
	qcl -b 134 adder/test-add-multiple.qcl

test-copy-n2:
	qcl -b 133 magic-state/test-copy-n2.qcl

scratch-bit-dump:
	qcl -f x scratch/bit-dump.qcl
