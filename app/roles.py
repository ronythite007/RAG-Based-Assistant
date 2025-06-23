from .models import Role

def get_access_filter(role: Role):
    if role == Role.CEO:
        return None  # Full access
    access_map = {
        Role.FINANCE: {"department": "finance"},
        Role.MARKETING: {"department": "marketing"},
        Role.HR: {"department": "hr"},
        Role.ENGINEERING: {"department": "engineering"},
        Role.EMPLOYEE: {"access_level": "general"}
    }
    return access_map.get(role, {"access_level": "general"})
