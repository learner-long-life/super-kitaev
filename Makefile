all: \
	test-narrow 				\
	test-compose-norecurse		\
	test-compose-recurse-helper	\
	test-compose-recurse		\
	test-encoded				\
	test-parallel-iterate		\
	test-parallel-add			\

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
	qcl adder/test-parallel-add.qcl
	