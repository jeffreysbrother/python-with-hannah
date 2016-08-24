# "import module" or "from module import foo"?
# see this link: http://stackoverflow.com/questions/710551/import-module-or-from-module-import
#
# "import module" -- must type module.foo (can use 'import module as mo' as an alternative)
#
# "from module import foo" -- less typing (no need to namespace), maybe harder to understand (context lost)
#
# in the link above there is also a discussion about 'from module import *' (not advised)
#
# still not clear as to whether this imports functions, classes, both, or whatever (or anything)

from poopy import catholic

# only the catholic function is imported, so an attempt to use the nonsense function will cause the interpreter to throw an error
catholic()
nonsense()
