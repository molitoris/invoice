import os
import jinja2


class InvoiceGenerator:
    """Class to generate an invoice based on a latex template"""

    def __init__(self, template_file=None):
        """
        :param template_file: path to the tex template file
        """

        self.template_file = self._get_template_file(template_file)

    @staticmethod
    def _get_template_file(template_file=None):
        if template_file is None:
            try:
                import importlib.resources as pkg_resources
            except ImportError:
                # Backport for python < 3.7
                import importlib_resources as pkg_resources

            from invoice import templates

            return pkg_resources.read_text(templates, "invoice_temp.tex")

        with open(template_file, "r") as f:
            return f.read()

    def fill_template(self, *args, **kwargs):

        latex_jinja_env = jinja2.Environment(
            block_start_string="\BLOCK{",
            block_end_string="}",
            variable_start_string="\VAR{",
            variable_end_string="}",
            comment_start_string="\#{",
            comment_end_string="}",
            line_statement_prefix="%-",
            line_comment_prefix="%#",
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(os.path.abspath(".."))
        )

        jinja_template = latex_jinja_env.from_string(self.template_file)
        return jinja_template.render(*args, **kwargs)

