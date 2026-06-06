import os


CURSOR_API_URL = "https://api2.cursor.sh"
CURSOR_CLIENT_VERSION = os.getenv("CURSOR_CLIENT_VERSION", "cli-2026.01.09-231024f")
CURSOR_AGENT_RUN_PATH = "/agent.v1.AgentService/Run"
CURSOR_GET_USABLE_MODELS_PATH = "/agent.v1.AgentService/GetUsableModels"
CONNECT_END_STREAM_FLAG = 0b00000010
