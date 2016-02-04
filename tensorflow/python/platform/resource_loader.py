# Copyright 2015 Google Inc. All Rights Reserved.
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
# ==============================================================================

"""Load a file resource and return the contents."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=unused-import
# pylint: disable=g-import-not-at-top
# pylint: disable=wildcard-import
from . import control_imports
import tensorflow.python.platform
if control_imports.USE_OSS:
  from tensorflow.python.platform.default._resource_loader import *
else:
  from tensorflow.python.platform.google._resource_loader import *
