# Global variables to get the region information 
EC2_API_TOKEN_URL: str = "http://169.254.169.254/latest/api/token"
EC2_METADATA_REGION_URL: str = "http://169.254.169.254/latest/meta-data/placement/region"
GET_REGION_TIMEOUT: int = 2

# Global retry logic variables while invoking models on Amazon Bedrock
INITIAL_RETRY_DELAY: float = 1
MAX_RETRY_DELAY: float = 60

# Global variables used in model invocation while passing in different documents
PDF_EXT: str = '.pdf'
DOC_EXT: str = '.doc'
DOCX_EXT: str = '.docx'
HTTP_PREFIX: str = 'http://'
HTTPS_PREFIX: str = 'https://'