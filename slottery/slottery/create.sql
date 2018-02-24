# drop database webapp;
# create database webapp default charset utf8 COLLATE utf8_general_ci;


drop table daletou_history cascade;

create table if not exists daletou_history (
  lottery_number nvarchar(10) not null primary key comment '彩票期数',
  front_1 nvarchar(10) comment '前区号码一',
  front_2 nvarchar(10) comment '前区号码二',
  front_3 nvarchar(10) comment '前区号码三',
  front_4 nvarchar(10) comment '前区号码四',
  front_5 nvarchar(10) comment '前区号码五',
  back_1 nvarchar(10) comment '后区号码一',
  back_2 nvarchar(10) comment '后区号码二',
  prize_pool_bonus nvarchar(100) comment '奖池奖金(元)',
  first_prize_count nvarchar(100) comment '一等奖注数',
  first_prize_bonus nvarchar(100) comment '一等奖奖金(元)',
  second_prize_count nvarchar(100) comment '二等奖注数',
  second_prize_bonus nvarchar(100) comment '二等奖奖金(元)',
  total_betting_amount nvarchar(100) comment '总投注额(元)',
  lottery_date date comment '开奖日期'
);

select * from daletou_history;
truncate daletou_history;