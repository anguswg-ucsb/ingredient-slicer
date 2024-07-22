#!/bin/bash

# Example usage:
# sh sh/publish_to_pypi.sh <package name> <version> <TestPyPI API Token> <PyPI

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <package name> <version> <TestPyPI API Token> <PyPI API Token>"
    exit 1
fi

PACKAGE_NAME=$1
VERSION=$2
TESTPYPI_TOKEN=$3
PYPI_TOKEN=$4
EGG_FILE="$PACKAGE_NAME.egg-info"

echo "Package name: $PACKAGE_NAME"
echo "Version: $VERSION"

echo "Updating version in pyproject.toml to $VERSION..."
sed -i '' "s/^version = \".*\"/version = \"$VERSION\"/" pyproject.toml
# sed -i.bak "s/^version = \".*\"/version = \"$VERSION\"/" pyproject.toml
# sed -i -e 's/^version = ".*"/version = "1.0.9"/' pyproject.toml

# # Delete old dist/ folder
# if [ -d "dist" ]; then
#     echo "Deleting old dist/ folder..."
#     rm -r dist/
# fi

# Delete the specific .egg-info folder
if [ -d "$EGG_FILE" ]; then
    echo "Deleting $EGG_FILE..."
    rm -r "$EGG_FILE"
fi

echo "Building package..."
python3 -m build

echo "Checking dist/ with twine..."
twine check dist/*

echo "Uploading package to TestPyPI..."
TWINE_PASSWORD=$TESTPYPI_TOKEN twine upload -r testpypi dist/*

echo "Uploading package to PyPI..."
TWINE_PASSWORD=$PYPI_TOKEN twine upload dist/*

echo "Completed publishing version $VERSION of $PACKAGE_NAME to PyPI!"