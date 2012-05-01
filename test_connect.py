#!python

from connect import Connect
#from mock import Mock, patch

class TestConnect:
    def setup(self):
        self.connect = Connect("localhost:8000", "camd", "camd")


    def test_get_runs(self):
        res = self.connect.get_runs(product="Firefox")
        assert "no" == res

    def test_get_tests(self):

        #print [str(x) for x in connect.get_tests(run_id=1)]
        tests = self.connect.get_tests(run_id=1)
        tests[0].markpass()
        tests[1].markfail("why u no pass?", "http://deathvalleydogs.com")
        tests[2].markinvalid("why u no make sense?")

        assert "nothin" == "\n".join([str((x.name, str(x.state))) for x in tests])

    def test_get_environment_id(self):
        #print connect.get_environments(run_id=1)
        print "id: {0}".format(self.connect.get_environment_id(run_id=1, element_list=["Chrome", "Mandarin", "OS X"]))


