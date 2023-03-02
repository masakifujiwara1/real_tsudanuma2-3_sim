from setuptools import setup

package_name = 'real_tsudanuma2-3_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    # py_modules=[
    #     'my_node'
    # ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='fmasa',
    author_email='fmasa@todo.todo',
    maintainer='fmasa',
    maintainer_email='fmasa@todo.todo',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'The real_tsudanuma2-3_sim package.'
    ),
    license='TODO',
    tests_require=['pytest'],
    # entry_points={
    #     'console_scripts': [
    #         'my_node = my_node:main'
    #     ],
    # },
)