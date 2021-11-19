"""This module implements the OptimizationParameters entity."""
# INTEL CONFIDENTIAL
#
# Copyright (C) 2021 Intel Corporation
#
# This software and the related documents are Intel copyrighted materials, and
# your use of them is governed by the express license under which they were provided to
# you ("License"). Unless the License provides otherwise, you may not use, modify, copy,
# publish, distribute, disclose or transmit this software or the related documents
# without Intel's prior written permission.
#
# This software and the related documents are provided as is,
# with no express or implied warranties, other than those that are expressly stated
# in the License.

from dataclasses import dataclass
from typing import Callable


def default_progress_callback(_: int):
    """
    This is the default progress callback for OptimizationParameters.
    """


def default_save_model_callback():
    """
    This is the default save model callback for OptimizationParameters.
    """


@dataclass
class OptimizationParameters:
    """
    Optimization parameters.

    :var resume: Set to ``True`` if optimization must be resume with the optimizer state;
        set to ``False`` to discard the optimizer state and start with fresh optimizer
    :var update_progress: Callback which can be used to provide updates about the progress of a task.
    :var save_model: Callback to notify that the model weights have been changed.
        This callback can be used by the task when temporary weights should be saved (for instance, at the
        end of an epoch). If this callback has been used to save temporary weights, those weights will be
        used to resume optimization if for some reason training was suspended.
    """

    resume: bool = False
    update_progress: Callable[[int], None] = default_progress_callback
    save_model: Callable[[], None] = default_save_model_callback