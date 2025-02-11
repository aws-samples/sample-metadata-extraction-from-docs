# Metadata Schema Extraction using Foundation Models on Amazon Bedrock

This project demonstrates how to extract structured metadata from documents using Foundation Models (FMs) available through Amazon Bedrock. The system processes various document formats and generates metadata based on custom schemas.

## Overview

The solution enables users to:
- Process multiple document formats (`PDF`, `DOCX`, etc.)
- Use different Foundation Models available on Amazon Bedrock (Anthropic, Amazon Nova, Llama, etc.)
- Apply custom metadata schemas
- Use different prompt templates for different models
- Generate structured metadata output

## Prerequisites & Environment Setup

### Python Environment Setup

Ensure to run this solution in a  `python3.11` virtual environment. The notebooks that are run as a part of this solution install the required packages given in the [`requirements.txt`](requirements.txt) file.

### Data Files Configuration

To use your custom data or any open source data, add a `URL`, `PDF`, or `DOCX` file in your configuration. For example, update your configuration file with the follows:

``` {.bash}
# These files can either be PDF/Docx files or they can
  # be public urls that the solution gets and uses to extract metadata from
  data_files:
  - https://docs.aws.amazon.com/pdfs/whitepapers/latest/ml-best-practices-healthcare-life-sciences/ml-best-practices-healthcare-life-sciences.pdf#ml-best-practices-healthcare-life-sciences
```

### Custom metadata schema

To use your custom metadata schema, provide your template in the [`config.yaml`](config.yaml) file. All the metadata will be extracted in this format. View an example below:

```{.bash}
# Enter the metadata schema you would like your metadata to be extracted in.
# This can be your custom metadata that the model on Bedrock will use to generate
# metadata from documents.
metadata_schema: | 
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "description": "PDF Document Analysis Schema",
      "type": "object",
      "properties": {
        "document_metadata": {
          "type": "object",
          "inferenceType": "extractive",
          "properties": {
            "title": {
              "type": "string",
              "description": "Title of the PDF document\n"
            },
            "author": {
              "type": "string",
              "description": "Author of the document\n"
            },
            "creation_date": {
              "type": "string",
              "description": "Date when the document was created\n"
            }
            .
            .
            .
            .
          }
        }
      }
    }
```

### Custom prompt templates

To use your custom prompt templates and instructions for the model to follow, you can change the existing prompt templates in the [`prompt_template`](prompt_template) directory. The current prompt template directory contains prompts for Anthropic and Amazon Nova models but can be extended based on your use case.

## Project Structure
```
├── data/ # Source documents (PDF, DOCX, HTTP/HTTPS URLs etc.) 
├── prompt_template/ # Model-specific prompt templates 
├── results/ # Output directory for extraction results 
├── config.yaml # Configuration file 
└── README.md
```


## Configuration

### Directory Configuration
Configure the following in `config.yaml`:
- `source_dir`: Directory containing source documents
- `results_dir`: Directory for storing extraction results
- `prompt_template_dir`: Directory containing model-specific prompts

## Steps to run

1. [`0_schema_extraction_using_Amazon_Bedrock.ipynb`](0_schema_extraction_using_Amazon_Bedrock.ipynb): This notebook refers to the data provided in the `data` directory and the metadata schema provided in the [`config.yaml`](config.yaml) file to extract metadata from each document. The prompt that is used to extract metadata from the document is provided in the `prompt_templates` directory. This prompt uses the document and the metadata schema provided by the user to extract relevant data from the documents. This notebook can be used with custom metadata schemas and prompts, giving users full control and flexibility into metadata extraction from their documents.

1. [`1_perform_analysis_on_metadata_evaluation.ipynb`](1_perform_analysis_on_metadata_evaluation.ipynb): This notebook iterates through each model completion and stores the schema in `JSON` files in the [`results`](results) directory for further analysis.

## Results

Once you run the solution, you will see a `schema_extracted` directory which will contain metadata extracted from each document provided in the config file. A human in the loop can then be used to check for the accuracy of these responses. View an example below:

``` {.json}
{
  "document_metadata": {
    "title": "Machine Learning Best Practices in Healthcare and Life Sciences",
    "author": "Sai Sharanya Nalla, Wajahat Aziz, Kartik Kannapur, Ujjwal Ratan, Garin Kessler, Ian Sutcliffe",
    "creation_date": "November 22, 2021",
    "last_modified": "November 22, 2021",
    "page_count": 42,
    "file_size": "no"
  },
  .
  .
  .
}
```