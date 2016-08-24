# "import module" or "from module import foo"?
# see this link: http://stackoverflow.com/questions/710551/import-module-or-from-module-import
#
# "import module" -- must type module.foo (can use 'import module as mo' as an alternative)
#
# "from module import foo" -- less typing (no need to namespace), maybe harder to understand (context lost)
#
# still not clear as to whether this imports functions, classes, both, or whatever (or anything)

from poopy import nonsense

catholic()
nonsense()
