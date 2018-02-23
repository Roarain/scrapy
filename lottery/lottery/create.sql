# drop database webapp;
# create database webapp default charset utf8 COLLATE utf8_general_ci;


drop table shuangseqiu_history cascade;

create table if not exists shuangseqiu_history (
  lottery_number nvarchar(10) not null primary key comment '彩票期数',
  red_1 nvarchar(10) comment '红球一',
  red_2 nvarchar(10) comment '红球二',
  red_3 nvarchar(10) comment '红球三',
  red_4 nvarchar(10) comment '红球四',
  red_5 nvarchar(10) comment '红球五',
  red_6 nvarchar(10) comment '红球六',
  blue_1 nvarchar(10) comment '蓝球一',
  happy_sunday nvarchar(100) comment '快乐星期天',
  prize_pool_bonus nvarchar(100) comment '奖池奖金(元)',
  first_prize_count nvarchar(100) comment '一等奖注数',
  first_prize_bonus nvarchar(100) comment '一等奖奖金(元)',
  second_prize_count nvarchar(100) comment '二等奖注数',
  second_prize_bonus nvarchar(100) comment '二等奖奖金(元)',
  total_betting_amount nvarchar(100) comment '总投注额(元)',
  lottery_date date comment '开奖日期'
);

select * from shuangseqiu_history;
truncate shuangseqiu_history;