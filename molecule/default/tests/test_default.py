import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_virtualenv_is_installed(host):
    assert host.pip_package.get_packages()['virtualenv']['version'] == '15.0.1'
