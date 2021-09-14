# -*- coding: utf-8 -*-

# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import os
import mock
import unittest2

import st2tests

from st2common.services.packs import delete_action_files_from_pack
from st2common.services.packs import clone_action

TEST_PACK = "dummy_pack_1"
TEST_PACK_PATH = os.path.join(
    st2tests.fixturesloader.get_fixtures_packs_base_path(), TEST_PACK
)

TEST_SOURCE_PACK = "core"
TEST_SOURCE_PACK_PATH = os.path.join(
    st2tests.fixturesloader.get_fixtures_packs_base_path(), TEST_SOURCE_PACK
)

TEST_SOURCE_WORKFLOW_PACK = "orquesta_tests"
TEST_SOURCE_WORKFLOW_PACK_PATH = os.path.join(
    st2tests.fixturesloader.get_fixtures_packs_base_path(), TEST_SOURCE_WORKFLOW_PACK
)

TEST_DEST_PACK = "dummy_pack_23"
TEST_DEST_PACK_PATH = os.path.join(
    st2tests.fixturesloader.get_fixtures_packs_base_path(), TEST_DEST_PACK
)


class DeleteActionFilesTest(unittest2.TestCase):
    def test_delete_action_files_from_pack(self):
        """
        Test that the action files present in the pack and removed
        on the call of delete_action_files_from_pack function.
        """

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        # creating entry_point file in dummy pack
        with open(entry_point, "w") as f:
            f.write("# entry point file to be removed")

        # creating metadata file in dummy pack
        with open(metadata_file, "w") as f:
            f.write("# metadata file to be removed")

        # asserting both entry_point and metadata files exists
        self.assertTrue(os.path.exists(entry_point))
        self.assertTrue(os.path.exists(metadata_file))

        delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)

        # asserting both entry_point and metadata files removed and they doesn't exist
        self.assertFalse(os.path.exists(entry_point))
        self.assertFalse(os.path.exists(metadata_file))

    def test_entry_point_file_does_not_exists(self):
        """
        Tests that entry_point file doesn't exists at the path and if action delete
        api calls delete_action_files_from_pack function, it doesn't affect.
        """

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        # creating only metadata file in dummy pack
        with open(metadata_file, "w") as f:
            f.write("# metadata file to be removed")

        # asserting entry_point file doesn't exist
        self.assertFalse(os.path.exists(entry_point))

        # asserting metadata files exists
        self.assertTrue(os.path.exists(metadata_file))

        delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)

        # asserting both entry_point and metadata files don't exist
        self.assertFalse(os.path.exists(entry_point))
        self.assertFalse(os.path.exists(metadata_file))

    def test_metadata_file_does_not_exists(self):
        """
        Tests that metadata file doesn't exists at the path and if action delete
        api calls delete_action_files_from_pack function, it doesn't affect.
        """

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        # creating only entry_point file in dummy pack
        with open(entry_point, "w") as f:
            f.write("# entry point file to be removed")

        # asserting metadata file doesn't exist
        self.assertFalse(os.path.exists(metadata_file))

        # asserting entry_point file exists
        self.assertTrue(os.path.exists(entry_point))

        delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)

        # asserting both entry_point and metadata files don't exist
        self.assertFalse(os.path.exists(entry_point))
        self.assertFalse(os.path.exists(metadata_file))


class DeleteActionEntryPointFilesErrorTest(unittest2.TestCase):
    """
    Testing that exceptions are thrown by delete_action_files_from_pack function
    for entry point file. Here only entry point file is created and metadata
    file doesn't exist.
    """

    def setUp(self):
        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")

        # creating entry_point file in dummy pack
        with open(entry_point, "w") as f:
            f.write("# entry point file to be removed")

    def tearDown(self):
        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")

        # removing entry_point file from dummy pack
        os.remove(entry_point)

    @mock.patch.object(os, "remove")
    def test_permission_error_to_remove_resource_entry_point_file(self, remove):

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        remove.side_effect = PermissionError("No permission to delete file from disk")

        # asserting entry_point file exists
        self.assertTrue(os.path.exists(entry_point))

        # asserting metadata file doesn't exist
        self.assertFalse(os.path.exists(metadata_file))

        expected_msg = 'No permission to delete "%s" file from disk' % (entry_point)

        # asserting PermissionError with message on call of delete_action_files_from_pack
        # to delete entry_point file
        with self.assertRaisesRegexp(PermissionError, expected_msg):
            delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)

    @mock.patch.object(os, "remove")
    def test_exception_to_remove_resource_entry_point_file(self, remove):

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        remove.side_effect = Exception("Another exception occured")

        # asserting entry_point file exists
        self.assertTrue(os.path.exists(entry_point))

        # asserting metadata file doesn't exist
        self.assertFalse(os.path.exists(metadata_file))

        expected_msg = (
            'The action file "%s" could not be removed from disk, please '
            "check the logs or ask your StackStorm administrator to check "
            "and delete the actions files manually" % (entry_point)
        )

        # asserting exception with message on call of delete_action_files_from_pack
        # to delete entry_point file
        with self.assertRaisesRegexp(Exception, expected_msg):
            delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)


class DeleteActionMetadataFilesErrorTest(unittest2.TestCase):
    """
    Testing that exceptions are thrown by delete_action_files_from_pack function for
    metadata file. Here only metadata file is created and metadata file doesn't exist.
    """

    def setUp(self):
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        # creating metadata file in dummy pack
        with open(metadata_file, "w") as f:
            f.write("# metadata file to be removed")

    def tearDown(self):
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        # removing metadata file from dummy pack
        os.remove(metadata_file)

    @mock.patch.object(os, "remove")
    def test_permission_error_to_remove_resource_metadata_file(self, remove):

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        remove.side_effect = PermissionError("No permission to delete file from disk")

        # asserting metadata file exists
        self.assertTrue(os.path.exists(metadata_file))

        # asserting entry_point file doesn't exist
        self.assertFalse(os.path.exists(entry_point))

        expected_msg = 'No permission to delete "%s" file from disk' % (metadata_file)

        # asserting PermissionError with message on call of delete_action_files_from_pack
        # to delete metadata file
        with self.assertRaisesRegexp(PermissionError, expected_msg):
            delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)

    @mock.patch.object(os, "remove")
    def test_exception_to_remove_resource_metadata_file(self, remove):

        entry_point = os.path.join(TEST_PACK_PATH, "actions", "test_entry_point.py")
        metadata_file = os.path.join(TEST_PACK_PATH, "actions", "test_metadata.yaml")

        remove.side_effect = Exception("Another exception occured")

        # asserting metadata file exists
        self.assertTrue(os.path.exists(metadata_file))

        # asserting entry_point file doesn't exist
        self.assertFalse(os.path.exists(entry_point))

        expected_msg = (
            'The action file "%s" could not be removed from disk, please '
            "check the logs or ask your StackStorm administrator to check "
            "and delete the actions files manually" % (metadata_file)
        )

        # asserting exception with message on call of delete_action_files_from_pack
        # to delete metadata file
        with self.assertRaisesRegexp(Exception, expected_msg):
            delete_action_files_from_pack(TEST_PACK, entry_point, metadata_file)


class CloneActionsTest(unittest2.TestCase):
    @classmethod
    def tearDownClass(cls):
        action_files_path = os.path.join(TEST_DEST_PACK_PATH, "actions")
        workflow_files_path = os.path.join(action_files_path, "workflows")
        for file in os.listdir(action_files_path):
            if os.path.isfile(os.path.join(action_files_path, file)):
                os.remove(os.path.join(action_files_path, file))
        for file in os.listdir(workflow_files_path):
            if os.path.isfile(os.path.join(workflow_files_path, file)):
                os.remove(os.path.join(workflow_files_path, file))

    def test_clone_action_with_python_script_runner(self):
        clone_action(
            TEST_SOURCE_PACK_PATH,
            "actions/inject_trigger.yaml",
            "inject_trigger.py",
            "python-script",
            TEST_DEST_PACK_PATH,
            TEST_DEST_PACK,
            "action_1",
        )
        cloned_action_metadata_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_1.yaml"
        )
        cloned_action_entry_point_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_1.py"
        )
        self.assertTrue(os.path.exists(cloned_action_metadata_file_path))
        self.assertTrue(os.path.exists(cloned_action_entry_point_file_path))

    def test_clone_action_with_shell_script_runner(self):
        clone_action(
            TEST_SOURCE_PACK_PATH,
            "actions/sendmail.yaml",
            "send_mail/send_mail",
            "local-shell-script",
            TEST_DEST_PACK_PATH,
            TEST_DEST_PACK,
            "action_2",
        )
        cloned_action_metadata_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_2.yaml"
        )
        cloned_action_entry_point_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_2"
        )
        self.assertTrue(os.path.exists(cloned_action_metadata_file_path))
        self.assertTrue(os.path.exists(cloned_action_entry_point_file_path))

    def test_clone_action_with_local_shell_cmd_runner(self):
        clone_action(
            TEST_SOURCE_PACK_PATH,
            "actions/echo.yaml",
            "",
            "local-shell-cmd",
            TEST_DEST_PACK_PATH,
            TEST_DEST_PACK,
            "action_3",
        )
        cloned_action_metadata_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_3.yaml"
        )
        self.assertTrue(os.path.exists(cloned_action_metadata_file_path))

    def test_clone_workflow(self):
        clone_action(
            TEST_SOURCE_WORKFLOW_PACK_PATH,
            "actions/data-flow.yaml",
            "workflows/data-flow.yaml",
            "orquesta",
            TEST_DEST_PACK_PATH,
            TEST_DEST_PACK,
            "workflow_1",
        )
        cloned_workflow_metadata_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "workflow_1.yaml"
        )
        cloned_workflow_entry_point_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "workflows", "workflow_1.yaml"
        )
        self.assertTrue(os.path.exists(cloned_workflow_metadata_file_path))
        self.assertTrue(os.path.exists(cloned_workflow_entry_point_file_path))

    @mock.patch("shutil.copy")
    def test_permission_error_to_write_in_destination_file(self, mock_copy):
        mock_copy.side_effect = PermissionError("No permission to write in file")
        cloned_action_entry_point_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_4.py"
        )
        expected_msg = 'No permission to write in "%s" file' % (
            cloned_action_entry_point_file_path
        )

        with self.assertRaisesRegexp(PermissionError, expected_msg):
            clone_action(
                TEST_SOURCE_PACK_PATH,
                "actions/inject_trigger.yaml",
                "inject_trigger.py",
                "python-script",
                TEST_DEST_PACK_PATH,
                TEST_DEST_PACK,
                "action_4",
            )

    @mock.patch("shutil.copy")
    def test_file_not_found_error_for_destination_file(self, mock_copy):
        mock_copy.side_effect = FileNotFoundError("No such file or directory")
        cloned_action_entry_point_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_5.py"
        )
        expected_msg = (
            "Please make sure 'workflows' directory present in path: '%s'"
            % (cloned_action_entry_point_file_path)
        )

        with self.assertRaisesRegexp(FileNotFoundError, expected_msg):
            clone_action(
                TEST_SOURCE_PACK_PATH,
                "actions/inject_trigger.yaml",
                "inject_trigger.py",
                "python-script",
                TEST_DEST_PACK_PATH,
                TEST_DEST_PACK,
                "action_5",
            )

    @mock.patch("shutil.copy")
    def test_exceptions_to_write_in_destination_file(self, mock_copy):
        mock_copy.side_effect = Exception(
            "Exception encoutntered during writing in destination action file"
        )
        cloned_action_metadata_file_path = os.path.join(
            TEST_DEST_PACK_PATH, "actions", "action_6.yaml"
        )
        expected_msg = (
            'Could not copy to "%s" file, please check the logs or ask your '
            "StackStorm administrator to check and clone the actions files manually"
            % cloned_action_metadata_file_path
        )

        with self.assertRaisesRegexp(Exception, expected_msg):
            clone_action(
                TEST_SOURCE_PACK_PATH,
                "actions/echo.yaml",
                "",
                "local-shell-cmd",
                TEST_DEST_PACK_PATH,
                TEST_DEST_PACK,
                "action_6",
            )
