from app.models import Asset

assets: dict[str, Asset] = {}


def get_store() -> dict[str, Asset]:
    return assets
