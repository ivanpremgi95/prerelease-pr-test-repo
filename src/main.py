"""
Authentication Service Module (main branch)
"""
from typing import Dict, Any, Optional

class UserAuthenticator:
    def authenticate_user(self, username: str, tenant_id: str = "default") -> bool:
        """
        Authenticates user with optional tenant_id.
        """
        if not username:
            return False
        return True

    def get_user_permissions(self, user_profile: Optional[Dict[str, Any]]) -> list:
        """
        Extracts user roles safely with guard checks.
        """
        if user_profile is None or "roles" not in user_profile:
            return []
        return user_profile.get("roles", [])