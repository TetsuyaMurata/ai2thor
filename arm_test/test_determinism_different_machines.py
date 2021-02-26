import argparse
import datetime
import json
import pdb
import threading

import ai2thor.controller
import ai2thor
import random
import copy
import time

from helper_mover import get_reachable_positions, execute_command, ADITIONAL_ARM_ARGS, get_current_full_state, two_dict_equal, ENV_ARGS


scene_indices = [i + 1 for i in range(30)] +[i + 1 for i in range(200,230)] +[i + 1 for i in range(300,330)] +[i + 1 for i in range(400,430)]
scene_names = ['FloorPlan{}_physics'.format(i) for i in scene_indices]
set_of_actions = ['mm', 'rr', 'll', 'w', 'z', 'a', 's', 'u', 'j', '3', '4', 'p']



def parse_args():
    parser = argparse.ArgumentParser(description='Data loader')
    parser.add_argument('--generate_test', default=False, action='store_true')
    parser.add_argument('--number_of_test', default=20,type=int)
    parser.add_argument('--max_seq_len', default=100,type=int)
    parser.add_argument('--parallel_thread', default=1,type=int)
    parser.add_argument('--test_file_name', default='determinism_json.json',type=str)
    parser.add_argument(
        "--commit_id", type=str, default=None,
    )
    args = parser.parse_args()
    global MAX_TESTS
    MAX_TESTS = args.number_of_test
    global MAX_EP_LEN
    MAX_EP_LEN = args.max_seq_len
    return args

def reset_the_scene_and_get_reachables(controller, scene_name=None):
    if scene_name is None:
        scene_name = random.choice(scene_names)
    controller.reset(scene_name)
    return get_reachable_positions(controller)


def random_tests(controller):
    all_timers = []

    all_dict = {}

    for i in range(MAX_TESTS):
        print('test number', i)
        reachable_positions = reset_the_scene_and_get_reachables(controller)

        initial_location = random.choice(reachable_positions)
        initial_rotation = random.choice([i for i in range(0, 360, 45)])
        event1 = controller.step(action='TeleportFull', x=initial_location['x'], y=initial_location['y'], z=initial_location['z'], rotation=dict(x=0, y=initial_rotation, z=0), horizon=10, standing=True)
        initial_pose = dict(action='TeleportFull', x=initial_location['x'], y=initial_location['y'], z=initial_location['z'], rotation=dict(x=0, y=initial_rotation, z=0), horizon=10, standing=True)

        controller.step('PausePhysicsAutoSim')
        controller.step(action='MakeAllObjectsMoveable')
        all_commands = []
        before = datetime.datetime.now()
        for j in range(MAX_EP_LEN):
            command = random.choice(set_of_actions)
            execute_command(controller, command, ADITIONAL_ARM_ARGS)
            all_commands.append(command)
            last_event_success = controller.last_event.metadata['lastActionSuccess']

            pickupable = controller.last_event.metadata['arm']['PickupableObjectsInsideHandSphere']
            picked_up_before = controller.last_event.metadata['arm']['HeldObjects']
            if len(pickupable) > 0 and len(picked_up_before) == 0:
                cmd = 'p'
                execute_command(controller, cmd, ADITIONAL_ARM_ARGS)
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
        scene_name = controller.last_event.metadata['sceneName']

        #TODO only when pick up has happened
        dict_to_add = ({'initial_location': initial_location,
               'initial_rotation': initial_rotation,
               'all_commands': all_commands,
               'final_state': final_state,
               'initial_pose': initial_pose,
               'scene_name': scene_name
               })
        all_dict[len(all_dict)] = dict_to_add
        # print('FPS', sum(all_timers) / len(all_timers))
    return all_dict
def determinism_test(controller, all_tests):
    # Redo the actions 20 times:
    # only do this if an object is picked up
    for k, test_point in all_tests.items():
        initial_location = test_point['initial_location']
        initial_rotation = test_point['initial_rotation']
        all_commands = test_point['all_commands']
        final_state = test_point['final_state']
        initial_pose = test_point['initial_pose']
        scene_name = test_point['scene_name']
        all_action_details = []
        all_action_success = []

        controller.reset(scene_name)
        teleport_action = dict(action='TeleportFull', x=initial_location['x'], y=initial_location['y'], z=initial_location['z'], rotation=dict(x=0, y=initial_rotation, z=0), horizon=10, standing=True)
        event1 = controller.step(**teleport_action)
        all_action_details.append(teleport_action)
        all_action_success.append(event1.metadata['lastActionSuccess'])
        pause_physics = dict(action='PausePhysicsAutoSim')
        event = controller.step(**pause_physics)
        all_action_success.append(event.metadata['lastActionSuccess'])
        all_action_details.append(pause_physics)
        for cmd in all_commands:
            action_detail = execute_command(controller, cmd, ADITIONAL_ARM_ARGS)
            all_action_details.append(action_detail)
            last_event_success = controller.last_event.metadata['lastActionSuccess']
            all_action_success.append(last_event_success)
        current_state = get_current_full_state(controller)
        if (not two_dict_equal(final_state, current_state)):
            print('not deterministic')
            print('scene name', controller.last_event.metadata['sceneName'])
            print('initial pose', initial_pose)
            print('list of actions', all_commands)
            pdb.set_trace()
        else:
            print('test {} passed'.format(k))

def test_generator(controller, args):
    all_dict = random_tests(controller)
    with open(args.test_file_name ,'w') as f:
        json.dump(all_dict, f)

def test_from_file(controller, args):
    with open(args.test_file_name ,'r') as f:
        all_dict = json.load(f)
    determinism_test(controller, all_dict)


if __name__ == '__main__':
    args = parse_args()
    if args.commit_id is not None:
        ENV_ARGS['commit_id'] = args.commit_id
        ENV_ARGS['scene'] = 'FloorPlan1_physics'

    if args.generate_test:

        controller = ai2thor.controller.Controller(**ENV_ARGS)
        print('controller build', controller._build.url)
        test_generator(controller, args)
    else:
        threads = []
        for i in range(args.parallel_thread):
            controller = ai2thor.controller.Controller(**ENV_ARGS)
            print('controller build', controller._build.url)
            x = threading.Thread(target=test_from_file, args=(controller,args,))
            threads.append(x)
            x.start()
        for index, thread in enumerate(threads):
            print("Main    : before joining thread %d.", index)
            thread.join()
            print("Main    : thread %d done", index)



