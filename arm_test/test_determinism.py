import argparse
import datetime
import pdb

import ai2thor.controller
import ai2thor
import random
import copy
import time
from helper_mover import get_reachable_positions, execute_command, ADITIONAL_ARM_ARGS, get_current_full_state, two_dict_equal, ENV_ARGS, reset_the_scene_and_get_reachables

MAX_TESTS = 3000
MAX_EP_LEN = 100
scene_indices = [i + 1 for i in range(30)] +[i + 1 for i in range(200,230)] +[i + 1 for i in range(300,330)] +[i + 1 for i in range(400,430)]
scene_names = ['FloorPlan{}_physics'.format(i) for i in scene_indices]
set_of_actions = ['mm', 'rr', 'll', 'w', 'z', 'a', 's', 'u', 'j', '3', '4', 'p']


def extra_step(controller): # remove or add everywhere?
    # x = controller.step("AdvancePhysicsStep")
    return


def main(controller):
    all_timers = []

    for i in range(MAX_TESTS):
        reachable_positions = reset_the_scene_and_get_reachables(controller)
        all_command_details = []

        initial_location = random.choice(reachable_positions)
        initial_rotation = random.choice([i for i in range(0, 360, 45)])
        extra_step(controller)
        event1 = controller.step(action='TeleportFull', x=initial_location['x'], y=initial_location['y'], z=initial_location['z'], rotation=dict(x=0, y=initial_rotation, z=0), horizon=10, standing=True)
        initial_pose = dict(action='TeleportFull', x=initial_location['x'], y=initial_location['y'], z=initial_location['z'], rotation=dict(x=0, y=initial_rotation, z=0), horizon=10, standing=True)
        all_command_details.append(initial_pose)

        extra_step(controller)
        controller.step('PausePhysicsAutoSim')
        extra_step(controller)
        controller.step(action='MakeAllObjectsMoveable')
        all_command_details.append(dict(action='PausePhysicsAutoSim'))
        all_command_details.append(dict(action='MakeAllObjectsMoveable'))
        all_commands = []

        before = datetime.datetime.now()
        for j in range(MAX_EP_LEN):
            command = random.choice(set_of_actions)
            extra_step(controller)
            details = execute_command(controller, command, ADITIONAL_ARM_ARGS)
            all_commands.append(command)
            all_command_details.append(details)
            last_event_success = controller.last_event.metadata['lastActionSuccess']

            pickupable = controller.last_event.metadata['arm']['PickupableObjectsInsideHandSphere']
            picked_up_before = controller.last_event.metadata['arm']['HeldObjects']
            if len(pickupable) > 0 and len(picked_up_before) == 0:
                cmd = 'p'
                extra_step(controller)
                details = execute_command(controller, cmd, ADITIONAL_ARM_ARGS)
                all_command_details.append(details)
                all_commands.append(cmd)
                if controller.last_event.metadata['lastActionSuccess'] is False:
                    print('Failed to pick up ')
                    print('scene name', controller.last_event.metadata['sceneName'])
                    print('initial pose', initial_pose)
                    print('list of actions', all_commands)
                    break


        after = datetime.datetime.now()
        time_diff = after - before
        seconds = time_diff.total_seconds()
        all_timers.append(len(all_commands) / seconds)

        final_state = get_current_full_state(controller) # made sure this does not require deep copy
        print('FPS', sum(all_timers) / len(all_timers))


        # Redo the actions 20 times:
        # only do this if an object is picked up
        picked_up_before = controller.last_event.metadata['arm']['HeldObjects']
        if len(picked_up_before) > 0:
            for _ in range(10):
                reset_the_scene_and_get_reachables(controller, controller.last_event.metadata['sceneName'])
                extra_step(controller)
                event1 = controller.step(action='TeleportFull', x=initial_location['x'], y=initial_location['y'], z=initial_location['z'], rotation=dict(x=0, y=initial_rotation, z=0), horizon=10, standing=True)
                for cmd in all_commands:
                    extra_step(controller)
                    execute_command(controller, cmd, ADITIONAL_ARM_ARGS)
                    last_event_success = controller.last_event.metadata['lastActionSuccess']
                current_state = get_current_full_state(controller)
                if not two_dict_equal(final_state, current_state):
                    print('not deterministic')
                    print('scene name', controller.last_event.metadata['sceneName'])
                    print('initial pose', initial_pose)
                    print('list of actions', all_commands)
                    pdb.set_trace()
                    break


def parse_args():
    parser = argparse.ArgumentParser(
        description="allenact", formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--commit_id", type=str, default=None,
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.commit_id is not None:
        ENV_ARGS['commit_id'] = args.commit_id
        ENV_ARGS['scene'] = 'FloorPlan1_physics'
    controller = ai2thor.controller.Controller(
        **ENV_ARGS
    )
    print('controller build', controller._build.url)
    main(controller)

