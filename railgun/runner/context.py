#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/runner/context.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from celery import Celery
from celery.utils.log import get_task_logger

from . import runconfig, permcheck


app = Celery('railgun.runner')
app.config_from_object(runconfig)

# the default logger for this package
logger = get_task_logger(__name__)

# check permissions if RUNNER_CHECK_PERM is enabled
if runconfig.RUNNER_CHECK_PERM:
    permcheck.checker.execute(logger)
