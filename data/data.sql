UPDATE res_country SET address_format=E'%(street)s\n%(street2)s\n%(zip)s %(city)s' WHERE code = 'AT';
UPDATE res_lang SET date_format = '%d.%m.%Y' WHERE code = 'de_DE';
