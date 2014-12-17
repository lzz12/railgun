import unittest
import operator

from scriptlibs import Version
class VersionTestCase(unittest.TestCase):
    def setUp(self):
        self.version = Version()
        
    def tearDown(self):
        self.version = None
        
    def testCmp(self):
        self.c = cmp((1,0,1),(2,0,1) )
        self.assertEqual(self.c, 2)
    
    def test_Data_str(self):
        self.version.set('1.0.1')
        self.assertEqual(self.version.data, (1, 0, 1))
    ##
    def test_Data_unicode(self):
        self.version.set(u'1.0.1')
        self.assertEqual(self.version.data, (1, 0, 1))
        
    def test_Data_Version(self):
        Version ver = Version()
        ver.set('1.0.1')
        self.version.set(ver)
        self.assertEqual(self.version.data, (1, 0, 1))
        
    def test_Data_list(self):
        ll = [1, 0, 1]
        self.version.set(ll)
        self.assertEqual(self.version.data, (1, 0, 1))
        
    def test_Data_tuple(self):
        tt = (1, 0, 1)
        self.version.set(tt)
        self.assertEqual(self.version.data, (1, 0, 1))  
        
from scriptlibs import Dependency
class DependencyTestCase(unittest.TestCase):
    def setUp(self):
        self.dependency = Dependency()

    def tearDown(self):
        self.dependency = None

    def test_Dependency(self):
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.dependency.set(dep)
        self.assertEqual(self.dependency.pkgname,'bootstrap')
        self.assertEqual(self.dependency.pkgver,'3.0')
        self.assertEqual(self.dependency.veropt,'>=')
        self.assertEqual(self.dependency._checker,operator.ge)

    def test_not_Dependency(self):
        self.dependency.set('bootstrap >= 3.0')
        self.assertEqual(self.dependency.pkgname,'bootstrap')
        self.assertEqual(self.dependency.pkgver,'3.0')
        self.assertEqual(self.dependency.veropt,'>=')
        self.assertEqual(self.dependency._checker,operator.ge)

    def test_check(self):
        self.dependency.set('bootstrap >= 3.0')
        self.assertTrue(self.dependency.check(3.0))

from scriptlibs import DependencySet
class DependencySetTestCase(unittest.TestCase):
    def setUp(self):
        self.dependencyset = DependencySet()

    def tearDown(self):
        self.dependencyset = None
   
    def test_deps_str(self):
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.dependencyset.deps(dep)
        self.assertEqual(self.dependencyset.data['bootstrap'],dep)
    
    ##  
    def test_deps_Dependency(self):
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.dependencyset.deps(dep)
        self.assertEqual(self.dependencyset.data['bootstrap'],dep)

    def test_checkdep(self):
        self.dependencyset.deps('bootstrap >= 3.0')
        self.assertTrue(self.dependencyset.checkdep('bootstrap',3.0))

from scriptlibs import ScriptLib
class ScriptLibTestCase(unittest.TestCase):
    def setUp(self):
        self.sclib = ScriptLib()

    def tearDown(self):
        self.sclib = None

    def test_deps_str(self):
        self.sclib.deps('bootstrap >= 3.0')
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.assertEqual(self.sclib.depends.data['bootstrap'],dep)

    def test_deps_Dependency(self):
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.sclib.deps(dep)
        self.assertEqual(self.sclib.depends.data['bootstrap'],dep)

    def test_checkdep(self):
        self.sclib.deps('bootstrap >= 3.0')
        ScriptLib script = ScriptLib()
        script.deps('bootstrap >= 3.0')
        self.assertTrue(self.sclib.checkdep(script))

from scriptlibs import ScriptRepo
class ScriptRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.scriptrepo = ScriptRepo()

    def tearDown(self):
        self.scriptrepo = None

    def test_addScript(self):
        ScriptLib script = ScriptLib()
        script.deps('bootstrap >= 3.0')
        self.scriptrepo.addScript(script)
        self.assertEqual(self.scriptrepo.scripts['bootstrap'],script)

    def test_getScript(self):
        ScriptLib script = ScriptLib()
        script.deps('bootstrap >= 3.0')
        self.scriptrepo.addScript(script)
        self.assertEqual(self.scriptrepo.getScript('bootstrap'),script)

from scriptlibs import PageScripts
class PageScriptsTestCase(unittest.TestCase):
    def setUp(self):
        self.pagescripts = PageScripts()

    def tearDown(self):
        self.pagescripts = None

    def test_deps_str(self):
        self.pagescripts.deps('bootstrap >= 3.0')
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.assertEqual(self.pagescripts.depends.data['bootstrap'],dep)

    def test_deps_Dependency(self):
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        self.pagescripts.deps(dep)
        self.assertEqual(self.pagescripts.depends.data['bootstrap'],dep)

    def test_depScript_str(self):
        ScriptLib script = ScriptLib()
        script.deps('bootstrap >= 3.0')
        self.pagescripts.deps('bootstrap >= 3.0')
        self.assertEqual(self.pagescripts._depScript('bootstrap >= 3.0'),script)

    def test_depScript_Dependency(self):
        Dependency dep = Dependency()
        dep.set('bootstrap >= 3.0')
        ScriptLib script = ScriptLib()
        script.deps('bootstrap >= 3.0')
        self.pagescripts.deps(dep)
        self.assertEqual(self.pagescripts._depScript('bootstrap >= 3.0'),script)


if __name__ == '__main__':
    unittest.main()
