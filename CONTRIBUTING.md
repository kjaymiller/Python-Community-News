# Contributing (Code) to Python Community News

Thank you for taking interest in contributing to this project.


## Before you start
This project has a [Code of Conduct](CODE_OF_CONDUCT.md) that you MUST follow in order to participate in this project in any way.

This document is intended to help first-time or returning contributors to the project. It covers making contributions outside of the scheduled content and topics. For more information on how to submit a topic or conference, please see the [README](README.md).

## About the code in this project

You can break the code into essentially four parts:
- [Contributing (Code) to Python Community News](#contributing-code-to-python-community-news)
  - [Before you start](#before-you-start)
  - [About the code in this project](#about-the-code-in-this-project)
    - [For All Types of Contributions](#for-all-types-of-contributions)
      - [If Wanting to Work on an Existing Issue](#if-wanting-to-work-on-an-existing-issue)
    - [Automation with Github via GH Actions](#automation-with-github-via-gh-actions)
  - [General Administration around GitHub](#general-administration-around-github)
    - [Deployting to our third-party platforms via API](#deployting-to-our-third-party-platforms-via-api)
  - [Deploying of content to the web via Render Engine](#deploying-of-content-to-the-web-via-render-engine)

You are able to contribute to all four of these parts but in different ways.

### For All Types of Contributions
To ensure that everyone is one the same page, please follow this process for all types of contributions.

1. Read and follow [Code of Conduct](CODE_OF_CONDUCT.md)
2. Create an issue on GitHub with the title of your perspective change. Use the approriate labels for the type of contribution you are making. Examples of appropriate labels are:
    - `bug`
    - `feature`
    - `documentation`
    - `gh action`

    For bugs and features include a label for the area of the project that is affected. Examples of appropriate labels are:
        - `newsletter`
        - `website`
        - `podcast`

3. Specify that you will work on this issue. This lets others know that someone is actively working on the project.
4. Fork the repository on your profile and make changes locally. 

#### If Wanting to Work on an Existing Issue

**Claim** the issue by commenting on it or stating you will work on the issue. We will accept PRs from the first person (collaborating on an issue is encouraged).

![Create a Branch from an Issue](.github/assets/Create%20Branch.jpg)

### Automation with Github via GH Actions

GH Actions allow you to automate the deployment of your code to GitHub.

We intend to use GitHub Actions to automate the compilation of issues to consider for the show and the creation of at show pull request.

We'll also use GitHub Actions to interact with issues as they relate to the associated [Project](https://github.com/users/kjaymiller/projects/4) boards.

Just adding a missing period here.

We'll also be using GH Actions to automate sending supporting content to our newsletter service (currently [ButtonDown](https://buttondown.email/)), and perhaps other services as we see fit. 

You should submit a PR for a GitHub Actions if you believe the action will improve how we interact with our existing workflow.

If you would like to pose a change to the existing workflow, please file and issue and wait for aggreement from the maintainers before working on the project.

## General Administration around GitHub
We use GitHub issues to communicate many changes that we would like to deploy to our website/podcast/newsletter and the inner workings of between them all. These may result in an issue with an `admin` label. 

These are often changes to issue/PR templates or documentation that communicates the intention of the project.

You are more than invited to work on these issues. Following the guidance given [above](#for-all-types-of-contributions).

### Deployting to our third-party platforms via API

We have to authenticate with our third-party platforms to deploy content to them and this requires an API key and often subject to rate-limiting. 

If you are working on code that would connect to a Third Party, YOU MUST USE A TEST-CASE and mock the API call request and responses.

We use [`httpx`](https://www.python-httpx.org) to make REST API calls to our third-party platforms and [`pytest-httpx`](https://pypi.org/project/pytest-httpx/) to mock those API calls in testing.

## Deploying of content to the web via Render Engine
We want to keep an archive of our content and make it easier for people for find the show and share it with others. For that reason all of our episodes are also shared at https://pythoncommunitynews.com.

We use [Render_Engine](https://github.com/kjaymiller/render_engine). Render Engine is a Static Site Generator that uses markdown and frontmatter to generate static HTML pages.

If you have a change on how Render Engine should generate the pages, please submit an issue on [that repository](https://github.com/kjaymiller/render_engine)

If you have a content change that you would like to make please submit a PR in the correct file/directory/repository.

If there is a typo or specific change to content change and the show has not been released, comment on the corresponding issue with the `[BUILD]<YYYY-MM-DD.md>` name. If caught in time doing this will ensure the changes are deployed to all the relevant places.

If the content has been released already, submit a PR to the corresponding file in `/site/content/YYYY-MM-DD.md`. Once the show and newsletter have been released, we can manually change the information in the archive but it is unlikely that people will get the change before it has been sent to them.

We store the output of Render Engine in the `web` repository. This helps to eliminate confusion as to where content needs to be updated. The website is rebuilt with every pull request.