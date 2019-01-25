from distutils.core import setup

setup(
    name='Krakatau',
    version='1.0',
    packages=['Krakatau', 'Krakatau.ssa', 'Krakatau.ssa.ssa_ops',
              'Krakatau.ssa.ssa_jumps', 'Krakatau.ssa.constraints', 'Krakatau.java', 'Krakatau.util',
              'Krakatau.verifier', 'Krakatau.assembler', 'Krakatau.classfileformat'],
    package_data={'Krakatau': ['../assemble.py', '../disassemble.py', '../decompile.py']},
    url='https://github.com/Storyyeller/Krakatau',
    license=' GPL-3.0',
    author='Robert Grosse',
    author_email='',
    description=' Java decompiler, assembler, and disassembler'
)
