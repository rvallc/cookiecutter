#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from .generate import generate_context, generate_files


def main():
    """ Entry point for the package, as defined in setup.py. """

    # Get command line input/output arguments
    parser = argparse.ArgumentParser(
        description='Create a project from a Cookiecutter project template.'
    )
    parser.add_argument(
        'input_dir',
        help='Cookiecutter project template dir, e.g. {{project.repo_name}}/'
    )
    args = parser.parse_args()

    context = generate_context()
    generate_files(
        input_dir=args.input_dir,
        context=context
    )


if __name__ == '__main__':
    main()
