'''
	This module is an apple picking game to control a market.
	
	Classes:
		- AppleTrader
		- PriceCalculator
	
	Example Usage:
	
	Author:
	Version:
	Style Guidelines:
'''


class AppleTrader:
	'''
	one line to be written
	
	Attributes:
		- total_cash_euro (float): amount of money in cash register
		- number_of_total_apples (int): total number of apple in supply
		- number_of_traded_apples (int): number of bought/sold apples
		- is_buy (bool): True if customer buys, otherwise False
	
	Methods:
		- update_supplies: Updates number_of_total_apples and
		 total_cash_euro after each trade
		- get_cash_balance: Returns total_cash_euro
		- get_total_number_of_apples: Returns number_of_total_apples
	
	Example Usage:
		trade = AppleTrader(total_cash_euro=95.5,
							get_cash_balance=70,
							number_of_traded_apples=7,
							is_buy=False)
							
		>>> trade.get_cash_balance()
			95.5		
	'''
	
	def __init__(self,
				 total_cash_euro: float, 
				 number_of_total_apples: int, 
				 number_of_traded_apples: int, 
				 is_buy: bool = True):
		'''
		Initializes the AppleTrader class with total cash,
		 total and traded number of apples, and initial trade status.
		'''
		if (total_cash_euro < 0 
		or number_of_total_apples < 0 
		or number_of_traded_apples < 0):
			raise ValueError("Cash and apple quantities must be non-negative.")

		self.total_cash_euro = total_cash_euro
		self.number_of_total_apples = number_of_total_apples
		self.number_of_traded_apples = number_of_traded_apples
		self.initial_trade_status_is_buy = is_buy
	
	def get_cash_balance(self):
		'''Returns total euro in cash register'''
		return self.total_cash_euro

	def get_total_number_of_apples(self):
		'''Returns number of total apples in supply'''
		return self.number_of_total_apples

	def update_supplies(self, price_per_apple: float, final_trade_status: bool):
		'''
			Updates the supplies based on the final status of the trade.
			
			Parameters:
				- get_cash_balance: 
				-
		'''
		if final_trade_status:
			self.total_cash_euro += self.number_of_traded_apples * price_per_apple
			self.number_of_total_apples -= self.number_of_traded_apples
		else:
			self.total_cash_euro -= self.number_of_traded_apples * price_per_apple
			self.number_of_total_apples += self.number_of_traded_apples


class PriceCalculator:
	'''
	PriceCalculator computes price per apple based on supply status.
	
	Attributes:
		- trade: an object of AppleTrader class
		- base_price_per_apple: (optional, float) = 1.0

	Methods:
		- calculate_supply_ratio: Returns the supply ratio
		- get_price: Computes the price per apple based on supply status
	
	Example Usage:
		trade = AppleTrader(total_cash_euro=100,
							number_of_total_apples=100,
							number_of_traded_apples=5,
							is_buy=True)
							
		price = PriceCalculator(trade, base_price_per_apple=0.99)
							
		>>> price.get_price()
			0.515
	'''
	
	def __init__(self, trader: AppleTrader, base_price_per_apple: float = 1.0):
		'''
		Initializes PriceCalculator with an object of AppleTrader class
		'''
		self.trader = trader
		self.price_per_apple = base_price_per_apple

	def calculate_supply_ratio(self):
		'''Returns the supply ratio (a number between 0 and 1)'''
		if self.trader.number_of_total_apples == 0:
			return 0
		return (self.trader.number_of_total_apples - self.trader.number_of_traded_apples) / self.trader.number_of_total_apples

	def get_price(self):
		'''
		Calculates and returns the price per apple based on supply ratio and trade status
		'''
		supply_ratio = self.calculate_supply_ratio()

		if self.trader.initial_trade_status_is_buy:
			if supply_ratio >= 0.75:
				return self.price_per_apple - supply_ratio / 2
			elif 0.5 <= supply_ratio < 0.75:
				return self.price_per_apple - supply_ratio / 5
			else:
				return self.price_per_apple + supply_ratio / 8
		else:
			if supply_ratio >= 0.75:
				return self.price_per_apple - supply_ratio / 1.8
			elif 0.5 <= supply_ratio < 0.75:
				return self.price_per_apple - supply_ratio / 3.8
			else:
				return self.price_per_apple

if __name__ == '__main__':
    trader = AppleTrader(total_cash_euro=100, number_of_total_apples=100, number_of_traded_apples=5, is_buy=True)
    price_calculator = PriceCalculator(trader, base_price_per_apple=0.99)
    print(price_calculator.get_price())

