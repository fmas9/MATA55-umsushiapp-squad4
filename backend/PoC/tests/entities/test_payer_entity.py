import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError
from domain.entities.locale import Locale
from domain.entities.user.payer import Payer


def test_create_valid_payer():
    payer = Payer(
        id=uuid4(),
        name="John Doe",
        email="john@example.com",
        password="securepassword",
        phone_number="+1234567890",
        code="USR123",
        locale=Locale(city="New York", country="US"),
        description="Test payer",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    assert payer.name == "John Doe"
    assert payer.is_active is True
    assert payer.description == "Test payer"


def test_payer_optional_description():
    payer = Payer(
        id=uuid4(),
        name="Jane Smith",
        email="jane@example.com",
        password="password123",
        phone_number="+1987654321",
        code="USR456",
        locale=Locale(city="Los Angeles", country="US"),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    assert payer.description is None


def test_invalid_uuid_raises_validation_error():
    with pytest.raises(ValidationError):
        Payer(
            id="not-a-uuid",
            name="Invalid UUID",
            email="invalid@example.com",
            password="pass",
            phone_number="0000000000",
            code="ERR001",
            locale=Locale(city="Nowhere", country="XX"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_missing_required_field_raises_validation_error():
    with pytest.raises(ValidationError):
        Payer(
            id=uuid4(),
            # name is missing
            email="missing@example.com",
            password="abc",
            phone_number="123",
            code="MISSING",
            locale=Locale(city="Missing City", country="MS"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
