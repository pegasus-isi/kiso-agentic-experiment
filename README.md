# Pydantic Agent Experiment

> Run a Pydantic AI agent on cloud-provisioned infrastructure using Kiso — a template for reproducible agentic workloads.

## What This Is

This is a proof-of-concept that provisions a VM (via FABRIC testbed or Vagrant/VirtualBox), installs Ollama to serve a local open-source LLM, and runs a minimal Python agent using Pydantic AI. The agent asks where the 2012 Olympics were held and parses the response into a typed `CityLocation` object.

Use this as a starting template for running more complex agentic workloads on reproducible, cloud-provisioned infrastructure.

## Prerequisites

**System requirements:**
- Python 3.9+
- a [FABRIC testbed account](https://portal.fabric-testbed.net) (for remote provisioning), **or** Vagrant + VirtualBox (for local VM provisioning)

**Install Kiso:**

```sh
# Install the provider-specific dependencies for your target environment
pip install kiso[fabric]    # for FABRIC testbed
pip install kiso[vagrant]   # for Vagrant/VirtualBox
pip install kiso[fabric,vagrant]  # for both
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
> `secrets/fabric_rc` is required for the default `fabric` site in [`experiment.yml`](experiment.yml). No files are required in `secrets/` when using the local Vagrant/VirtualBox setup. To use Vagrant/VirtualBox comment out the `fabric` site and uncomment the `vagrant` site in [`experiment.yml`](experiment.yml).

- Create a [FABRIC portal account](https://portal.fabric-testbed.net) and finish the enrollment flow.
- [Have an active FABRIC project allocation](https://learn.fabric-testbed.net/knowledge-base/creating-or-joining-a-project/) — create a new project or join an existing one
- [SSH keys generated and configured](https://learn.fabric-testbed.net/knowledge-base/generating-ssh-configuration-and-ssh-keys/) — required for Kiso to connect to provisioned nodes over SSH
- [A FABRIC API token generated](https://learn.fabric-testbed.net/knowledge-base/obtaining-and-using-fabric-api-tokens/) — required for the RC file
- Create a FABRIC RC file (used as `rc_file` in the config)
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
