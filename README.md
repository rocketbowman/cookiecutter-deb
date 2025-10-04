# Overview

This repository defines a cookiecutter template that is used to define
infrastructure for Debian packaging. The packaging scheme is based on the 
[The Ultimate Guide to Creating Debian Packages](https://dario.griffo.io/posts/ultimate-guide-debian-packaging).

The packaging strategy does the following:

* The `build.sh` contains logic to fetch upstream binaries and invoke
  the build in the container.
* The `Dockerfile` defines the container in which the build happens.
* The `.github/workflow/release.yml` file defines the GitHub workflow that
  runs the build and deploys the artifacts to GitHub.

This template facilitates the creation of these packages by applying metadata
throughout the package definition. It also does the following:

* An `assets` directory is created in the package repository to contain things
  like images.
* The template defines `TODO` items in several places. After you populate the
  template to create your project, `post_gen_project.py` runs to collect those
  `TODO` items in a single file that indicate the file, line number, and task 
  to be performed.

# Using This Template

## Prerequisites

You must have at least one of
[cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html)
or [cruft](https://cruft.github.io/cruft/) installed to apply the template.

Cruft and cookiecutter supplement each other. Cruft enables you to keep your
projects aligned with your template. It's compatible with cookiecutter
templates, but as a newer project, it doesn't have full support of everything
that cookiecutter does. 

## Generating your project

1. Initialize the template with one of the following commands:
    1. (Recommended) `cruft create https://github.com/rocketbowman/cookiecutter-deb/`
    2. `cookiecutter gh:rocketbowman/cookiecutter-deb`
2. Provide answers to the prompts. 
3. Open `todo.txt` to see a list of tasks to complete to get your package to
   build.. Work through the tasks until they are complete. 

Cruft is recommended when you want to keep the project in sync with updates to
the template. When using cruft to create your project, it records your responses
in a `.cruft.json` alongside a git hash of the template that produced it. That 
enables cruft to detect changes between the current template and the one used
to generate your project.

If you want to defer answering some prompts, you can use the defaults that are
provided. When you leave a required prompt unanswered, a `TODO` item is placed
for completion later.

The `todo.txt` file is generated once when the template is created. After that,
it is static. It is produced by scanning the files in your project for the
literal string `TODO`. You are responsible for marking items resolved and 
clearing the `TODO` entries in the file as you complete them.

When you are done with your package, you can upload your source to GitHub with
steps like these:

``` bash
git init
git add *
git commit -m "init: create debian package for <pkgname>"
git remote add origin https://github.com/<username>/<repo-name>.git>
git branch -M main
git push -u origin main
```

# Keeping Packages Synchronized with Template

Consult the [Cruft Documentation](https://cruft.github.io/cruft/) for details.

Here is a short list of highlights.

* Use `cruft check` to verify that your project is consistent with the template
* Use `cruft diff` to see the differences between your project and the template
* Use `cruft update` to apply updates from the project to your template.
