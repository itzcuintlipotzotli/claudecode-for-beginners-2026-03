[gh-conf-ssh-keys]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
[gh-troubleshoot-ssh-keys-conf]: https://docs.github.com/authentication/troubleshooting-ssh
[claude-pricing]: https://claude.com/pricing
[claude-install]: https://claude.com/product/claude-code
[cc-settings]: https://docs.anthropic.com/en/docs/claude-code/settings
[cc-memory]: https://docs.anthropic.com/en/docs/claude-code/memory
[cc-permissions]: https://docs.anthropic.com/en/docs/claude-code/settings#permissions
[cc-sandboxing]: https://www.anthropic.com/engineering/claude-code-sandboxing
[owasp-wstg]: https://owasp.org/www-project-web-security-testing-guide/
[owasp-asvs]: https://owasp.org/www-project-application-security-verification-standard/

![AI Assisted Secure Coding](resources/heading-image.png)

# Prerequisites

- GitHub account — a free account works.
- Claude subscription — a Pro is needed, you can get one at [Claude Pricing][claude-pricing].
- Git Bash or WSL2 — only if you are planning to [Run the lab locally](#run-locally)

# Setup

We'll go over two different exercises where we'll work together with Claude Code to perform quality-related tasks; the exercises can be carried out locally on your machine or in _GitHub Codespaces_.

## 1. Fork the Repository

You'll work on your own fork of this repository. To get started, locate the Fork button at the top of the repository page, next to _Watch_ and _Star_.

![gh-code-toolbar](resources/gh-repo-toolbar.png)

1. Click the **Fork** button.
2. Make sure your user is selected in the _Owner_ drop-down.
3. Provide a name for the repository or leave it as-is.

You may now browse to the new repository under your account.

Once you have your fork ready, proceed to [Run in Codespaces](#run-in-codespaces) or [Run Locally](#run-locally) which are the two choices to setup your environment.

## Run in Codespaces

GitHub Codespaces gives you a ready-to-use development environment in your browser — no local installation needed. This is the recommended path if you are not familiar with local development setup.

### 2. Open the Repository in Codespaces

Once you are on the front page of your forked repository:

1. Click the green **Code** button — a palette will pop up.
2. Select the **Codespaces** tab, then click **Create codespace on main**.

![gh-repo-code](resources/gh-codespaces.png)

A new tab will open while your codespace is being set up. Wait for it to finish — you should then see an editor with the file tree on the left side.

### 3. Install Claude Code

Once your codespace is up and running, install the Claude Code extension:

1. Open the Extensions sidebar (_Ctrl+Shift+X_).
2. Search for **Claude Code**.
3. Click **Install**.

### 4. Authenticate

If the Claude Code tab is not visible yet, open the command palette with _Ctrl+Shift+P_ and select **Claude > Open in New Tab**.

Select the option to authenticate with a Claude subscription and use your account to sign in.

>Dismiss the dialog that pops up by hitting "Cancel" and copy the URL provided in the Claude tab, copy and paste in your browser to authenticate and follow the instructions shown in the page to finish up.

You are all set — jump straight to the [Exercises](#exercises) section.

---

## Run Locally

Use this path if you prefer to work on your own machine. You will need:

- VS Code (extensions may vary)
- Your preferred terminal emulator
- Git

### 2. Set Up Access to GitHub

You need a way to authenticate with GitHub to clone your repository. Pick **one** of the two options below.

#### Option A — SSH Keys

SSH keys are the most common method. If you have already set up SSH keys for GitHub you can skip ahead to [clone the repository](#3-clone-the-repository).

**Generate a new SSH key:**

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Accept the default file location by pressing _Enter_, and optionally set a passphrase.

**Copy the public key to your clipboard:**

```bash
# macOS
cat ~/.ssh/id_ed25519.pub | pbcopy

# Linux
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard

# Windows (Git Bash or WSL)
cat ~/.ssh/id_ed25519.pub | clip
```

**Add the key to GitHub:**

1. Go to **GitHub → Settings → SSH and GPG keys**.
2. Click **New SSH key**, paste the key, and save.

If you run into any issues, refer to the [SSH troubleshooting guide][gh-troubleshoot-ssh-keys-conf].

---

#### Option B — GitHub CLI

The GitHub CLI (`gh`) handles authentication and cloning without needing to manage SSH keys manually.

**Install the GitHub CLI:**

```bash
# macOS
brew install gh

# Windows (winget)
winget install --id GitHub.cli

# Ubuntu / Debian
sudo apt update && sudo apt install gh

# Fedora / RHEL
sudo dnf install gh
```

**Authenticate:**

```bash
gh auth login
```

Follow the interactive prompts — select **GitHub.com**, choose **HTTPS** as the preferred protocol, and authenticate via browser when asked.

---

### 3. Clone the Repository

Once you are on the front page of your forked repository, click the green **Code** button and copy the URL shown, then run one of the commands below depending on the method you chose in the previous step.

**SSH:**

```bash
git clone git@github.com:YOUR_USERNAME/REPO_NAME.git
```

**HTTPS:**

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
```

**GitHub CLI:**

```bash
gh repo clone YOUR_USERNAME/REPO_NAME
```

Replace `YOUR_USERNAME` and `REPO_NAME` with the values from your forked repository URL.

### 4. Install Claude Code

Claude Code is distributed as an npm package, so you'll need **Node.js 18 or later** installed first.

**Install Node.js (if not already installed):**

```bash
# macOS
brew install node

# Windows (winget)
winget install OpenJS.NodeJS

# Ubuntu / Debian
sudo apt update && sudo apt install nodejs npm

# Fedora / RHEL
sudo dnf install nodejs npm
```

**Install the Claude Code CLI:**

```bash
npm install -g @anthropic-ai/claude-code
```

**Confirm the installation worked:**

```bash
claude --version
```

**Install the VS Code extension (optional but recommended):**

```bash
code --install-extension anthropic.claude-code
```

### 5. Authenticate

Open a terminal, navigate to the directory where you cloned the repository, and run:

```bash
claude
```

Select the option to authenticate with a Claude subscription and use your account to sign in.
# Exercises

## E1 - Refactor the Asset Management Application

A FastAPI web application that manages hardware and software assets in an organisation. The code is under `assets_management_app`. Use Claude Code to extend it with the following:

1. An endpoint to add one or more tags to an asset.
2. Activate or deactivate an asset. Inactive assets should not appear in listings by default; record when and by whom the asset was deactivated.
3. Decommission an asset. This is a permanent action; record when and by whom it was carried out.
4. Retrieve an asset by ID. Inactive and decommissioned assets can be looked up by ID.

## E2 - Create an Application from Scratch

A companion web API where devices can report security events caught by a local agent. Requirements are documented in `threat_management_app/README.md`.

1. Adjust the description or requirements as needed — for example, swap the language or stack, or tweak the functional requirements.
2. Instruct Claude to read `threat_management_app/README.md` and implement the API with tests.
3. Review the output and iterate with follow-up prompts.


