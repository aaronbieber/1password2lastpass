# 'make install' to build and install the program.
# 'make clean' to destroy all the build artifacts.

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
