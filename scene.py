import subprocess
import yaml

def turn_off_scene(scene_entity):
  lights = [entity for entity in scene_entity['entities'] if entity.startswith('light.')]
  switches = [entity for entity in scene_entity['entities'] if entity.startswith('switch.')]

  for light_id in lights:
    light.turn_off(entity_id=light_id)

  for switch_id in switches:
    switch.turn_off(entity_id=switch_id)

@service
def toggle_scene(scene_name):
  scene_id = state.getattr(scene_name)['id']
  scenes = yaml.safe_load(subprocess.check_output(["cat", "scenes.yaml"]))
  scene_entity = [scene for scene in scenes if scene['id'] == scene_id][0]

  for entity_id in scene_entity['entities']:
    if state.get(entity_id) == 'on':
      turn_off_scene(scene_entity)
      return

  scene.turn_on(entity_id=scene_name)