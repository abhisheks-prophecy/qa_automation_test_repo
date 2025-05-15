from setuptools import setup, find_packages
setup(
    name = 'Automation_python_ReusableJobCluster_Pipeline',
    version = '1.0',
    packages = (
      find_packages(include = ('automation_python_reusablejobcluster_pipeline*', ))
      + ['prophecy_config_instances.automation_python_reusablejobcluster_pipeline']
    ),
    package_dir = {
      'prophecy_config_instances.automation_python_reusablejobcluster_pipeline': 'configs/resources/automation_python_reusablejobcluster_pipeline'
    },
    package_data = {'prophecy_config_instances.automation_python_reusablejobcluster_pipeline' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = automation_python_reusablejobcluster_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
