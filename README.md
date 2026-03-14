# Pydantic Agent Experiment

> Run a Pydantic AI agent on cloud-provisioned infrastructure using Kiso — a template for reproducible agentic workloads.

## What This Is

This is a proof-of-concept that provisions a VM (via Vagrant/VirtualBox or FABRIC testbed), installs Ollama to serve a local open-source LLM, and runs a minimal Python agent using Pydantic AI. The agent asks where the 2012 Olympics were held and parses the response into a typed `CityLocation` object.

Use this as a starting template for running more complex agentic workloads on reproducible, cloud-provisioned infrastructure.

## Prerequisites

**System requirements:**
- Python 3.9+
- Vagrant + VirtualBox (for local VM provisioning), **or** a [FABRIC testbed account](https://portal.fabric-testbed.net) (for remote provisioning)

**Install Kiso:**

```sh
# Install the provider-specific dependencies for your target environment
pip install kiso[vagrant]   # for Vagrant/VirtualBox
pip install kiso[fabric]    # for FABRIC testbed
pip install kiso[vagrant,fabric]  # for both
```

## Quick Start

**1. Add credentials**

Place any required credentials in the `secrets/` directory. See [Credentials](#credentials) for details.

**2. Provision infrastructure**

```sh
kiso up
```

**3. Run the agent**

```sh
kiso run

# Check the output
cat agent-output.txt
```

**4. Tear down**

```sh
kiso down
```

Outputs defined in the experiment configuration are written to the path specified in that config.

## Credentials

> [!NOTE]
> `secrets/fabric_rc` is required only if you enable the commented `fabric` site in [`experiment.yml`](experiment.yml). No files are required in `secrets/` when using the default local Vagrant/VirtualBox setup.

- If you plan to use the optional FABRIC backend, complete the account setup steps in the [FABRIC Quick Start Guide](https://learn.fabric-testbed.net/knowledge-base/quick-start-guide/) before running `kiso up`.
- Create a [FABRIC portal account](https://portal.fabric-testbed.net) and finish the enrollment flow.
- Create a FABRIC project, or join an existing project, from the portal so your account can provision resources.
- Generate SSH keys from the portal's `User Profile -> My SSH Keys` page as described in [Generating SSH Configuration and SSH Keys](https://learn.fabric-testbed.net/knowledge-base/generating-ssh-configuration-and-ssh-keys/). FABRIC expects both bastion and sliver SSH keys.
- Download the generated SSH key files and store them locally, typically under `~/.ssh/`, with appropriate permissions.
- Generate a FABRIC API token from `Experiments -> Manage Tokens -> Open FABRIC Credential Manager` as described in [Obtaining and using FABRIC API tokens](https://learn.fabric-testbed.net/knowledge-base/obtaining-and-using-fabric-api-tokens/). If you are running FABRIC tooling from your laptop or desktop, save the downloaded token where `FABRIC_TOKEN_LOCATION` points.
- Create the `secrets/fabric_rc` file,
```sh
export FABRIC_BASTION_HOST=bastion.fabric-testbed.net
export FABRIC_PROJECT_ID=<fabric-project-id>
export FABRIC_BASTION_USERNAME=<fabric-bastion-username>
export FABRIC_BASTION_KEY_LOCATION=<path-to-fabric-bastion-key>
export FABRIC_SLICE_PRIVATE_KEY_FILE=<path-to-fabric-sliver-key>
export FABRIC_SLICE_PUBLIC_KEY_FILE=<path-to-fabric-bastion-public-key>
export FABRIC_LOG_LEVEL=INFO
export FABRIC_LOG_FILE=/tmp/fablib/fablib.log
export FABRIC_TOKEN_LOCATION=<path-to-fabric-token>
```

## References

- [EnOSlib](https://discovery.gitlabpages.inria.fr/enoslib/) — Python library for reproducible distributed systems experiments, used internally by Kiso for resource management.
- [FABRIC Testbed](https://portal.fabric-testbed.net) — NSF-funded programmable research infrastructure for large-scale networking and systems experiments.
- [Vagrant](https://developer.hashicorp.com/vagrant) — Tool for building and managing portable virtual machine environments, used for local provisioning.

## Acknowledgements

Kiso is funded by the National Science Foundation (NSF) under award [2403051](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2403051).

## License

Apache 2.0 © [Pegasus ISI](https://github.com/pegasus-isi)
