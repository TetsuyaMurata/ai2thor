from logging import disable
import os
import sys
root_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + "/..")
sys.path.insert(0, root_dir)
from arm_test.base import execute_actions, standard_pose
import arm_test.base

           # pp
           # inita
           # rr
           # mmlah 1 1
           # telefull
           # mmlah 0.5203709825292535 2 True
           # pac
           # mmla 0.01000303 -1.63912773e-06 0.558107364 2 armBase True
           # pac
           # mmlah 0.49074136446614885 2 True


actions = [{'action': 'RotateContinuous', 'degrees': 45, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'RotateContinuous', 'degrees': 45, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.7499999151111442, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.6999998531482053, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.6499998208148847, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.5999997218149233, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.5499996598519846, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.4999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.4999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.04999988079071, 'y': -2.98023224e-08, 'z': 0.3499999}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.09999971390000001, 'y': -2.98023224e-08, 'z': 0.3499997}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.14999955, 'y': -2.98023224e-08, 'z': 0.349999517}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.19999938, 'y': -2.98023224e-08, 'z': 0.349999338}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.249998975, 'y': -2.98023224e-08, 'z': 0.34999916}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.249998569, 'y': -2.98023224e-08, 'z': 0.399998981}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.249998212, 'y': -2.98023224e-08, 'z': 0.4499988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.4999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.299998212, 'y': -2.98023224e-08, 'z': 0.3999988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.299998212, 'y': -2.98023224e-08, 'z': 0.3999988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.299998212, 'y': -2.98023224e-08, 'z': 0.3999988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.249998212, 'y': -2.98023224e-08, 'z': 0.4499988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.5999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.5999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.299998212, 'y': -2.98023224e-08, 'z': 0.3999988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.199998212, 'y': -2.98023224e-08, 'z': 0.3999988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.249998212, 'y': -2.98023224e-08, 'z': 0.3499988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArm', 'position': {'x': 0.249998212, 'y': -2.98023224e-08, 'z': 0.4499988}, 'handCameraSpace': False, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.5999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}, {'action': 'MoveMidLevelArmHeight', 'y': 0.4999995904816413, 'disableRendering': True, 'restrictMovement': False, 'waitForFixedUpdate': False, 'returnToStart': True, 'speed': 1, 'move_constant': 0.05}]


standard_pose()
execute_actions(actions, disableRendering=True, returnToStart=True)
event = arm_test.base.controller.step('MoveMidLevelArmHeight', y=0.49074136446614885, disableRendering=True, returnToStart=True, speed=2.0)
assert event.metadata['lastActionSuccess'], "MoveMidLevelArmHeight failed; arm is stuck"
