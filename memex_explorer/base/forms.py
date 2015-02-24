"""Provides base forms, configured via django-crispy-forms.

The `AddProjectForm` form represents the simplest instance."""

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from base.models import Project


class CrispyModelForm(ModelForm):
    """Make Django model forms "crispy", a la django-crispy-forms."""
    
    def __init__(self, *args, **kwargs):
        """Initialize with a FormHelper and default submit action."""

        super(CrispyModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(Submit('submit', "Submit")))


class AddProjectForm(CrispyModelForm):
    """Add Project crispy model form."""
    class Meta:
        model = Project
        fields = ['name', 'description']

<<<<<<< HEAD
=======

class ProjectSettingsForm(AddProjectForm):
    """Change the settings of a project."""

>>>>>>> 504db77a6276b2ebfecde1031f5f3dd8af50ca63
