from setuptools import setup

setup(name='commandline.template.tutorial',
      version='0.1',
      description='test stuff for pycon tutorial',
      py_modules=['wordcount_lib'],
      scripts=['wordcount'],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
)