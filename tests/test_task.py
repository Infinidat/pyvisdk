import unittest, types
from pyvisdk import Vim
from tests.common import get_options
from pyvisdk.facade.task import TaskManager

def nothing():
    pass

def random_string(n):
    import random
    import string
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(n))

TASKS = ['hello world',
         'I hate VMware',
         'me too',
         'This is a very long task name, a very very long name',
         'school sucks',
         'one more',
         'last one']

class Test_Task(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)
        cls.manager = TaskManager(cls.vim)
        cls.obj = cls.vim.getHostSystems()[0]
        cls.cleanUpStaleTasks()

    @classmethod
    def cleanUpStaleTasks(cls):
        for task in cls.manager._managed_object.recentTask:
            if task.info.state in ['running', 'queued']:
                task.SetTaskState('error', None, None)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def test_task(self):
        with self.manager.task(self.obj, TASKS[0]):
            pass

    def test_task__error(self):
        with self.assertRaises(Exception):
            with self.manager.task(self.obj, TASKS[1]):
                raise Exception()

    def test_wrap(self):
        task = self.manager.task(self.obj, TASKS[2])
        func = task.wraps(nothing)
        func()

    def test_step(self):
        task = self.manager.task(self.obj, TASKS[3])
        task.step([nothing, nothing, nothing])

    def test_step_manually(self):
        with self.manager.task(self.obj, TASKS[4]) as task:
            task.update_progress(10)
            task.update_progress(20)
            task.update_progress(90)
            
class Test_TaskWait(Test_Task):
    def test_waitForTask_ref(self):
        dummy_task = self.manager.task(self.obj, TASKS[5])
        task = dummy_task._managed_object
        task.SetTaskState("success")
        self.assertEquals(task.core.waitForTask(task.ref), 'success')
    
    def test_waitForTask_regular(self):
        dummy_task = self.manager.task(self.obj, TASKS[5])
        task = dummy_task._managed_object
        task.SetTaskState("success")
        self.assertEquals(task.core.waitForTask(task), 'success')
        
    def test_waitForTask_fail(self):
        from pyvisdk.exceptions import VisdkTaskError
        dummy_task = self.manager.task(self.obj, TASKS[5])
        task = dummy_task._managed_object
        task.SetTaskState("error", None, None)
        with self.assertRaises(VisdkTaskError):
            task.core.waitForTask(task)
    
    def _change_task(self, task, new_state):
        task.SetTaskState(new_state, None, None)
    
    def _waitForTask_timeout(self, is_running, wait_timeout, how_long=5):
        from pyvisdk.exceptions import VisdkTaskError
        import threading
        dummy_task = self.manager.task(self.obj, TASKS[5])
        task = dummy_task._managed_object
        if is_running:
            task.SetTaskState("running", None, None)
        timer = threading.Timer(how_long, self._change_task, args=[task, "success"])
        timer.start()
        if wait_timeout is not None and how_long > wait_timeout:
            with self.assertRaises(VisdkTaskError):
                task.core.waitForTask(task, wait_timeout)
        else:
            self.assertEquals(task.core.waitForTask(task, wait_timeout), 'success')
        timer.join()
            
    def test_waitForTask_timeout_running_infinite_wait(self):
        self._waitForTask_timeout(True, None)
    def test_waitForTask_timeout_queued_infinite_wait(self):
        self._waitForTask_timeout(False, None)
    def test_waitForTask_timeout_running_long_wait(self):
        self._waitForTask_timeout(True, 10)
    def test_waitForTask_timeout_queued_long_wait(self):
        self._waitForTask_timeout(False, 10)
    def test_waitForTask_timeout_running_short_wait(self):
        self._waitForTask_timeout(True, 1)
    def test_waitForTask_timeout_queued_short_wait(self):
        self._waitForTask_timeout(False, 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()

