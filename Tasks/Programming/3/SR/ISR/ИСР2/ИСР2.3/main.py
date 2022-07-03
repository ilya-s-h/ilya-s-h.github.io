def fib(n):
  res_lst = [0, 1]
  if n > 1:
    while True:
      cur_el = sum(res_lst[len(res_lst) - 2::])
      if cur_el <= n:
        res_lst.append(cur_el)
      else:
        break
  return res_lst


if __name__ == "__main__":
    print(fib(22))