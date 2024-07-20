# github_actions
https://zenn.dev/tk_resilie/articles/python_test_template

https://zenn.dev/panyoriokome/scraps/ad415e5ffc7c3d

https://docs.github.com/ja/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners

https://docs.github.com/ja/actions/hosting-your-own-runners/managing-self-hosted-runners/using-a-proxy-server-with-self-hosted-runners


# self-hosted runner
https://qiita.com/h_tyokinuhata/items/7a9297f75d0513572f4a
https://zenn.dev/hironobuu/articles/e85418948e896f

# Download
# Create a folder
$ mkdir actions-runner && cd actions-runner# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.317.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.317.0/actions-runner-linux-x64-2.317.0.tar.gz# Optional: Validate the hash
$ echo "9e883d210df8c6028aff475475a457d380353f9d01877d51cc01a17b2a91161d  actions-runner-linux-x64-2.317.0.tar.gz" | shasum -a 256 -c# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.317.0.tar.gz

# disable ipv6
ipv6を無効にしないと、HTTP接続エラーになる。
https://qiita.com/htshozawa/items/77dd0be079cdf817a5a6

# Configure
# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/hardwork9047/github_actions --token BE7PUOYLBYRBVK7UMX5BVCTGTNSRA# Last step, run it!
$ ./run.sh

# Using your self-hosted runner
# Use this YAML in your workflow file for each job
runs-on: self-hosted