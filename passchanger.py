#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to generate reset token and reset a user's password, for localhost using.
"""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jumpserver.settings')
  
    import django
    from users.models import User
    
    django.setup()
    username = input("Username to reset: ").strip()
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"User '{username}' not found Xp")
        sys.exit(1)

    # Generating token
    token = user.generate_reset_token()
    print(f"Token generated for {username}: {token}")
  
    new_password = input("New password: ").strip()
    
    try:
        user.reset_password(new_password)
        print("Password reset successfully!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
