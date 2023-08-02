from odoo import models, fields, api


class Person(models.Model):
    _name = 'custom.person'
    _description = 'Custom Person Model'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Char(string='Date of birth', required=True)
    citizenship_number = fields.Char(string='Citizenship Number', required=True)
    voter_id = fields.Char(string='Voter ID')
    mobile_no = fields.Char("Mobile No")
    email = fields.Char(string='Email')
    permanent_address = fields.Text(string='Permanent Address:Province')
    district = fields.Text(string='District')
    parliamentary_constituency_number = fields.Char(string='Parliamentary Constituency Number')
    state_election_constituency_number = fields.Char(string='State Election Constituency Number')
    municipality = fields.Char(string='Municipality')
    rural_municipality = fields.Char(string='Rural Municipality')
    temporary_address = fields.Text(string='Temporary Address:Province')
    father_name = fields.Char(string='Father Name')
    mother_name = fields.Char(string='Mother Name')
    husband_name = fields.Char(string="Husband's Name")
    wife_name = fields.Char(string="Wife's Name")
    family_number = fields.Char(string='Family Number')
    educational_qualification_certificate = fields.Boolean(string='Educational Qualification Certificate',
                                                           default=False, widget='checkbox')
    is_12th_grade_completed = fields.Boolean(string='12th Grade Completed', default=False, widget='checkbox')
    has_bachelors_degree = fields.Boolean(string="Bachelor's Degree", default=False, widget='checkbox')
    is_postgraduate = fields.Boolean(string='Postgraduate', default=False, widget='checkbox')
    has_phd = fields.Boolean(string='Ph.D.', default=False, widget='checkbox')
    is_others = fields.Boolean(string='Others', default=False, widget='checkbox')
    religion = fields.Char(string='Religion')
    MARITAL_STATUS_SELECTION = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        # Add more marital status options here
    ]

    marital_status = fields.Selection(
        MARITAL_STATUS_SELECTION,
        string='Marital Status',
        default='single'
    )
    ETHNIC_GROUP_SELECTION = [
        ('adibasi_janjati', 'Adibasi/Janjati'),
        ('dalit', 'Dalit'),
        ('madhesi', 'Madhesi'),
        ('muslim', 'Muslim'),
        ('backward_region', 'Backward Region'),
        ('disabled', 'Disabled'),
        ('others', 'Others'),
    ]

    ethnic_group = fields.Selection(
        ETHNIC_GROUP_SELECTION,
        string='Ethnic Group'
    )
    year_of_continuous_residence = fields.Integer(string='Year of Continuous Residence')
    date_of_previous_membership = fields.Date(string='Date of Taking Active Membership Previously')
    membership_number = fields.Char(string='Membership Number')
    past_responsibilities = fields.Text(string='Past Responsibilities')
    organization_name = fields.Char(string='Organization Name', required=True)
    position = fields.Char(string='Position', required=True)
    years_of_experience = fields.Float(string='Years of Work Experience', digits=(6, 2))
    signature = fields.Binary(string='Signature', attachment=True)
    recommending_member_name = fields.Char(string='Name of the Member Recommending')
    contact_number = fields.Char(string='Contact Number')
    applicant_signature = fields.Binary(string="Applicant's Signature", attachment=True)
    date_field = fields.Date(string='Date')
    membership_period = fields.Char(string='Membership Period')
    photo = fields.Binary(string='Photo', attachment=True)

    def action_send_mail(self):
        template = self.env.ref('cus_123.cus_1223')
        for rec in self:
            template.send_mail(rec.id, force_send=True)
