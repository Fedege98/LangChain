from langchain.document_loaders import AzureBlobStorageContainerLoader
from langchain.document_loaders import AzureBlobStorageFileLoader
from langchain.document_loaders import BigQueryLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import DataFrameLoader
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import GCSDirectoryLoader
from langchain.document_loaders import GoogleDriveLoader
from langchain.document_loaders.image import UnstructuredImageLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import NotionDirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import UnstructuredPowerPointLoader
from langchain.document_loaders import ReadTheDocsLoader
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import SeleniumURLLoader
from langchain.document_loaders import UnstructuredWordDocumentLoader
from langchain.document_loaders import YoutubeLoader

'''this class structures documents so that LLMs can best interact with them. This module contains utility 
functions for working with documents, different types of indexes, and then examples for using those indexes in chains.'''


class DataLoader:
    pass
