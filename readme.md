
# Viole - Random Code Name Generator

Viole is a Python library that generates random code names using a combination of letters and numbers. It provides flexibility in generating code names with different patterns and components.

## 1. Installation

You can install Viole via pip: `pip install VioleRCNG` 

## 2. Usage
`import viole_rcng`

## 3. Generate a code name with default settings

    code_name = viole_rcng.gencode()
    print(code_name)

## 4. Generate a code name with custom settings

    code_name = viole_rcng.gencode(name='Custom_Name', factor=5, lu=True, ul=True, separator='-')
    print(code_name)` 

## 5. Parameters

| Parameter  | Description                                          | Default Value |
|------------|------------------------------------------------------|---------------|
| `name`     | The base name to be included in the code name       | 'ReNN_Viole_rCNg' |
| `factor`   | The factor determining the length of the unique code part (the unique code is always the factor*4)| 3 |
| `lu`       | Include the LU (Lowercase-Uppercase) code part      | `True` |
| `ul`       | Include the UL (Uppercase-Lowercase) code part      | `True` |
| `separator`| The separator character between code name components| '_' |

## 6. Examples

Check out the [GitHub repository](https://github.com/horue/Viole-Random-Code-Name-Generator) for usage examples and more information.

## 7. License

Viole is licensed under the MIT License. You are free to use and modify this software for any purpose.

## 8. About

This project is maintained by [horue](https://github.com/horue). Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.
