#
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
#

from ote_sdk.serialization.datetime_mapper import DatetimeMapper
from ote_sdk.utils.time_utils import now


def test_serialization_deserialization():
    """
    This test serializes datetime, deserializes serialized datetime and compares with original one.
    """

    original_time = now()
    serialized_time = DatetimeMapper.forward(original_time)
    assert serialized_time == original_time.strftime("%Y-%m-%dT%H:%M:%S.%f")

    deserialized_time = DatetimeMapper.backward(serialized_time)
    assert original_time == deserialized_time