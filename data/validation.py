
import datetime

""" Returns a percent string as a decimal parse_float

Expects a string of the form 'XX.XX%'
"""
KEYS = [
        "id",
        "member_id",
        "loan_amnt",
        "funded_amnt",
        "funded_amnt_inv",
        "term",
        "int_rate",
        "installment",
        "grade",
        "sub_grade",
        "emp_title",
        "emp_length",
        "home_ownership",
        "annual_inc",
        "is_inc_v",
        "issue_d",
        "loan_status",
        "pymnt_plan",
        "url",
        "desc",
        "purpose",
        "title",
        "zip_code",
        "addr_state",
        "dti",
        "delinq_2yrs",
        "earliest_cr_line",
        "fico_range_low",
        "fico_range_high",
        "inq_last_6mths",
        "mths_since_last_delinq",
        "mths_since_last_record",
        "open_acc",
        "pub_rec",
        "revol_bal",
        "revol_util",
        "total_acc",
        "initial_list_status",
        "out_prncp",
        "out_prncp_inv",
        "total_pymnt",
        "total_pymnt_inv",
        "total_rec_prncp",
        "total_rec_int",
        "total_rec_late_fee",
        "recoveries",
        "collection_recovery_fee",
        "last_pymnt_d",
        "last_pymnt_amnt",
        "next_pymnt_d",
        "last_credit_pull_d",
        "last_fico_range_high",
        "last_fico_range_low",
        "collections_12_mths_ex_med",
        "mths_since_last_major_derog",
        "policy_code"
    ]

def is_valid_loan(loan):
    return _has_all_keys(loan)

def _has_all_keys(loan):
    for key in KEYS:
        if key not in loan:
            return False
    return True

def parse_percent(val):
    return parse_float(val[0:-1])

def parse_float(val):
    try:
        return float(val)
    except ValueError:
        if len(val) == 0:
            return 0.0
        else:
            raise ValueError

def parse_date(val):
    if len(val) == 0:
        return None
    return datetime.datetime.strptime(val, "%b-%Y")

def parse_int(val):
    try:
        return int(val)
    except ValueError:
        if len(val) == 0:
            return 0
        else:
            raise ValueError("Unable to parse: %s" % val)


def parse_loan_row(row):
    return {
        'id': parse_int(row['id']),
        'member_id': parse_int(row['member_id']),
        'loan_amnt': parse_float(row['loan_amnt']),
        'funded_amnt': parse_float(row['funded_amnt']),
        'funded_amnt_inv': parse_float(row['funded_amnt_inv']),
        'term': row['term'],
        'int_rate': parse_percent(row['int_rate']),
        'installment': parse_float(row['installment']),
        'grade': row['grade'],
        'sub_grade': row['sub_grade'],
        'emp_title': row['emp_title'],
        'emp_length': row['emp_length'],
        'home_ownership': row['home_ownership'],
        'annual_inc': parse_float(row['annual_inc']),
        'is_inc_v': row['is_inc_v'],
        'issue_d': parse_date(row['issue_d']),
        'loan_status': row['loan_status'],
        'pymnt_plan': row['pymnt_plan'],
        'url': row['url'],
        'desc': row['desc'],
        'purpose': row['purpose'],
        'title': row['title'],
        'zip_code': row['zip_code'],
        'addr_state': row['addr_state'],
        'dti': parse_float(row['dti']),
        'delinq_2yrs': parse_int(row['delinq_2yrs']),
        'earliest_cr_line': parse_date(row['earliest_cr_line']),
        'fico_range_low': parse_int(row['fico_range_low']),
        'fico_range_high': parse_int(row['fico_range_high']),
        'inq_last_6mths': parse_int(row['inq_last_6mths']),
        'mths_since_last_delinq': parse_int(row['mths_since_last_delinq']),
        'mths_since_last_record': parse_int(row['mths_since_last_record']),
        'open_acc': parse_int(row['open_acc']),
        'pub_rec': parse_int(row['pub_rec']),
        'revol_bal': parse_float(row['revol_bal']),
        'revol_util': parse_percent(row['revol_util']),
        'total_acc': parse_float(row['total_acc']),
        'initial_list_status': row['initial_list_status'],
        'out_prncp': parse_float(row['out_prncp']),
        'out_prncp_inv': parse_float(row['out_prncp_inv']),
        'total_pymnt': parse_float(row['total_pymnt']),
        'total_pymnt_inv': parse_float(row['total_pymnt_inv']),
        'total_rec_prncp': parse_float(row['total_rec_prncp']),
        'total_rec_int': parse_float(row['total_rec_int']),
        'total_rec_late_fee': parse_float(row['total_rec_late_fee']),
        'recoveries': parse_float(row['recoveries']),
        'collection_recovery_fee': parse_float(row['collection_recovery_fee']),
        'last_pymnt_d': parse_date(row['last_pymnt_d']),
        'last_pymnt_amnt': parse_float(row['last_pymnt_amnt']),
        'next_pymnt_d': parse_date(row['next_pymnt_d']),
        'last_credit_pull_d': parse_date(row['last_credit_pull_d']),
        'last_fico_range_high': parse_int(row['last_fico_range_high']),
        'last_fico_range_low': parse_int(row['last_fico_range_low']),
        'collections_12_mths_ex_med': parse_int(row['collections_12_mths_ex_med']),
        'mths_since_last_major_derog': parse_int(row['mths_since_last_major_derog']),
        'policy_code': parse_int(row['policy_code']),
    }

