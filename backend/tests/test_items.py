def test_create_item(client):
    """Test creating a new item"""
    item_data = {
        "name": "Test Item",
        "description": "A test item description",
        "is_active": True
    }
    response = client.post("/api/v1/items", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert "id" in data


def test_read_items(client):
    """Test reading items list"""
    # Create a test item first
    item_data = {"name": "Test Item", "description": "Test"}
    client.post("/api/v1/items", json=item_data)
    
    # Read items
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_read_item(client):
    """Test reading a single item"""
    # Create a test item first
    item_data = {"name": "Test Item", "description": "Test"}
    create_response = client.post("/api/v1/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Read the item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]


def test_update_item(client):
    """Test updating an item"""
    # Create a test item first
    item_data = {"name": "Test Item", "description": "Test"}
    create_response = client.post("/api/v1/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Update the item
    update_data = {"name": "Updated Item"}
    response = client.put(f"/api/v1/items/{item_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]


def test_delete_item(client):
    """Test deleting an item"""
    # Create a test item first
    item_data = {"name": "Test Item", "description": "Test"}
    create_response = client.post("/api/v1/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    
    # Verify it's deleted
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 404


def test_read_nonexistent_item(client):
    """Test reading a non-existent item returns 404"""
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404
