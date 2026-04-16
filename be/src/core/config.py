# --------------------------------------------------------------------------- #
#  Core configuration – secrets & algorithm for JWT
# --------------------------------------------------------------------------- #

SECRET_KEY = "super-secret-key-change-me-in-production"   # TODO: move to env var
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
