from setuptools import setup, find_packages
setup(
    name = 'Automation-python-GB',
    version = '1.0',
    packages = find_packages(include = ('automationpythongb*', )) + ['prophecy_config_instances.automationpythongb'],
    package_dir = {'prophecy_config_instances.automationpythongb' : 'configs/resources/automationpythongb'},
    package_data = {'prophecy_config_instances.automationpythongb' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.49'],
    entry_points = {
'console_scripts' : [
'main = automationpythongb.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
