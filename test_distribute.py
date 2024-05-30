import pytest

from distribute import Worker, distribute


def a_worker(name, effort=1, coefficient=1):
    return Worker(name, effort, coefficient)


@pytest.mark.parametrize("budget, workers, expected", [
    (0, [], {}),
    (500, [a_worker("roger")], {"roger": 500}),
    (600, [a_worker("roger"), a_worker("jacques")], {"roger": 300, "jacques": 300}),
    (600, [a_worker("roger"), a_worker("berta")], {"roger": 300, "berta": 300}),
    (1200, [a_worker("roger", effort=2), a_worker("berta", effort=1)], {"roger": 800, "berta": 400}),
    (1200, [a_worker("roger", effort=4), a_worker("berta", effort=4)], {"roger": 600, "berta": 600}),
    (1200, [a_worker("roger", coefficient=14, effort=4), a_worker("berta", coefficient=7, effort=4)], {"roger": 800, "berta": 400}),
    (1200, [a_worker("roger", coefficient=4, effort=2), a_worker("berta", coefficient=2, effort=4)], {"roger": 600, "berta": 600}),
    (18000, [a_worker("roger", coefficient=750, effort=10), a_worker("berta", coefficient=800, effort=3), a_worker("jacques", coefficient=600, effort=7), a_worker("bertrand", coefficient=400, effort=10)], {"roger": 7458.563535911602, "berta": 2386.740331491713, "bertrand": 3977.9005524861877, "jacques": 4176.795580110497}),
])
def test_coeff(budget, workers, expected):
    assert distribute(budget, *workers) == expected
