import os
from typing import Union

from pydantic_settings import BaseSettings, SettingsConfigDict

context = os.getenv("CONTEXT", "local")


class LocalConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.local")

    app: str
    device_name: str = "emulator-5554"
    platform_version: str = "12.0"
    platform_name: str = "Android"
    appium_url: str = "http://localhost:4723"


class BrowserStackConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.browserstack")

    user_name: str
    access_key: str
    app: str
    device: str = "Google Pixel 3"
    os_version: str = "9.0"
    project: str = "Wikipedia Mobile Tests"
    build: str = "Build 1"
    name: str = "Wikipedia tests"


config: Union[LocalConfig, BrowserStackConfig] = (
    LocalConfig() if context == "local" else BrowserStackConfig()
)
