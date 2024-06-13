# Contributing to Mazaal AI Public Models Repositories

Thank you for your interest in contributing to our project :sparkles:. We appreciate your support and welcome contributions from the community. This document outlines the guidelines and steps to contribute effectively.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Contributing via Pull Requests](#contributing-via-pull-requests)
3. [Google-Style Docstrings](#google-style-docstrings)
4. [Development Setup](#development-setup)
5. [Reporting Bugs](#reporting-bugs)

## Code of Conduct

All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read and follow it to maintain a welcoming and inclusive environment for everyone involved in the project.

## Contributing via Pull Requests

We welcome code contributions to enhance the project. To contribute code, please follow these steps:

1. **Fork the repository**: Click on the "Fork" button at the top-right corner of the project's GitHub page to create a copy of the repository in your GitHub account.

2. **Clone the forked repository**: Clone the forked repository to your local machine using the following command:

```
git clone https://github.com/your-username/project.git
```

3. **Create a new branch**: Create a new branch with a descriptive name for your feature or bug fix. Use the following command:
```
git checkout -b feature/your-feature-name
```

4. **Add your model**: Add your own model, following the project's coding style and guidelines. Ensure that your code is well-documented and includes appropriate tests. Your model should include the following structure (see the example model in models/text/example_text_model):
```
Dockerfile - Dockerfile to run your model's prediction
main.py - Your model's prediction function
requirements.txt - Required libraries for your model
```

5. **Commit your changes**: Commit your changes with a clear and descriptive commit message. Use the following commands:
```
git add .
git commit -m "Add your commit message here"
```

6. **Push your changes**: Push your changes to your forked repository using the following command:
```
git push origin feature/your-feature-name
```

7. **Create a pull request**: Go to the project's GitHub page and click on the "Pull requests" tab. Click on the "New pull request" button. Select your forked repository and the branch you created. Provide a clear title and description for your pull request, explaining the changes you made and why they are valuable to the project.

8. **Address feedback**: Our maintainers will review your pull request and provide feedback. Please be responsive to their comments and make the necessary changes to improve your contribution.

## Google-Style Docstrings
When adding a new model, include a Google-style docstring to provide clear and concise documentation. This makes it easier for other developers to understand and work with your code later.
```python
def calculate_average(numbers: List[float]) -> float:
    """Calculates the average of a list of numbers.

    Args:
        numbers: The list of numbers to calculate the average of.

    Returns:
        The average of the input numbers.

    Raises:
        ValueError: If the input list is empty.

    Example:
        >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        >>> calculate_average(numbers)
        3.0
    """
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)
```

## Development Setup

To set up the development environment for this project, please follow the instructions in the [README](README.md) file.

## Reporting Bugs

If you encounter any bugs, have feature requests, or want to discuss improvements, please **open an issue** on our GitHub repository. When reporting bugs, provide a clear and concise description of the problem, along with steps to reproduce it. Include any relevant error messages or screenshots to help us understand and resolve the issue more effectively.
