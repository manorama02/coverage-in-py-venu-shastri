def get_number_list(num):
  return [int(n) for n in str(num)]

def checkempty(inp_str):
  return inp_str==""
def invalid_length(cc_number):
  return len(cc_number) != 16

def is_valid(cc_number):
	invalid=checkempty(cc_number) | invalid_length(cc_number)
	if invalid:
		return False
	numbers_list = get_number_list(cc_number)
	odd_digits = numbers_list[-1::-2]
	even_digits = numbers_list[-2::-2]
	checksum=0
	for d in even_digits:
		checksum+=sum(get_number_list(d*2))
	checksum+=sum(odd_digits)
	return checksum%10==0

