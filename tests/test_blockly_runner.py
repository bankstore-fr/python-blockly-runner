import glob
import json
import os

import pytest

from blockly_runner import execute_workspace, execute_workspace_merge_all_roots


def _generate_test_case():
    files = glob.glob("./tests/sample_workspaces/*.json")
    test_workspaces = []
    for file in files:
        with open(file, "r") as f:
            data = json.load(f)

        for env, expected_result in zip(data["envs"], data["expected_results"]):
            test_workspaces.append(
                pytest.param(
                    data["workspace"],
                    env,
                    expected_result,
                    id=f"{os.path.basename(file)}-{env}",
                )
            )

    return test_workspaces


@pytest.mark.parametrize("workspace, env, expected_result", _generate_test_case())
def test_execute_workspace_merge_all_roots(workspace, env, expected_result):
    result = execute_workspace_merge_all_roots(workspace, env)

    assert result == expected_result


def test_execute_workspace():
    with open("./tests/sample_workspaces/multiple_root_blocks.json", "r") as f:
        data = json.load(f)
        workspace = data["workspace"]
        env = data["envs"][0]

    result = execute_workspace(workspace, env)

    assert result == [{"my_var": -50}, {"my_var": -25}]
