from softgym.envs.cloth_pick_place import ClothPickPlace

from collections import OrderedDict

env_arg_dict = {
    'ClothPickPlace': {'observation_mode': 'cam_rgb',
                          'action_mode': 'picker_qpg',
                          'num_picker': 1,
                          'render': True,
                          'headless': False,
                          'horizon': 10,
                          'action_repeat': 1,
                          'render_mode': 'cloth',
                          'num_variations': 1,
                          'use_cached_states': False,
                          'save_cached_states': False,
                          'deterministic': False},
}

SOFTGYM_ENVS = OrderedDict({
    'ClothPickPlace': ClothPickPlace,
})
