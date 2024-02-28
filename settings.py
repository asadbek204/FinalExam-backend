import os
from dotenv import load_dotenv

load_dotenv()

avatars_path = os.getenv('AVATARS_PATH')
videos_path = os.getenv('VIDEOS_PATH')
photos_path = os.getenv('PHOTOS_PATH')
audios_path = os.getenv('AUDIOS_PATH')
stories_path = os.getenv('STORIES_PATH')
moments_path = os.getenv('MOMENTS_PATH')


class ServerSettings:
    def __init__(
            self,
            protocol: str | None = None,
            domain: str | None = None,
            port: int | None = None
    ) -> None:
        self.protocol = protocol or os.getenv("PROTOCOL", "http") + "://"
        self.domain: str = domain or os.getenv('DOMAIN_NAME')
        self.port: int = port or int(os.getenv('PORT'))

    @property
    def url(self) -> str:
        return f'{self.protocol}://{self.domain}:{self}'


class AuthSettings:
    def __init__(self, secret_key: str | None = None) -> None:
        self.secret_key: str = secret_key or os.getenv('SECRET_KEY')


class DatabaseSettings:
    def __init__(self, url: str | None = None) -> None:
        self.url: str = url or os.getenv('DATABASE_URL')


class SubDirsSettings:

    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        self.avatars: str = self.make_path(avatars_path)
        self.videos: str = self.make_path(videos_path)
        self.photos: str = self.make_path(photos_path)
        self.audios: str = self.make_path(audios_path)
        self.stories: str = self.make_path(stories_path)
        self.moments: str = self.make_path(moments_path)

    def make_path(self, sub_dir: str) -> str:
        return os.path.join(self.base_dir, sub_dir)


class MediaPathSettings:
    def __init__(
            self,
            media_base: str | None = None,
            chat: str | None = None,
            channel: str | None = None
    ) -> None:
        self.media_base_path: str = media_base or os.getenv('MEDIA_BASE_PATH')
        self.chat: SubDirsSettings = chat or SubDirsSettings(os.getenv('CHAT_MEDIA_BASE_PATH'))
        self.channel: SubDirsSettings = channel or SubDirsSettings(os.getenv('CHANNEL_MEDIA_BASE_PATH'))


class Settings:
    def __init__(
            self,
            server: ServerSettings | None = None,
            auth: AuthSettings | None = None,
            database: DatabaseSettings | None = None,
            media_path: MediaPathSettings | None = None
    ) -> None:
        self.server: ServerSettings = server or ServerSettings()
        self.auth: AuthSettings = auth or AuthSettings()
        self.database: DatabaseSettings = database or DatabaseSettings()
        self.media_path: MediaPathSettings = media_path or MediaPathSettings()


settings = Settings()
