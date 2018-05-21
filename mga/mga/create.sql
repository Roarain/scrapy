# drop database webapp;
# create database webapp default charset utf8 COLLATE utf8_general_ci;


drop table licensed cascade;

create table if not exists licensed (
  company_name nvarchar(100) comment '公司名称',
  reg_no nvarchar(100) comment '注册编号',
  license_number nvarchar(100) comment 'license号码',
  license_class nvarchar(100) comment 'license class',
  platform nvarchar(100) comment 'platform',
  status nvarchar(100) comment 'license status',
  registered_address nvarchar(500) comment '注册地址',
  termination_date nvarchar(100) comment 'termination date',
  entity_telephone_number nvarchar(100) comment '电话号码',
  general_email_address nvarchar(100) comment '邮箱'
);

select * from licensed;
truncate licensed;