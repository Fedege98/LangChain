from langchain.document_loaders import AzureBlobStorageContainerLoader, GCSFileLoader, NotionDBLoader
from langchain.document_loaders import AzureBlobStorageFileLoader
from langchain.document_loaders import BigQueryLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import DataFrameLoader
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
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
from getpass import getpass

'''this class structures documents so that LLMs can best interact with them. This module contains utility 
functions for working with documents, different types of indexes, and then examples for using those indexes in chains.'''


class DataLoader:
    global loader

    def AzureBlobStorageContainer(self, conn_str, container):
        loader = AzureBlobStorageContainerLoader(conn_str, container)
        return loader.load()

    def AzureBlobStorageFileLoad(self, conn_str, container, blob_name):
        loader = AzureBlobStorageFileLoader(conn_str, container, blob_name)
        return loader.load()

    def BigQueryLoad(self, BASE_QUERY):
        loader = BigQueryLoader(BASE_QUERY)
        return loader.load()

    def CSVLoad(self, file_path):
        loader = CSVLoader(file_path)
        return loader.load()

    def DataFrameLoad(self, df, page_content_column):
        loader = DataFrameLoader(df, page_content_column)
        return loader.load()

    def DirectoryLoad(self, path, which_file_end_string):
        loader = DirectoryLoader(path, which_file_end_string, loader_cls=TextLoader)
        return loader.load()

    def GCSDirloader(self, project_name, bucket):
        loader = GCSDirectoryLoader(project_name, bucket)
        return loader.load()

    def GCSFileload(self, project_name, bucket, blob):
        loader = GCSFileLoader(project_name, bucket, blob)
        return loader.load()

    def GoogleDrive(self, folder_id):
        loader = GoogleDriveLoader(folder_id)
        loader.load()

    def UnstructuredImageload(self, image):
        loader = UnstructuredImageLoader(image)
        return loader.load()[0]

    def UnstructuredMarkdownLoad(self, path):
        loader = UnstructuredMarkdownLoader(path)
        return loader.load()

    def NotionDirLoad(self, name_dir):
        loader = NotionDirectoryLoader(name_dir)
        return loader.load()

    def NotionDBload(self, NOTION_TOKEN, DATABASE_ID):
        loader = NotionDBLoader(NOTION_TOKEN, DATABASE_ID)
        return loader.load()

    def PyPDFLoad(self, path):
        loader = PyPDFLoader(path)
        return loader.load_and_split()

    def powerpointload(self, pptx):
        loader = UnstructuredPowerPointLoader(pptx)
        return loader.load()

    def documentation(self, root_html_scraped):
        loader = ReadTheDocsLoader(root_html_scraped)
        return loader.load()

    def URLloader(self, urls):
        loader = UnstructuredURLLoader(urls=urls)
        return loader.load()

    def Seleniumurloader(self, urls):
        loader = SeleniumURLLoader(urls=urls)
        return loader.load()

    def UnstructuredWord(self, path):
        loader = UnstructuredWordDocumentLoader(path)
        return loader.load()

    def Youtubeloader(self, link):
        loader = YoutubeLoader.from_youtube_channel(link, add_video_info=True)
        return loader.load()
