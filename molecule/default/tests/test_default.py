import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_foreman_running(host):
    assert host.service('postgresql').is_running
    assert host.service('postgresql').is_enabled
    assert host.service('httpd').is_enabled
    assert host.service('httpd').is_running


def test_foreman_org(host):
    cmd = host.run("hammer -u admin -p testpass1234 organization list | awk -F '|' '{print $3}'")  # noqa: E501
    assert 'test-org' in cmd.stdout
