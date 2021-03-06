# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CloItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # sale_statistics 销售统计表
    hall_name = scrapy.Field()                          # 单位
    game_lhdb = scrapy.Field()                          # 游戏-连环夺宝
    game_xywc = scrapy.Field()                          # 游戏-幸运五彩
    game_kxyk = scrapy.Field()                          # 游戏-开心一刻
    game_shxw = scrapy.Field()                          # 游戏-四花选五
    game_sjfg = scrapy.Field()                          # 游戏-三江风光
    game_hysj = scrapy.Field()                          # 游戏-好运射击
    game_qwgef = scrapy.Field()                         # 游戏-趣味高尔夫
    daily_turnover = scrapy.Field()                     # 营业额
    date_time = scrapy.Field()                          # 时间
    # winning_statistics 中奖统计表
    hall_name = scrapy.Field()                          # 单位
    senior_winning_count = scrapy.Field()               # 高等中奖-注数
    senior_winning_amount = scrapy.Field()              # 高等中奖-金额
    medium_winning_amount = scrapy.Field()              # 中等中奖金额
    low_winning_amount = scrapy.Field()                 # 低等中奖金额
    winning_amount = scrapy.Field()                     # 中奖合计
    date_time = scrapy.Field()                          # 时间
    # game_winning_statistics 游戏中奖统计表
    game_name = scrapy.Field()                          # 游戏玩法
    senior_winning_count = scrapy.Field()               # 高等中奖-注数
    senior_winning_amount = scrapy.Field()              # 高等中奖-金额
    medium_winning_amount = scrapy.Field()              # 中等中奖金额
    low_winning_amount = scrapy.Field()                 # 低等中奖金额
    winning_amount = scrapy.Field()                     # 中奖合计
    date_time = scrapy.Field()
    # redemption_statistics 兑奖统计表
    hall_name = scrapy.Field()                          # 单位
    senior_redemption_count = scrapy.Field()            # 高等兑奖-注数
    senior_redemption_amount = scrapy.Field()           # 高等兑奖-金额
    medium_redemption_amount = scrapy.Field()           # 中等兑奖金额
    low_redemption_amount = scrapy.Field()              # 低等兑奖金额
    redemption_amount = scrapy.Field()                  # 兑奖合计
    date_time = scrapy.Field()
    # game_redemption_statistics 游戏兑奖统计表
    game_name = scrapy.Field()                          # 游戏玩法
    senior_redemption_count = scrapy.Field()            # 高等兑奖-注数
    senior_redemption_amount = scrapy.Field()           # 高等兑奖-金额
    medium_redemption_amount = scrapy.Field()           # 中等兑奖金额
    low_redemption_amount = scrapy.Field()              # 低等兑奖金额
    redemption_amount = scrapy.Field()                  # 兑奖合计
    date_time = scrapy.Field()
    # discard_statistics 弃奖统计表
    hall_name = scrapy.Field()                          # 单位
    senior_discard_count = scrapy.Field()               # 高等奖弃奖-注数
    senior_discard_amount = scrapy.Field()              # 高等奖弃奖-金额
    medium_discard_amount = scrapy.Field()              # 中等奖弃奖金额
    discard_amount = scrapy.Field()                     # 弃奖合计
    date_time = scrapy.Field()
    # game_discard_statistics 游戏弃奖统计表
    game_name = scrapy.Field()                          # 游戏玩法
    senior_discard_count = scrapy.Field()               # 高等奖弃奖-注数
    senior_discard_amount = scrapy.Field()              # 高等奖弃奖-金额
    medium_discard_amount = scrapy.Field()              # 中等奖弃奖金额
    discard_amount = scrapy.Field()                     # 弃奖合计
    date_time = scrapy.Field()
    # sale_funds_allocation 销售及资金分配表
    hall_name = scrapy.Field()                          # 单位
    daily_turnover = scrapy.Field()                     # 销售额
    bonus_redemption = scrapy.Field()                   # 奖金-返奖奖金
    bonus_regulating_funds = scrapy.Field()             # 奖金-调节基金
    bonus_amount = scrapy.Field()                       # 奖金-合计
    issue_funds_zczx = scrapy.Field()                   # 发行经费-中彩中心
    issue_funds_province = scrapy.Field()               # 发行经费-省级
    issue_funds_city = scrapy.Field()                   # 发行经费-市级
    issue_funds_total = scrapy.Field()                  # 发行经费-合计
    charity_funds = scrapy.Field()                      # 公益基金
    date_time = scrapy.Field()
    # bonus_funds_allocation 游戏奖金分配表
    game_name = scrapy.Field()                          # 游戏玩法
    daily_turnover = scrapy.Field()                     # 销售额
    bonus_redemption = scrapy.Field()                   # 奖金-返奖奖金
    bonus_regulating_funds = scrapy.Field()             # 奖金-调节基金
    bonus_amount = scrapy.Field()                       # 奖金-合计
    date_time = scrapy.Field()
    # fund_settlement_central_province 中福在线资金结算表（中央级-省级）
    hall_name = scrapy.Field()                          # 单位
    sale_card_amount = scrapy.Field()                   # 售卡金额
    return_card_amount = scrapy.Field()                 # 退卡金额
    bonus_amount = scrapy.Field()                       # 中奖金额
    bonus_recharge_amount = scrapy.Field()              # 奖金充值
    sale_amount = scrapy.Field()                        # 销售额
    provincial_distribution_funds = scrapy.Field()      # 省级发行经费
    city_distribution_funds = scrapy.Field()            # 市级发行经费
    charity_funds = scrapy.Field()                      # 公益金
    receive_amount = scrapy.Field()                     # 应收(缴)金额
    date_time = scrapy.Field()
    # fund_settlement_province_city 中福在线资金结算表（省级-地市级）
    hall_name = scrapy.Field()                          # 单位
    sale_card_amount = scrapy.Field()                   # 售卡金额
    return_card_amount = scrapy.Field()                 # 退卡金额
    bonus_recharge_amount = scrapy.Field()              # 奖金充值
    redemption_amount = scrapy.Field()                  # 兑付奖金
    sale_amount = scrapy.Field()                        # 销售额
    city_distribution_funds = scrapy.Field()            # 地(市)级发行经费
    receive_amount = scrapy.Field()                     # 应收(缴)金额
    date_time = scrapy.Field()
    # fund_settlement_city_hall 中福在线资金结算表（地市级-大厅）
    hall_name = scrapy.Field()                          # 单位
    sale_card_amount = scrapy.Field()                   # 售卡金额
    return_card_amount = scrapy.Field()                 # 退卡金额
    bonus_recharge_amount = scrapy.Field()              # 奖金充值
    redemption_amount = scrapy.Field()                  # 兑付奖金
    sale_amount = scrapy.Field()                        # 销售额
    receive_amount = scrapy.Field()                     # 应收(缴)金额
    date_time = scrapy.Field()
    # dedicated_account_funds   专用帐户资金流向
    hall_name = scrapy.Field()                          # 单位
    revenue_sale_card_amount = scrapy.Field()           # 收入项-售卡金额
    revenue_bonus_recharge_amount = scrapy.Field()      # 收入项-奖金充值
    revenue_amount = scrapy.Field()                     # 收入项-合计
    expenditure_return_card_amount = scrapy.Field()     # 支出项-退卡金额
    expenditure_sale_amount = scrapy.Field()            # 支出项-销售额
    expenditure_amount = scrapy.Field()                 # 支出项-合计
    revenue_expenditure = scrapy.Field()                # 收入支出金额合计
    date_time = scrapy.Field()














