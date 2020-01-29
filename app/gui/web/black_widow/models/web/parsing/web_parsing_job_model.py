"""
*********************************************************************************
*                                                                               *
* web_parsing_model.py -- A web parsing job info model                          *
*                                                                               *
********************** IMPORTANT BLACK-WIDOW LICENSE TERMS **********************
*                                                                               *
* This file is part of black-widow.                                             *
*                                                                               *
* black-widow is free software: you can redistribute it and/or modify           *
* it under the terms of the GNU General Public License as published by          *
* the Free Software Foundation, either version 3 of the License, or             *
* (at your option) any later version.                                           *
*                                                                               *
* black-widow is distributed in the hope that it will be useful,                *
* but WITHOUT ANY WARRANTY; without even the implied warranty of                *
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 *
* GNU General Public License for more details.                                  *
*                                                                               *
* You should have received a copy of the GNU General Public License             *
* along with black-widow.  If not, see <http://www.gnu.org/licenses/>.          *
*                                                                               *
*********************************************************************************
"""

from django.db import models

from black_widow.app.gui.web.black_widow.models.abstract_job_model import AbstractJobModel


class WebParsingJobModel(AbstractJobModel):
    """
    Django Web Parsing Job Model
    """
    TYPE_SINGLE_PAGE = 'Single Page'
    TYPE_WEBSITE_CRAWLING = 'Website Crawling'
    TYPES = (
        ('1', TYPE_SINGLE_PAGE),
        ('2', TYPE_WEBSITE_CRAWLING)
    )

    parsing_type: str = models.CharField(
        null=False,
        choices=TYPES,
        max_length=50
    )
    depth: int = models.IntegerField(null=True)

    @staticmethod
    def all() -> models.query.QuerySet:
        return AbstractJobModel._all(WebParsingJobModel)

    def delete(self, using=None, keep_parents=False):
        return super(WebParsingJobModel, self).delete(using, keep_parents)

    def __str__(self) -> str:
        return 'SniffingJobModel(' + str({
            'id': self.id,
            'pid': self.pid,
            'pid_file': self.pid_file,
            'status': self.status_name
        }) + ')'