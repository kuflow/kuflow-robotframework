# Developing kuflow-robotframework

This doc is intended for contributors to `kuflow-robotframework`

## Development Environment

* Python 3.9
* Poetry
* Black (code formatter)
* Flake 8 (linter)
* PyTest
* For the generator tool:
  * Node >=16
  * Java 11 (>Java11 is not supported)

## Build

### Extend KuFlow rest client (only if you needs)

The project uses the OpenApi generator tools to provide a python rest client for KuFlow API. The generated client code is not a complete implementation of the API, only the methods that are required for the defined RobotFramework keywords. You can view the OpenApi Definition file to explore the current subset of methods. However, the generated code is not always valid due to the limitations of the (experimental) generator, so it must be treated with care.

If you need to add a new method on the client, the steps are as follows.

1. Edit the definition. You can download it from https://docs.kuflow.com/reference 

2. In the root folder:
    ```bash
    npm install
    npm run generate
    ```
    
3. Review the generated code. Please use the git source control because there are some overwrites.

### License headers

In order to add license headers to python files, run the following task:

```bash
npm run license
```

### Formatter

To format code:

```bash
poetry run black
# Or
npm run black
```

### RobotFramework keywords

The keywords of RobotFramework library are in [keywords.py](src/KuFlow/keywords.py) file. Please make sure they are properly documented.



## Test

Run all the tests with:

```bash
poetry run pytest
```
