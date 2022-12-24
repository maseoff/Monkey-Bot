from dataclasses import dataclass


@dataclass(frozen=True)
class TArticle(object):
    title: str | None
    text: str | None
    source: str | None
    path_to_image: str | None
