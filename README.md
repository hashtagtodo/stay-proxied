## STAY PROXIED

This software is designed to allow you to generate daily lists of active and free proxies. It includes three proxy sources; however, you can add additional sources as long as they are URLs with plain text lists.

### How does it work?

#### Step 1: Clone the Git Repository

Clone the repository with the following command:
```bash
git clone https://github.com/hashtagtodo/stay-proxied.git
```

#### Step 2: Install the Requirements

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

#### Step 3: Edit the config.json File

Edit the `config.json` file with the following settings:

**proxychains-path**: The path to your proxychains configuration file. The default path is included, but you can specify any directory.

**auto-update**: This allows the script to overwrite the proxychains.conf file once the established number of valid proxies is reached. Set to 1 to enable auto-update, or 0 to require user confirmation.

 **max-proxies**: The number of valid proxies needed before saving them to proxychains.conf.

#### Step 4: Run the Script

Run the script with root permissions:
```bash
sudo python main.py
```

**Note:**
It is necessary to run this script with root permissions; otherwise, it will not execute.

### How to Add More Sources

The `sources.txt` file contains the necessary URLs for proxy sources.

If your proxy list only has the format `ip:port`, you should indicate the protocol by adding it in the following way:
```
protocol|url
```

Example

socks5|https://domain.com/proxies.txt

In case your proxy list includes the protocol, i.e., `protocol://ip:port`, you should add the term `none` in the following way:
```
none|url
```
Example

none|https://domain.com/proxies_withprotocol.txt
