==============================
Step-by-step release procedure
==============================

(1) Bump the version number. It occurs in the following files:

    README.md
    setup.py
    docs/source/conf.py
    docs/source/index.rst

    TIP: Use find/grep to look for the previous version number!

(2) Verify that a local build of the documentation succeeds, by running the 'maintainer/make-docs.sh' script.

(3) Do a commit of the current state of the Git repository.

(4) Go to Read the Docs and trigger a rebuild of the documentation.

    If this fails, fix the problem and go back to step (2).

(5) Tag the version in Git.

(6) Run the 'maintainer/make-dist.sh' script.

(7) Run the 'maintainer/upload-dist.sh' script.
