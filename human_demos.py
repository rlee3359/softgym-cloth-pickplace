import torch
import cv2
from softgym.registered_env import env_arg_dict, SOFTGYM_ENVS
from softgym.utils.normalized_env import normalize
import numpy as np
import copy

W = 200

def get_mask(img):
  grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  mask = np.zeros_like(grey)
  mask[grey < 160] = 255
  return mask

down = False
ix,iy = -1, -1
tipx,tipy = -1, -1
def mouse_callback(event, x,y,flags,param):
  global down, img, ix,iy,tipx,tipy
  if event == cv2.EVENT_LBUTTONDOWN:
    # print("CLICKED")
    down = True
    ix,iy = x,y
    tipx,tipy = x,y
  elif event == cv2.EVENT_MOUSEMOVE:
    # print("MOVED")
    if down:
      tipx,tipy = x,y
  elif event == cv2.EVENT_LBUTTONUP:
    # print("UP")
    down = False

def get_user_action(obs_img):
  cv2.namedWindow('Demo')
  cv2.setMouseCallback('Demo', mouse_callback)
  while not down:
    img = copy.deepcopy(obs_img)
    cv2.imshow("Demo", img)
    cv2.waitKey(10)

  while down:
    img = copy.deepcopy(obs_img)
    ovr = np.zeros_like(img)

    cv2.circle(img, (ix,iy),4,(0,100,0),1)
    img = img/255.0 + 0.2*ovr/255.0

    cv2.arrowedLine(img, (ix,iy), (tipx,tipy), (1,0,1), 2, tipLength=0.3)
    cv2.imshow("Demo", img)
    cv2.waitKey(10)

  pick = [ix, iy]
  place = [tipx, tipy]
  act = np.array([ix/W, iy/W, tipx/W, tipy/W])
  return act, pick, place

episode_num = 10
episode_length = 10
buf = []
name = "ClothPickPlace"
env_kwargs = env_arg_dict[name]
env_kwargs['headless'] = True
env_kwargs['camera_width'] = W
env_kwargs['camera_height'] = W
env_kwargs['num_variations'] = 1
env = SOFTGYM_ENVS[name](**env_kwargs)

for e in range(episode_num):
  obs = env.reset()[0]
  obs = obs[:,:,::-1]
  for t in range(episode_length):
    cv2.imshow("obs", obs)
    cv2.waitKey(1)
    action, pick, place = get_user_action(obs)
    nobs, _, done,_ = env.step(action)
    nobs = nobs[0]
    nobs = nobs[:,:,::-1]
    buf.append((obs,(pick, place),nobs))
    obs = nobs

    torch.save(buf, './data/human_dataset.pt')
