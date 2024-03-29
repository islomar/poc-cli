# Playground for CLI tools
Playground for experimenting with building CLI tools

## Public CLIs
- Tynibird
  - https://pypi.org/project/tinybird-cli
  - https://docs.tinybird.co/cli.html
  - Python
  - Features:
    - TBD
- [AWS](https://docs.aws.amazon.com/cli/latest/)
- [AWS SAM CLI](https://github.com/aws/aws-sam-cli)
  - Python
  - [Click](https://click.palletsprojects.com/en/8.1.x/) for the command-line interface
- [Google Cloud](https://cloud.google.com/sdk/gcloud)
- [GitHub CLI](https://github.com/cli/cli)
  - Go
- [Slack CLI](https://slack.engineering/the-joy-of-internal-tools/)
  - https://github.com/slackhq/magic-cli
- Anonymized CLI
  - TBD


## Options
- **Argparse**
  - The standard library
- **Docopts**
  - http://docopt.org/
  - https://github.com/docopt/docopts
  - https://github.com/denisidoro/docpars
  - https://github.com/CodelyTV/dotly/blob/main/scripts/core/documentation.sh
- **Click**
  - https://click.palletsprojects.com/en/8.1.x/
  - [Why Click?](https://click.palletsprojects.com/en/latest/why/)
- **Invoke**
  - a simple task running library that can be used to build a command-line application
  - https://www.pyinvoke.org/
- **Charm**
  - https://charm.sh/

## Resources
- [Click vs Argparse vs Docopt](https://click.palletsprojects.com/en/8.1.x/why/#why-not-docopt-etc)
- [Comparing Python Command-Line Parsing Libraries – Argparse, Docopt, and Click](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
- [Best practices for inclusive CLIs](https://seirdy.one/posts/2022/06/10/cli-best-practices/)
- [UX patterns for CLI tools](https://lucasfcosta.com/2022/06/01/ux-patterns-cli-tools.html)


## Ideas to implement (just for learning)
- Distribute as 
  - Python package
    - https://realpython.com/pypi-publish-python-package/
    - https://acloudguru.com/hands-on-labs/building-a-command-line-tool-with-python
  - Go binary
- Automate the publication with GitHub Actions
- Jira issues older than N weeks/months
- GitHub stats
- Twitter stats
- Check if all the needed tools for X are installed (bonus: and up to date)
- Automatic local set up (e.g. instal Docker, etc)
- Automatic set up for a project (clone repo, install tools, run all the tests, etc)
- Include help
- Self update
- Report new version exists
- Use Yubikey for retrieving secrets
