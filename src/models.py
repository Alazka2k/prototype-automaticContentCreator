from pydantic import BaseModel

class Scene(BaseModel):
    description: str
    visual_prompt: str

class VideoScript(BaseModel):
    title: str
    description: str
    hashtags: str
    opening_scene: Scene
    scenes: list[Scene]
    closing_scene: Scene