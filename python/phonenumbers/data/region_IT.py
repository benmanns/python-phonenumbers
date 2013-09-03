"""Auto-generated file, do not edit by hand. IT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IT = PhoneMetadata(id='IT', country_code=39, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[01589]\\d{5,10}|3(?:[12457-9]\\d{8}|[36]\\d{7,9})', possible_number_pattern='\\d{6,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='0(?:[26]\\d{4,9}|(?:1(?:[0159]\\d|[27][1-5]|31|4[1-4]|6[1356]|8[2-57])|3(?:[0159]\\d|2[1-4]|3[12]|[48][1-6]|6[2-59]|7[1-7])|4(?:[0159]\\d|[23][1-9]|4[245]|6[1-5]|7[1-4]|81)|5(?:[0159]\\d|2[1-5]|3[2-6]|4[1-79]|6[4-6]|7[1-578]|8[3-8])|7(?:[0159]\\d|2[12]|3[1-7]|4[2346]|6[13569]|7[13-6]|8[1-59])|8(?:[0159]\\d|2[34578]|3[1-356]|[6-8][1-5])|9(?:[0159]\\d|[238][1-5]|4[12]|6[1-8]|7[1-6]))\\d{2,7})', possible_number_pattern='\\d{6,11}', example_number='0212345678'),
    mobile=PhoneNumberDesc(national_number_pattern='3(?:[12457-9]\\d{8}|6\\d{7,8}|3\\d{7,9})', possible_number_pattern='\\d{9,11}', example_number='3123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:0\\d{6}|3\\d{3})', possible_number_pattern='\\d{6,9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='0878\\d{5}|1(?:44|6[346])\\d{6}|89(?:2\\d{3}|4(?:[0-4]\\d{2}|[5-9]\\d{4})|5(?:[0-4]\\d{2}|[5-9]\\d{6})|9\\d{6})', possible_number_pattern='\\d{6,10}', example_number='899123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='84(?:[08]\\d{6}|[17]\\d{3})', possible_number_pattern='\\d{6,9}', example_number='848123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='1(?:78\\d|99)\\d{6}', possible_number_pattern='\\d{9,10}', example_number='1781234567'),
    voip=PhoneNumberDesc(national_number_pattern='55\\d{8}', possible_number_pattern='\\d{10}', example_number='5512345678'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='848\\d{6}', possible_number_pattern='\\d{9}', example_number='848123456'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['0[26]|55']),
        NumberFormat(pattern='(0[26])(\\d{4})(\\d{5})', format='\\1 \\2 \\3', leading_digits_pattern=['0[26]']),
        NumberFormat(pattern='(0[26])(\\d{4,6})', format='\\1 \\2', leading_digits_pattern=['0[26]']),
        NumberFormat(pattern='(0\\d{2})(\\d{3,4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['0[13-57-9][0159]']),
        NumberFormat(pattern='(\\d{3})(\\d{3,6})', format='\\1 \\2', leading_digits_pattern=['0[13-57-9][0159]|8(?:03|4[17]|9[245])', '0[13-57-9][0159]|8(?:03|4[17]|9(?:2|[45][0-4]))']),
        NumberFormat(pattern='(0\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['0[13-57-9][2-46-8]']),
        NumberFormat(pattern='(0\\d{3})(\\d{2,6})', format='\\1 \\2', leading_digits_pattern=['0[13-57-9][2-46-8]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[13]|8(?:00|4[08]|9[59])', '[13]|8(?:00|4[08]|9(?:5[5-9]|9))']),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['894', '894[5-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3'])],
    leading_zero_possible=True)
