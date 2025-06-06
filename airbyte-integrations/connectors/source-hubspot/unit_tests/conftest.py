#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import pytest
from source_hubspot.source import SourceHubspot
from source_hubspot.streams import API

from airbyte_cdk.test.catalog_builder import CatalogBuilder
from airbyte_cdk.test.entrypoint_wrapper import EntrypointOutput, read


NUMBER_OF_PROPERTIES = 2000
OBJECTS_WITH_DYNAMIC_SCHEMA = [
    "calls",
    "company",
    "deal",
    "emails",
    "form",
    "goal_targets",
    "line_item",
    "meetings",
    "notes",
    "tasks",
    "product",
]


@pytest.fixture(name="oauth_config")
def oauth_config_fixture():
    return {
        "start_date": "2021-10-10T00:00:00Z",
        "credentials": {
            "credentials_title": "OAuth Credentials",
            "redirect_uri": "https://airbyte.io",
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "refresh_token": "test_refresh_token",
            "access_token": "test_access_token",
            "token_expires": "2021-05-30T06:00:00Z",
        },
    }


@pytest.fixture(name="common_params")
def common_params_fixture(config):
    source = SourceHubspot(config, None, None)
    common_params = source.get_common_params(config=config)
    return common_params


@pytest.fixture(name="config_invalid_client_id")
def config_invalid_client_id_fixture():
    return {
        "start_date": "2021-01-10T00:00:00Z",
        "credentials": {
            "credentials_title": "OAuth Credentials",
            "client_id": "invalid_client_id",
            "client_secret": "invalid_client_secret",
            "access_token": "test_access_token",
            "refresh_token": "test_refresh_token",
        },
    }


@pytest.fixture(name="config")
def config_fixture():
    return {
        "start_date": "2021-01-10T00:00:00Z",
        "credentials": {"credentials_title": "Private App Credentials", "access_token": "test_access_token"},
        "enable_experimental_streams": False,
    }


@pytest.fixture(name="config_experimental")
def config_eperimantal_fixture():
    return {
        "start_date": "2021-01-10T00:00:00Z",
        "credentials": {"credentials_title": "Private App Credentials", "access_token": "test_access_token"},
        "enable_experimental_streams": True,
    }


@pytest.fixture(name="config_invalid_date")
def config_invalid_date_fixture():
    return {
        "start_date": "2000-00-00T00:00:00Z",
        "credentials": {"credentials_title": "Private App Credentials", "access_token": "test_access_token"},
    }


@pytest.fixture(name="some_credentials")
def some_credentials_fixture():
    return {"credentials_title": "Private App Credentials", "access_token": "wrong token"}


@pytest.fixture(name="fake_properties_list")
def fake_properties_list():
    return [f"property_number_{i}" for i in range(NUMBER_OF_PROPERTIES)]


@pytest.fixture(name="migrated_properties_list")
def migrated_properties_list():
    return [
        "hs_v2_date_entered_prospect",
        "hs_v2_date_exited_prospect",
        "hs_v2_cumulative_time_in_prsopect",
        "hs_v2_some_other_property_in_prospect",
    ]


@pytest.fixture(name="api")
def api(some_credentials):
    return API(some_credentials)


@pytest.fixture
def http_mocker():
    return None


def find_stream(stream_name, config):
    for stream in SourceHubspot(config=config, catalog=None, state=None).streams(config=config):
        if stream.name == stream_name:
            return stream
    raise ValueError(f"Stream {stream_name} not found")


@pytest.fixture(autouse=True)
def patch_time(mocker):
    mocker.patch("time.sleep")


def read_from_stream(cfg, stream: str, sync_mode, state=None, expecting_exception: bool = False) -> EntrypointOutput:
    return read(SourceHubspot(cfg, None, None), cfg, CatalogBuilder().with_stream(stream, sync_mode).build(), state, expecting_exception)


@pytest.fixture()
def mock_dynamic_schema_requests(requests_mock):
    for entity in OBJECTS_WITH_DYNAMIC_SCHEMA:
        requests_mock.get(
            f"https://api.hubapi.com/properties/v2/{entity}/properties",
            json=[
                {
                    "name": "hs__migration_soft_delete",
                    "label": "migration_soft_delete_deprecated",
                    "description": "Describes if the goal target can be treated as deleted.",
                    "groupName": "goal_target_information",
                    "type": "enumeration",
                }
            ],
            status_code=200,
        )


def mock_dynamic_schema_requests_with_skip(requests_mock, object_to_skip: list):
    for object_name in OBJECTS_WITH_DYNAMIC_SCHEMA:
        if object_name in object_to_skip:
            continue
        requests_mock.get(
            f"https://api.hubapi.com/properties/v2/{object_name}/properties",
            json=[{"name": "hs__test_field", "type": "enumeration"}],
            status_code=200,
        )
