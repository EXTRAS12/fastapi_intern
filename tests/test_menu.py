DATA = {'title': 'test', 'description': 'test'}
UPDATE = {
    'title': 'update test',
    'description': 'update test',
}


def test_get_all_menus(client):
    response = client.get('/api/v1/menus')
    assert response.json() == []
    assert response.status_code == 200


def test_not_found_menu(client):
    response = client.get('/api/v1/menus/0')
    assert response.json() == {'detail': 'menu not found'}


def test_create_menu(client):
    response = client.post(
        '/api/v1/menus',
        json={
            'title': 'Menu 1',
            'description': 'Description 1',
        },
    )
    assert response.json() == {
        'id': '1',
        'title': 'Menu 1',
        'description': 'Description 1',
        'submenus_count': 0,
        'dishes_count': 0,
    }


def test_menu(client):
    response = client.get('/api/v1/menus/1')
    assert response.json() == {
        'id': '1',
        'title': 'Menu 1',
        'description': 'Description 1',
        'submenus_count': 0,
        'dishes_count': 0,
    }


def test_patch_menu(client):
    response = client.patch(
        '/api/v1/menus/1',
        json={'title': 'update', 'description': 'update'},
    )
    assert response.json() == {
        'id': '1',
        'title': 'update',
        'description': 'update',
        'submenus_count': 0,
        'dishes_count': 0,
    }


def test_delete_menu(client):
    response = client.delete('/api/v1/menus/1')
    assert response.json() == {
        'status': True,
        'message': 'The menu has been deleted',
    }


def test_patch_not_found_menu(client):
    response = client.patch(
        '/api/v1/menus/0',
        json={'title': 'update', 'description': 'updated menu'},
    )
    assert response.json() == {'detail': 'menu not found'}


def test2_delete_menu(client):
    response = client.delete('/api/v1/menus/0')
    assert response.json() == {'detail': 'menu not found'}


def test2_create_menu(client):
    response = client.post(
        '/api/v1/menus',
        json={
            'title': 'Menu 1',
            'description': 'Description 1',
        },
    )
    assert response.json() == {
        'id': '2',
        'title': 'Menu 1',
        'description': 'Description 1',
        'submenus_count': 0,
        'dishes_count': 0,
    }


def test_submenu_get(client):
    response = client.get('/api/v1/menus/2/submenus')
    assert response.json() == []


def test_submenu_post(client):
    response = client.post(
        '/api/v1/menus/2/submenus',
        json={
            'title': 'My submenu 1',
            'description': 'My submenu description 1',
        },
    )
    assert response.json() == {
        'id': '1',
        'title': 'My submenu 1',
        'description': 'My submenu description 1',
        'dishes_count': 0,
    }


def test_not_found_submenu(client):
    response = client.get('/api/v1/menus/2/submenus/2')
    assert response.status_code == 404
    assert response.json() == {'detail': 'submenu not found'}


def test_submenu_patch(client):
    response = client.patch(
        '/api/v1/menus/2/submenus/1',
        json={
            'title': 'My update submenu 1',
            'description': 'My update submenu description 1',
        },
    )
    assert response.json() == {
        'id': '1',
        'title': 'My update submenu 1',
        'description': 'My update submenu description 1',
        'dishes_count': 0,
    }


def test_del_submenu(client):
    response = client.delete('/api/v1/menus/2/submenus/1')
    assert response.json() == {
        'status': True,
        'message': 'The submenu has been deleted',
    }


def test_post_submenu1(client):
    response = client.post(
        '/api/v1/menus/2/submenus',
        json={
            'title': 'My submenu 2',
            'description': 'My submenu description 2',
        },
    )
    assert response.json() == {
        'id': '2',
        'title': 'My submenu 2',
        'description': 'My submenu description 2',
        'dishes_count': 0,
    }


def test_get_list_dishes(client):
    response = client.get('/api/v1/menus/2/submenus/2/dishes')
    assert response.json() == []


def test_post_dish(client):
    response = client.post(
        '/api/v1/menus/2/submenus/2/dishes',
        json={'title': 'dish 1', 'description': 'dish description 1', 'price': '5.5'},
    )
    assert response.json() == {
        'id': '1',
        'title': 'dish 1',
        'description': 'dish description 1',
        'price': '5.5',
    }


def test_patch_dish(client):
    response = client.patch(
        '/api/v1/menus/2/submenus/2/dishes/1',
        json={
            'title': 'update dish',
            'description': 'update dish description',
            'price': '10.5',
        },
    )
    assert response.json() == {
        'id': '1',
        'title': 'update dish',
        'description': 'update dish description',
        'price': '10.5',
    }


def test_get_one_dish(client):
    response = client.get('/api/v1/menus/2/submenus/2/dishes/1')
    assert response.json() == {
        'id': '1',
        'title': 'update dish',
        'description': 'update dish description',
        'price': '10.5',
    }


def test_delete_dish_not_found(client):
    response = client.get('/api/v1/menus/2/submenus/2/dishes/2')
    assert response.json() == {'detail': 'dish not found'}


def test_delete_menu2(client):
    response = client.delete('/api/v1/menus/2')
    assert response.json() == {
        'status': True,
        'message': 'The menu has been deleted',
    }
