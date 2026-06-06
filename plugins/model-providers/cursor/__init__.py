from providers import register_provider
from providers.base import ProviderProfile

cursor = ProviderProfile(
    name="cursor",
    aliases=("cursor-agent", "cursor_subscription"),
    display_name="Cursor",
    description="Cursor subscription (Claude, GPT, Composer via Cursor Agent API)",
    api_mode="cursor_agent",
    env_vars=("CURSOR_ACCESS_TOKEN",),
    base_url="https://api2.cursor.sh",
    auth_type="oauth_external",
    fallback_models=(
        "claude-4.6-opus-high",
        "claude-4.5-sonnet",
        "gpt-5.4",
        "cursor-composer-2.5",
    ),
)
register_provider(cursor)
