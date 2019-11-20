import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_minio_user(host):
    u = host.user('minio')
    assert u.name == 'minio'
    assert u.group == 'minio'


def test_minio_data_directory(host):
    d = host.file("/var/lib/minio")
    assert d.exists
    assert d.is_directory
    assert d.user == 'minio'
    assert d.group == 'minio'


def test_minio_service(host):
    s = host.service('minio')
    assert s.is_running
