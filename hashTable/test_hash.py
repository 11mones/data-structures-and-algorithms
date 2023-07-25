from hash import HashTable


def test_set_and_get():
    hash_table = HashTable()
    hash_table.set('m', 11)
    assert hash_table.get('m') == 11

def test_set_and_has():
    hash_table = HashTable()
    hash_table.set('m', 11)
    assert hash_table.has('m') is True
    assert hash_table.has('not_exist') is False

def test_collision_handling():
    hash_table = HashTable()
    hash_table.set('d', 42)
    hash_table.set('g', 'value')
    assert hash_table.get('d') == 42
    assert hash_table.get('g') == 'value'


def test_update_value_for_key():
    hash_table = HashTable()
    hash_table.set('m', 42)
    hash_table.set('m', 'mones_new')
    assert hash_table.get('m') == 'mones_new'



def test_hash_method():
    hash = HashTable()
    actual = hash._HashTable__hash('m')
    assert 127 == actual



def test_no_existing_key():
    hash = HashTable()
    hash.set('1',"mones")
    assert hash.get('1') == "mones"
    assert hash.get("2") == None

def test_all():
    hash = HashTable()
    hash.set('m',"mones")
    hash.set('k',"khaled")
    hash.set('a',"ali")
    assert hash.keys == ['m' , 'k' , 'a']
    assert hash.keys != ['m' , 'k' ,' a']

