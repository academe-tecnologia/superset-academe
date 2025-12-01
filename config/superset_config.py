import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True,
}

TALISMAN_ENABLED = False

SECRET_KEY = os.environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE")

SESSION_COOKIE_SAMESITE = "None"
ENABLE_PROXY_FIX = True
PUBLIC_ROLE_LIKE_GAMMA = True
SESSION_COOKIE_SECURE = True
CSRF_ENABLED = False
WTF_CSRF_ENABLED = False
GUEST_ROLE_NAME = "Gamma"
GUEST_TOKEN_JWT_SECRET = "test-guest-secret-change-me"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 300

CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}
