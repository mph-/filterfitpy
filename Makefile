.PHONY: install
install:
	python3 setup.py install

.PHONY: package
package:
	python3 setup.py sdist bdist_wheel

.PHONY: upload-test
upload-test: package
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: upload
upload: package
	python3 -m twine upload dist/*

.PHONY: test
test: filterfitpy/*.py
	nosetests3 -s --pdb

.PHONY: cover
cover: filterfitpy/*.py
	nosetests3 --pdb --with-coverage --cover-package=filterfitpy --cover-html

.PHONY: doc-install
doc-install: doc
	scp -r doc/_build/html/* filterfitpy.elec.canterbury.ac.nz:/var/www/filterfitpy/

.PHONY: doc
release: doc push
	cd /tmp; rm -rf filterfitpy; git clone git@github.com:mph-/filterfitpy.git; cd filterfitpy; make test; make upload

.PHONY: release-test
release-test: doc push
	cd /tmp; rm -rf filterfitpy; git clone git@github.com:mph-/filterfitpy.git; cd filterfitpy; make test

.PHONY: style-check
style-check:
	flake8 filterfitpy
#	flake8 doc

.PHONY: flake8
flake8:
	flake8 filterfitpy
#	flake8 doc

.PHONY: check
check: style-check test

.PHONY: push
push: check
	git push
	git push --tags

.PHONY: doc
doc:
	cd doc; make html

.PHONY: clean
clean:
	-rm -rf build filterfitpy.egg-info dist
#	cd doc; make clean
