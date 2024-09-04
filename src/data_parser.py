from dataclasses import dataclass
from typing import List

@dataclass
class Scene:
    description: str
    visual_prompt: str

@dataclass
class VideoScript:
    title: str
    description: str
    hashtags: str
    opening_scene: Scene
    scenes: List[Scene]
    closing_scene: Scene

def parse_response(response):
    # This function is no longer needed if the API is returning a structured object
    # Instead, we'll create a function to convert the API response to our VideoScript object
    return create_video_script(response)

def create_video_script(response_dict):
    opening_scene = Scene(
        description=response_dict.get('opening_scene', {}).get('description', ''),
        visual_prompt=response_dict.get('opening_scene', {}).get('visual_prompt', '')
    )
    
    scenes = [
        Scene(description=scene.get('description', ''), visual_prompt=scene.get('visual_prompt', ''))
        for scene in response_dict.get('scenes', [])
    ]
    
    closing_scene = Scene(
        description=response_dict.get('closing_scene', {}).get('description', ''),
        visual_prompt=response_dict.get('closing_scene', {}).get('visual_prompt', '')
    )

    return VideoScript(
        title=response_dict.get('title', ''),
        description=response_dict.get('description', ''),
        hashtags=response_dict.get('hashtags', ''),
        opening_scene=opening_scene,
        scenes=scenes,
        closing_scene=closing_scene
    )