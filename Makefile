pytest:
	@pytest -s -v

pytest_report:
	@pytest --html=report.html

pytest_testrail:
	@py.test --testrail --tr-config=testrail.cfg --tr-close-on-complete

my_py:
	@mypy --no-strict-optional, --ignore-missing-imports, --disalllow-untyped-defs, --disallow-incomplete-defs,
      --pretty