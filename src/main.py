"""
Authentication Service Module (update-code branch)
"""
from typing import Dict, Any, Optional

class UserAuthenticator:
    def authenticate_user(self, username: str, auth_token: str, tenant_id: str = "default") -> bool:
        """
        BREAKING CHANGE 1: Introduced a mandatory position 2 positional parameter `auth_token`
        without a default value. This breaks all existing positional calls `authenticate_user(username)`.
        """
        if not username or not auth_token:
            return False
        return True

    def get_user_permissions(self, user_profile: Optional[Dict[str, Any]]) -> list:
        """
        BREAKING CHANGE 2: Removed the null/None guard check on `user_profile`.
        If `user_profile` is None, this now throws a runtime `TypeError: 'NoneType' object is not subscriptable`.
        """
        # Guard removed! Null reference exception risk.
        return user_profile["roles"]