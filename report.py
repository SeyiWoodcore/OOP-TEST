import sqlalchemy


 # Creating a class for all my query objects
class script:

    def __init__(self, Branch, start_date, end_date):
        self.Branch = Branch
        self.start_date = start_date
        self.end_date = end_date



 #A function that returns the query to get Active customers
    def ActiveCustomerReportsQuery(self):
            return sqlalchemy.text(
                f"""  o.`name` AS "Branch",
					upper(COALESCE (c.display_name, c.fullname)) AS "Customer Name",
                    c.account_no AS "CIF Number",
                    c.external_id as "External Id",
                    if(c.legal_form_enum = 2, "Entity", "Person") AS "Customer Type",
                    upper(c.firstname) AS "First Name",
                    upper(c.lastname) AS "Last Name",
                    c.office_joining_date "Office Join Date",
                    c.submittedon_date AS "Submitted Date",
                    c.activation_date AS "Activation Date",
                    ( SELECT code_value FROM m_code_value WHERE code_id = 4 AND id = c.gender_cv_id ) AS Gender,
                    c.mobile_no AS "Mobile Number",
                    c.email_address AS "Email",
                    adr.address_line_1 AS "Address Line 1",
                    adr.address_line_2 AS "Address Line 2",
                    adr.address_line_3 AS "Address Line 3",
                    adr.city as "City",
                    cv_state.code_value AS "State or Province",
                    cv_country.code_value AS "Country",
                    adr.postal_code AS "Postcal Code",
                    c.date_of_birth AS "Date of Birth",
                    '' AS "BVN",
                    '' AS "TIN",
                    '' AS "NIN",
                    IF(c.is_staff = 1, "True", "False") AS "Staff",
                    IF(c.is_fep = 1, "True", "False") AS 'Fep',
                    IF(c.is_fep = 1, "True", "False") AS 'Pep',
					upper(COALESCE(st.display_name, m_appuser.username)) AS "Account Officer",
                    ct.tier_name AS "Tier Name"
                FROM
                    m_office o
                        JOIN m_client c ON c.office_id = o.id
                        LEFT JOIN m_appuser ON m_appuser.id = c.submittedon_userid
                        LEFT JOIN m_staff st ON st.id = c.staff_id
                        LEFT JOIN m_client_address cd ON cd.client_id = c.id
                        LEFT JOIN m_address adr ON adr.id = cd.address_id
                        LEFT JOIN r_enum_value r ON r.enum_name = status_enum
                        AND r.enum_id = c.status_enum
                        LEFT JOIN m_client_tiers ct ON ct.id = c.client_tiers_id
                        LEFT JOIN m_code_value cv_country ON cv_country.id = adr.country_id
                        LEFT JOIN m_code_value cv_state ON cv_state.id = adr.state_province_id
                WHERE
                    c.status_enum = 300
                    AND o.id IN {self.branch}
                        AND c.activation_date BETWEEN '{self.start_date}' AND '{self.end_date}' """
        )

    

    def ActiveLoansQuery(self):
         return sqlalchemy.text(
              f""" SELECT
                     M.name AS BRANCH,
                     fullname AS CUSTOMERNAME,
                    L.account_no AS LOAN_ACCOUNT_NO,
C.account_no AS CIF_NUMBER,
disbursedon_date AS DISBURSEMENT_DATE,
expected_maturedon_date AS EXPECCTED_MATURITY_DATE,
currency_code AS CURRENCY,
principal_amount AS PRINCIPAL_AMOUNT,
approved_principal AS PRINCIPAL_REPAID,
principal_writtenoff_derived AS PRINCIPAL_WRITTEN_0FF,
principal_outstanding_derived AS PRINCIPAL_BALANCE,
interest_charged_derived AS INTEREST_CHARGED,
interest_writtenoff_derived AS INTEREST_WRITTENOFF,
interest_waived_derived AS INTEREST_WAIVED,
interest_outstanding_derived AS INTEREST_BALANCE,
fee_charges_charged_derived AS FEE_CHARGED,
fee_charges_repaid_derived AS FEE_REPAID,
fee_charges_writtenoff_derived AS FEE_WRITTEN_OFF,
fee_charges_waived_derived AS FEE_WAIVED,
fee_charges_outstanding_derived AS FEE_BALANCE,
penalty_charges_charged_derived AS PENALTY_CHARGED,
penalty_charges_repaid_derived AS PENALTY_REPAID,
penalty_charges_writtenoff_derived AS PENALTY_WRITTENOFF,
penalty_charges_outstanding_derived AS PENALTY_BALANCE,
L.external_id AS LOAN_EXTERNAL_ID,
L.client_id AS CUSTOMER_EXTERNAL_ID,
loan_officer_id AS LOAN_OFFICER
FROM m_office AS M
JOIN m_client AS C ON M.id = C.id
JOIN m_loan AS L ON 
C.id = L.id
WHERE status_enum = 300 AND
                  M.name IN {self.Branch}
                 AND activation_date  BETWEEN '{self.start_date} AND '{self.end_date}"""
            )
    
  
