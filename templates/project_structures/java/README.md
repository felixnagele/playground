# Java Template

Uses Maven & Java JDK 25 LTS

## Structure

- root files (README.md, pom.xml, .gitignore, etc.)
- src
  - main
    - java
    - resources
  - test
    - tests

## Setup

### Install & Build

```bash
mvn clean install
```

### Test

```bash
mvn test
```

### Run

```bash
cd target
```

```bash
java -jar templateRaw.jar
```

## Notes

- Make sure to have Java JDK 25 LTS installed and configured in your environment.
- Maven is used for dependency management and build automation.
- Adjust the `pom.xml` file to add any additional dependencies as needed.
- You can customize the project structure further based on your requirements.
