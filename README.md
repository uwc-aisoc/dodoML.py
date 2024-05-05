Seems like we’re doing Ice Dodo.

Ice Dodo has a clear structure in terms of model structure

input: the graphics in front of the player

- This is made easier by the fact that most levels are high contrast. This can be converted into 3-class input matrices (track, obstacle, void) and that should simplify the process enough for reinforcement learning to happen ok
  - Need to find levels that are distinct color palette                          
  - Use Low res version of ice dodo
  - How to map onto bitmap.
  - Variable FOV might be an issue
    - But it only happens between levels, not in them.
  - Converted using OBS filter???
    - OBS python addons for customisability
  - Then map single colors onto bitmap.
  - Use a library like [MoviePy](https://medium.com/@kapildevkhatik2/advanced-image-and-video-processing-techniques-using-python-549fb1cf224e)
    - Or openCV?
    - Color mapping: [Change the colors within certain range to another color using OpenCV - Stack Overflow](https://stackoverflow.com/questions/50210304/change-the-colors-within-certain-range-to-another-color-using-opencv)

output: controls, arrows

- Juwon concerned about ‘wrapping’ but honestly why can’t we just have artificial keyboard input controlling the game

Model should be rewarded by time survived. If they finish the level, then some high-ass reward.

- Juwon concerned about manipulating the system by just going around in circles to survive
  - Solution may be in capping runtime/model at 5mins (and then giving 0 reward). Also, we can cherry-pick levels

Speaking of cherry-picking levels

- We are confident that this structure will work with 2d/flat levels
  - Juwon: However with 3d levels, might be different
    - Chris thinks that we can just train on 3d levels anyways… we’re in it to see if it works or not

Therefore if we are to pursue this, the following questions need to be answered:

- How do we take the area in front of the player as input?
  - Screen record specific area?
- How to classify colors and map them into track/obstacle/void?
  -  By mapping ranges of colors onto them?
- How on God’s earth do we make a reinforcement learning model anyways? Chris hasn’t done this before… ever.
- Model might work well on a single level but Chris doubts that it can work across levels
- How on earth do we get thru generations quickly enough??
  - Can Ice dodo be slowed down?
  - Each model may take minutes before reward is decided(!!)
    - Therefore going thru a generation of models will take hours, days 😬
    - Don edited this
    - Adi edited this :)
    - Rupert edited this
