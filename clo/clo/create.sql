drop database webapp;
create database webapp default charset utf8 COLLATE utf8_general_ci;


drop table sales_statistics cascade;

create table if not exists sales_statistics (
  hall_name nvarchar(255) not null comment '大厅名称',
  game_lhdb decimal(15,2) comment '连环夺宝',
  game_xywc decimal(15,2) comment '幸运五彩',
  game_kxyk decimal(15,2) comment '开心一刻',
  game_shxw decimal(15,2) comment '四花选五',
  game_sjfg decimal(15,2) comment '三江风光',
  game_hysj decimal(15,2) comment '好运射击',
  game_qwgef decimal(15,2) comment '趣味高尔夫',
  daily_turnover decimal(16,2) comment '当天总营业额',
  date_time date not null comment '当天日期',
  primary key (hall_name, date_time)
  );

alter table sales_statistics add index index_date_time_sales_statistics (date_time);

select * from sales_statistics;
truncate sales_statistics;