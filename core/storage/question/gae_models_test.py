# Copyright 2017 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from core.domain import exp_domain
from core.platform import models
from core.tests import test_utils

(question_models,) = models.Registry.import_models([models.NAMES.question])


class QuestionModelUnitTests(test_utils.GenericTestBase):
    """Tests the QuestionModel class."""

    def test_create_question(self):
        state = exp_domain.State.create_default_state('ABC')
        question_state_data = state.to_dict()
        language_code = 'en'
        version = 1
        question_model = question_models.QuestionModel.create(
            question_state_data, language_code, version)

        self.assertEqual(
            question_model.question_state_data, question_state_data)
        self.assertEqual(question_model.language_code, language_code)


class QuestionSummaryModelUnitTests(test_utils.GenericTestBase):
    """Tests the QuestionSummaryModel class."""

    def test_get_by_creator_id(self):
        question_summary_model_1 = question_models.QuestionSummaryModel(
            id='question_1',
            creator_id='user',
            question_content='Question 1'
        )
        question_summary_model_2 = question_models.QuestionSummaryModel(
            id='question_2',
            creator_id='user',
            question_content='Question 2'
        )
        question_summary_model_1.put()
        question_summary_model_2.put()

        question_summaries = (
            question_models.QuestionSummaryModel.get_by_creator_id('user'))
        self.assertEqual(len(question_summaries), 2)
        self.assertEqual(question_summaries[0].id, 'question_1')
        self.assertEqual(question_summaries[1].id, 'question_2')


class QuestionSkillLinkModelUnitTests(test_utils.GenericTestBase):
    """Tests the QuestionSkillLinkModel class."""

    def test_create_question_skill_link(self):
        question_id = 'A Test Question Id'
        skill_id = 'A Test Skill Id'
        questionskilllink_model = question_models.QuestionSkillLinkModel.create(
            question_id, skill_id)

        self.assertEqual(questionskilllink_model.question_id, question_id)
        self.assertEqual(questionskilllink_model.skill_id, skill_id)
