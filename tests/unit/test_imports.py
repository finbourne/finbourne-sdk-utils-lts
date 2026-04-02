import unittest


class TestTopLevelImports(unittest.TestCase):
    """Test that the top-level package imports all subpackages."""

    def test_import_finbourne_sdk_utils(self):
        import finbourne_sdk_utils
        self.assertTrue(hasattr(finbourne_sdk_utils, "cocoon"))

    def test_import_cocoon_subpackage(self):
        import finbourne_sdk_utils.cocoon
        self.assertIsNotNone(finbourne_sdk_utils.cocoon)

    def test_import_extract_subpackage(self):
        import finbourne_sdk_utils.extract
        self.assertIsNotNone(finbourne_sdk_utils.extract)

    def test_import_iam_subpackage(self):
        import finbourne_sdk_utils.iam
        self.assertIsNotNone(finbourne_sdk_utils.iam)

    def test_import_jupyter_tools_subpackage(self):
        import finbourne_sdk_utils.jupyter_tools
        self.assertIsNotNone(finbourne_sdk_utils.jupyter_tools)

    def test_import_logger_subpackage(self):
        import finbourne_sdk_utils.logger
        self.assertIsNotNone(finbourne_sdk_utils.logger)

    def test_import_lpt_subpackage(self):
        import finbourne_sdk_utils.lpt
        self.assertIsNotNone(finbourne_sdk_utils.lpt)

    def test_import_pandas_utils_subpackage(self):
        import finbourne_sdk_utils.pandas_utils
        self.assertIsNotNone(finbourne_sdk_utils.pandas_utils)


class TestCocoonInitImports(unittest.TestCase):
    """Test that cocoon/__init__.py exports all expected names."""

    def test_import_load_from_data_frame(self):
        from finbourne_sdk_utils.cocoon import load_from_data_frame
        self.assertTrue(callable(load_from_data_frame))

    def test_import_resolve_instruments(self):
        from finbourne_sdk_utils.cocoon import resolve_instruments
        self.assertTrue(callable(resolve_instruments))

    def test_import_create_property_values(self):
        from finbourne_sdk_utils.cocoon import create_property_values
        self.assertTrue(callable(create_property_values))

    def test_import_set_attributes_recursive(self):
        from finbourne_sdk_utils.cocoon import set_attributes_recursive
        self.assertTrue(callable(set_attributes_recursive))

    def test_import_checkargs(self):
        from finbourne_sdk_utils.cocoon import checkargs
        self.assertTrue(callable(checkargs))

    def test_import_load_data_to_df_and_detect_delimiter(self):
        from finbourne_sdk_utils.cocoon import load_data_to_df_and_detect_delimiter
        self.assertTrue(callable(load_data_to_df_and_detect_delimiter))

    def test_import_check_mapping_fields_exist(self):
        from finbourne_sdk_utils.cocoon import check_mapping_fields_exist
        self.assertTrue(callable(check_mapping_fields_exist))

    def test_import_parse_args(self):
        from finbourne_sdk_utils.cocoon import parse_args
        self.assertTrue(callable(parse_args))

    def test_import_identify_cash_items(self):
        from finbourne_sdk_utils.cocoon import identify_cash_items
        self.assertTrue(callable(identify_cash_items))

    def test_import_validate_mapping_file_structure(self):
        from finbourne_sdk_utils.cocoon import validate_mapping_file_structure
        self.assertTrue(callable(validate_mapping_file_structure))

    def test_import_get_delimiter(self):
        from finbourne_sdk_utils.cocoon import get_delimiter
        self.assertTrue(callable(get_delimiter))

    def test_import_scale_quote_of_type(self):
        from finbourne_sdk_utils.cocoon import scale_quote_of_type
        self.assertTrue(callable(scale_quote_of_type))

    def test_import_strip_whitespace(self):
        from finbourne_sdk_utils.cocoon import strip_whitespace
        self.assertTrue(callable(strip_whitespace))

    def test_import_load_json_file(self):
        from finbourne_sdk_utils.cocoon import load_json_file
        self.assertTrue(callable(load_json_file))

    def test_import_default_fx_forward_model(self):
        from finbourne_sdk_utils.cocoon import default_fx_forward_model
        self.assertTrue(callable(default_fx_forward_model))

    def test_import_format_holdings_response(self):
        from finbourne_sdk_utils.cocoon import format_holdings_response
        self.assertTrue(callable(format_holdings_response))

    def test_import_format_instruments_response(self):
        from finbourne_sdk_utils.cocoon import format_instruments_response
        self.assertTrue(callable(format_instruments_response))

    def test_import_format_portfolios_response(self):
        from finbourne_sdk_utils.cocoon import format_portfolios_response
        self.assertTrue(callable(format_portfolios_response))

    def test_import_format_quotes_response(self):
        from finbourne_sdk_utils.cocoon import format_quotes_response
        self.assertTrue(callable(format_quotes_response))

    def test_import_format_transactions_response(self):
        from finbourne_sdk_utils.cocoon import format_transactions_response
        self.assertTrue(callable(format_transactions_response))

    def test_import_seed_data(self):
        from finbourne_sdk_utils.cocoon import seed_data
        self.assertTrue(callable(seed_data))

    def test_import_cocoon_module(self):
        from finbourne_sdk_utils.cocoon import cocoon
        self.assertIsNotNone(cocoon)

    def test_import_instruments_module(self):
        from finbourne_sdk_utils.cocoon import instruments
        self.assertIsNotNone(instruments)

    def test_import_properties_module(self):
        from finbourne_sdk_utils.cocoon import properties
        self.assertIsNotNone(properties)

    def test_import_systemConfiguration_module(self):
        from finbourne_sdk_utils.cocoon import systemConfiguration
        self.assertIsNotNone(systemConfiguration)

    def test_import_utilities_module(self):
        from finbourne_sdk_utils.cocoon import utilities
        self.assertIsNotNone(utilities)

    def test_import_async_tools_module(self):
        from finbourne_sdk_utils.cocoon import async_tools
        self.assertIsNotNone(async_tools)

    def test_import_validator_module(self):
        from finbourne_sdk_utils.cocoon import validator
        self.assertIsNotNone(validator)

    def test_import_dateorcutlabel_module(self):
        from finbourne_sdk_utils.cocoon import dateorcutlabel
        self.assertIsNotNone(dateorcutlabel)

    def test_import_transaction_type_upload_module(self):
        from finbourne_sdk_utils.cocoon import transaction_type_upload
        self.assertIsNotNone(transaction_type_upload)

    def test_import_create_transaction_type_configuration(self):
        from finbourne_sdk_utils.cocoon.transaction_type_upload import create_transaction_type_configuration
        self.assertTrue(callable(create_transaction_type_configuration))

    def test_import_upsert_transaction_type_alias(self):
        from finbourne_sdk_utils.cocoon.transaction_type_upload import upsert_transaction_type_alias
        self.assertTrue(callable(upsert_transaction_type_alias))


class TestExtractInitImports(unittest.TestCase):
    """Test that extract/__init__.py exports expected names."""

    def test_import_get_holdings_for_group(self):
        from finbourne_sdk_utils.extract import get_holdings_for_group
        self.assertTrue(callable(get_holdings_for_group))


class TestIamInitImports(unittest.TestCase):
    """Test that iam/__init__.py exports expected names."""

    def test_import_roles_module(self):
        from finbourne_sdk_utils.iam import roles
        self.assertIsNotNone(roles)

    def test_import_create_role(self):
        from finbourne_sdk_utils.iam.roles import create_role
        self.assertTrue(callable(create_role))


class TestJupyterToolsInitImports(unittest.TestCase):
    """Test that jupyter_tools/__init__.py exports expected names."""

    def test_import_StopExecution(self):
        from finbourne_sdk_utils.jupyter_tools import StopExecution
        self.assertTrue(isinstance(StopExecution, type))

    def test_import_toggle_code(self):
        from finbourne_sdk_utils.jupyter_tools import toggle_code
        self.assertTrue(callable(toggle_code))


class TestLoggerInitImports(unittest.TestCase):
    """Test that logger/__init__.py exports expected names."""

    def test_import_LusidLogger(self):
        from finbourne_sdk_utils.logger import LusidLogger
        self.assertTrue(isinstance(LusidLogger, type))


class TestLptInitImports(unittest.TestCase):
    """Test that lpt/__init__.py exports expected module attributes."""

    def test_import_lpt_module(self):
        from finbourne_sdk_utils.lpt import lpt
        self.assertIsNotNone(lpt)

    def test_import_either_module(self):
        from finbourne_sdk_utils.lpt import either
        self.assertIsNotNone(either)

    def test_import_stdargs_module(self):
        from finbourne_sdk_utils.lpt import stdargs
        self.assertIsNotNone(stdargs)

    def test_import_record_module(self):
        from finbourne_sdk_utils.lpt import record
        self.assertIsNotNone(record)

    def test_import_pager_module(self):
        from finbourne_sdk_utils.lpt import pager
        self.assertIsNotNone(pager)

    def test_import_refreshing_token_module(self):
        from finbourne_sdk_utils.lpt import refreshing_token
        self.assertIsNotNone(refreshing_token)

    def test_import_connect_lusid_module(self):
        from finbourne_sdk_utils.lpt import connect_lusid
        self.assertIsNotNone(connect_lusid)

    def test_import_dfq_module(self):
        from finbourne_sdk_utils.lpt import dfq
        self.assertIsNotNone(dfq)

    def test_import_lse_module(self):
        from finbourne_sdk_utils.lpt import lse
        self.assertIsNotNone(lse)


class TestPandasUtilsInitImports(unittest.TestCase):
    """Test that pandas_utils/__init__.py exports expected names."""

    def test_import_lusid_response_to_data_frame(self):
        from finbourne_sdk_utils.pandas_utils import lusid_response_to_data_frame
        self.assertTrue(callable(lusid_response_to_data_frame))


if __name__ == "__main__":
    unittest.main()
