from typing import List, Optional
from datetime import datetime
from app.models.user import User, UserCreate, UserUpdate

class UserService:
    """Service layer for user operations"""
    
    # Mock database - in real app, this would be a database
    _users = []
    _next_id = 1
    
    @classmethod
    def get_all_users(cls) -> List[User]:
        """Get all users"""
        return cls._users
    
    @classmethod
    def get_user_by_id(cls, user_id: int) -> Optional[User]:
        """Get user by ID"""
        for user in cls._users:
            if user.id == user_id:
                return user
        return None
    
    @classmethod
    def create_user(cls, user_data: UserCreate) -> User:
        """Create a new user"""
        user = User(
            id=cls._next_id,
            email=user_data.email,
            full_name=user_data.full_name,
            is_active=user_data.is_active,
            created_at=datetime.now()
        )
        cls._users.append(user)
        cls._next_id += 1
        return user
    
    @classmethod
    def update_user(cls, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update user"""
        user = cls.get_user_by_id(user_id)
        if not user:
            return None
        
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.full_name is not None:
            user.full_name = user_data.full_name
        if user_data.is_active is not None:
            user.is_active = user_data.is_active
        
        user.updated_at = datetime.now()
        return user
    
    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        """Delete user"""
        user = cls.get_user_by_id(user_id)
        if user:
            cls._users.remove(user)
            return True
        return False 