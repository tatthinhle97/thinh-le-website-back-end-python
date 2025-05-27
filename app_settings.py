from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Thinh Le\'s website'
    admin_email: str = 'letatthinh.1997@gmail.com'

    model_config = SettingsConfigDict(
        env_file='.env',
        # https://docs.pydantic.dev/latest/api/config/#pydantic.config.ExtraValues
        extra='allow')