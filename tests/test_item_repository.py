import pytest
from unittest.mock import Mock
from app.repositories.item_repository import create_item
from app.models.items import Item
from app.schemas.items_schemas import ItemCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

@pytest.fixture
def mock_db_session():
    return Mock(spec=Session)

@pytest.fixture
def item_data():
    return ItemCreate(name="Test Item", price=10.0)

@pytest.fixture
def mock_db_item(item_data):
    return Item(id=1, name=item_data.name, price=item_data.price)

def test_create_item_success(mock_db_session, item_data, mock_db_item, mocker):
    """
    Prueba la función create_item para asegurar que crea un nuevo ítem correctamente.
    """
    # Arrange
    db = mock_db_session
    db_item = mock_db_item

    # Configura mocks para los métodos necesarios
    db.add = mocker.Mock()
    db.commit = mocker.Mock()
    db.refresh = mocker.Mock()

    # Parchea la clase Item para que devuelva el mock db_item
    mocker.patch('app.repositories.item_repository.Item', return_value=db_item)

    # Act: llama a la función create_item
    result = create_item(db, item_data)

    # Assert: verifica las llamadas a los métodos del mock db
    db.add.assert_called_once_with(db_item)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(db_item)

    # Verifica que el ítem devuelto sea igual al mock db_item
    assert result == db_item

def test_create_item_database_failure(mock_db_session, item_data, mock_db_item, mocker):
    """
    Prueba la función create_item para asegurar que maneja los errores de la base de datos correctamente.
    """
    # Arrange
    db = mock_db_session
    db_item = mock_db_item

    # Configura mocks para lanzar excepciones al llamar a los métodos necesarios
    db.add = mocker.Mock(side_effect=SQLAlchemyError("Database connection failed"))
    db.commit = mocker.Mock(side_effect=SQLAlchemyError("Database commit failed"))
    db.refresh = mocker.Mock(side_effect=SQLAlchemyError("Database refresh failed"))

    # Parchea la clase Item para que devuelva el mock db_item
    mocker.patch('app.repositories.item_repository.Item', return_value=db_item)

    # Act: llama a la función create_item
    with pytest.raises(SQLAlchemyError):
        create_item(db, item_data)

    # Assert: verifica las llamadas a los métodos del mock db
    db.add.assert_called_once_with(db_item)
    db.commit.assert_not_called()  # No debería haber llegado a commit si falló add
    db.refresh.assert_not_called()  # No debería haber llegado a refresh si falló add