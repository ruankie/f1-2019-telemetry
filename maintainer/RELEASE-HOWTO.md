==============================
Step-by-step release procedure
==============================

(1) Bump the version number. It occurs in the following files:

    README.md
    setup.py
    docs/source/conf.py
    docs/source/index.rst

(2) Verify that a local build of the documentation succeeds, by running the 'maintainer/make-docs.sh' script.

(3) Use find/grep to verify that the previous version number isn't found.

(4) Do a commit of the current state of the Git repository.

    When done, push the local repository.

(5) Go to Read the Docs and trigger a rebuild of the documentation.

    If this fails, fix the problem and go back to step (2).

(6) Tag the version in Git.

    When done, push the local repository.

(7) Run the 'maintainer/make-dist.sh' script.

(8) Run the 'maintainer/upload-dist.sh' script.
