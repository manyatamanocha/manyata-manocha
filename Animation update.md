# Peek-and-wave update

The cartoon now uses two generated transparent layers, `img/peek-body-v2.png` and `img/peek-arm-v2.png`. Original images are retained. `sky_theme.py` places the arm over the stationary body and inlines `peek-animation.js`.

Sequence: after both images decode, enter from the right over 700 ms, animate the arm for 2200 ms, then rest. Clicking replays only the hand wave. The stationary hero controls visibility, avoiding the prior bug where observing the translated-offscreen mascot could cancel its own entrance. Hidden/offscreen animation pauses and resumes. Reduced motion displays the resting image.

Run `node tests/peek-animation.test.cjs`. Covers automatic startup, arm-only wave, resting/replay, repeated clicks, hidden-tab startup, offscreen pause/resume, reduced motion and image failure. These are controller tests, not browser rendering tests.

Build: `python3 build_web.py && python3 make_site.py`.

Visual validation is still required at desktop and mobile sizes. No browser connection was available. In particular inspect the elbow alignment and the arm's fade into the resting pose. Do not describe visual quality as verified.

Assets were edited with the built-in image generation tool, using `img/peek-clean.png` as the reference. Body prompt: preserve face, hair, body, composition and right-edge gripping hand; remove only the raised palm/arm and fill hair/shirt behind it; transparent background. Arm prompt: isolate the waving palm and bent forearm on transparency, preserve style and skin color, remove everything else. The generated arm used a different scale, compensated in CSS with width/height 70%, left 14.5%, top 21.5%; visual validation remains necessary.
