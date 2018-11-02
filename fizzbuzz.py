
class Fizzbuzz():

    def play(self, number):
        if self.isDivisibleBy(number, 15): return 'FizzBuzz'
        if self.isDivisibleBy(number, 3): return "Fizz"
        if self.isDivisibleBy(number, 5): return "Buzz"
        return number


    def isDivisibleBy(self, number, divisor):
        return number % divisor == 0
