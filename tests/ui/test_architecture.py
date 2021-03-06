#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

"""
Test class for Architecture UI
"""

from robottelo.common.helpers import generate_name
from robottelo.common.helpers import generate_string
from tests.ui.baseui import BaseUI


class Architecture(BaseUI):

    def create_os(self, os_name=None, major_version=None,):
        os_name = os_name or generate_name(6)
        major_version = major_version or generate_string('numeric', 1)
        self.navigator.go_to_operating_systems()  # go to operating system page
        self.operatingsys.create(os_name, major_version)

    def test_create_arch(self):
        "Create new Arch"
        name = generate_name(4)
        os_name = generate_name(6)
        major_version = generate_string('numeric', 1)
        self.login.login(self.katello_user, self.katello_passwd)  # login
        self.create_os(os_name, major_version)  # create os
        self.navigator.go_to_architectures()  # go to architecture page
        self.architecture.create(name, os_name)
        self.assertTrue(self, self.architecture.search(name))

    def test_remove_arch(self):
        "Delete Arch"
        name = generate_name(4)
        os_name = generate_name(6)
        major_version = generate_string('numeric', 1)
        self.login.login(self.katello_user, self.katello_passwd)  # login
        self.create_os(os_name, major_version)
        self.navigator.go_to_architectures()  # go to architecture page
        self.architecture.create(name, os_name)
        self.architecture.remove(name, True)

    def test_update_arch(self):
        "Update arch with new arch-name and new OS"
        oldname = generate_name(6)
        newname = generate_name(4)
        new_osname = generate_name(6)
        major_version = generate_string('numeric', 1)
        self.login.login(self.katello_user, self.katello_passwd)  # login
        self.create_os(new_osname, major_version)
        self.navigator.go_to_architectures()  # go to architecture page
        self.architecture.create(oldname)
        self.architecture.update(oldname, newname, new_osname)
        self.assertTrue(self, self.architecture.search(newname))
