pytest:
	@pytest -s -v

report:
	@pytest --html=report.html

testrail:
	@py.test --testrail --tr-config=testrail.cfg --tr-close-on-complete

my_py:
	@mypy --no-strict-optional --ignore-missing-imports --disalllow-untyped-defs --disallow-incomplete-defs --pretty

allure:
	@pytest --alluredir=C:\mari1\attestation\allure

safari:
	@pytest --driver Safari