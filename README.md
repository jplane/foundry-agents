# Using Azure AI Agent Service

This repo demonstrates a few simple examples of AI agents using tools like [Python function calls](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=code-example), [vectorized file search](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=upload-files-code-examples), and [Open API invocation](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=code-example).

## Prerequisites

- Azure subscription
- Azure AI Foundry [hub](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal) and [project](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
    - [choose a region that supports the Azure AI Agent Service](https://learn.microsoft.com/en-us/azure/ai-services/agents/concepts/model-region-support)
    - each user must have **Storage Blob Data Contributor** and **Azure AI Developer** RBAC roles assigned at the resource group level
- Visual Studio Code or Cursor
- [Dev Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Setup

- ensure you have a [supported model](https://learn.microsoft.com/en-us/azure/ai-services/agents/concepts/model-region-support) deployed in your Foundry hub... the example notebooks use `gpt-4o` but you're free to change that

- clone this repo

- open the repo in Visual Studio Code or Cursor

- open the command palette and select **Dev Containers: Reopen in Container**. This will build the dev container and install the required dependencies

- [obtain your Foundry project connection string](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?tabs=linux#insert-your-connection-string)

- copy [./src/notebooks/.env.example](./src/notebooks/.env.example) to `./src/notebooks/.env` and add the connection string

- log into the Azure CLI and select your target subscription

    ```bash
    az login
    az account set --subscription <your-subscription-id>
    ```

## Azure AI Agent with Python Function Calls

This sample illustrates an agent configured with a local Python function as a tool. The agent calls the function to perform a task like getting the weather for a specific location.

- [notebook](./src/notebooks/agent_with_local_function_call.ipynb)

## Azure AI Agent with Vectorized File Search

This sample illustrates an agent configured with a vectorized file search tool. The agent finds content from the files relevant to a given goal or user request, and uses the content to synthesize a response to the user (including annotations to the original source text).

- [notebook](./src/notebooks/agent_with_file_search.ipynb)

## Azure AI Agent with OpenAPI Invocation

This sample illustrates an agent configured with an OpenAPI invocation tool. The agent issues a REST API call to gather relevant information and synthesize a response to the user.

> _This example requires the [api](./src/api) directory is deployed to a public endpoint. A recommended way to do this is using [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview); if you're using Visual Studio Code, the [extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurecontainerapps) makes [deployment](https://learn.microsoft.com/en-us/azure/container-apps/deploy-visual-studio-code) easy. The extension is already installed in the Dev Container. You can also deploy without VS Code, using the [Azure CLI](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-code-to-cloud?tabs=bash%2Ccsharp)._

- [notebook](./src/notebooks/agent_with_open_api.ipynb)

## Azure AI Agent with multiple tools

This sample illustrates an agent configured with multiple tools. The agent uses the tools to gather information from different sources and synthesize a response to the user.

- [notebook](./src/notebooks/agent_with_multiple_tools.ipynb)
