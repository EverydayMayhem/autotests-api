import pytest

from pydantic import BaseModel

from clients.files.files_model import CreateFileRequestSchema,CreateFileResponseSchema
from clients.files.files_client import get_files_client, FilesClient
from fixtures.users import UserFixture

class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

    @property
    def file_id(self):
        return self.response.file.id

@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)

@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file='./testdata/files/cat.jpg')
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)