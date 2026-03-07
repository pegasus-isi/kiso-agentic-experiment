# Pydantic Agent Experiment

The experiment is a proof-of-concept demonstrating how to run an AI agent workload on provisioned infrastructure using Kiso. The experiment provisions a virtual machine (via Vagrant/VirtualBox or optionally FABRIC testbed), installs Ollama to serve a local open-source LLM, and then runs a small Python agent using Pydantic that queries the model for structured output. The agent itself is intentionally minimal — it asks where the 2012 Olympics were held and parses the response into a typed CityLocation object — serving as a template for running more complex agentic workloads on reproducible, cloud-provisioned infrastructure.

## Prerequisites

```sh
pip install kiso
# Install the resource provider specific dependencies you want to use
pip install kiso[vagrant,fabric]
```

## Running the experiment

Place any required credentials files in the `secrets` directory.

## Running the experiment

```sh
# Provision and setup the resources
kiso up --output ./output

# Run the experiments defined in the experiment configuration YAML file
kiso run --output ./output

# Destroy the provisioned resources
kiso down --output ./output

# Outputs defined in the experiment configuration will be placed to the destination specified in the experiment configuration.
```

# References

- [EnOSlib](https://discovery.gitlabpages.inria.fr/enoslib/)
- [FABRIC](https://portal.fabric-testbed.net)
- [Vagrant](https://developer.hashicorp.com/vagrant)

# Acknowledgements

Kiso is funded by National Science Foundation (NSF) under award [2403051](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2403051).
