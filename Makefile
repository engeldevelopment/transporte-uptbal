test:
	@python -m unittest discover -v

check_qc:
	@flake8

coverage:
	@coverage run -m unittest discover
	@coverage report

coverage_report:
	@coverage run -m unittest discover
	@coverage html