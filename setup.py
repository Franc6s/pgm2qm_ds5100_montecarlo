from setuptools import setup

setup(name = 'Monte Carlo Simulator',
      version = '1.0',
      description = 'Python Package for Montecarlo Simulator',
      url = 'https://github.com/Franc6s/pgm2qm_ds5100_montecarlo',
      author = 'Francis Mangala',
      author_email = 'pgm2qm@virginia.edu',
      license = 'MIT',
      packages = ['Montecarlo'],
      install_requires = ['numpy', 'pandas', 'random'])