def test_command(host):
    assert host.command('couchdb_cluster --version').rc == 0
