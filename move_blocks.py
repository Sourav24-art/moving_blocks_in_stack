l1 = 'sthfwr'
l2 = 'sgdqw'
l3 = 'btw'
l4 = 'drwtnqzj'
l5 = 'fbhglvtz'
l6 = 'lptcvbsg'
l7 = 'zbrtwgp'
l8 = 'ngmtcjr'
l9 = 'lgbw'

def Cap_lst(k):
  return list(k.upper())

lst_1 = Cap_lst(l1)
lst_2 = Cap_lst(l2)
lst_3 = Cap_lst(l3)
lst_4 = Cap_lst(l4)
lst_5 = Cap_lst(l5)
lst_6 = Cap_lst(l6)
lst_7 = Cap_lst(l7)
lst_8 = Cap_lst(l8)
lst_9 = Cap_lst(l9)

print(lst_9)



with open("data.txt","r") as instructions:
  data = instructions.read().split("\n")

print(len(data))
req_lst = []

#data extraction phase one
for i in data:
  k_01 = i.split("move")
  k_02 = k_01[1].split("from")
  k_03 = k_02[1].split("to")
  k_03.insert(0,k_02[0])
  req_lst.append(k_03)
  

print(req_lst)




def concatenate(l1,l2):
  for i in l2:
    l1.append(i)
  return l1


#this function will rearrange the blocks as per the block_count, start_position and end_position
def rearrange(Block_count,start_pos,end_pos):
  k = []
  if int(start_pos) == 1:
    return pop_elements_add(Block_count,lst_1,end_pos)
  elif int(start_pos) == 2:
    return pop_elements_add(Block_count,lst_2, end_pos)
  elif int(start_pos) == 3:
    return pop_elements_add(Block_count,lst_3,end_pos)
  elif int(start_pos) == 4:
    return pop_elements_add(Block_count,lst_4,end_pos)
  elif int(start_pos) == 5:
    return pop_elements_add(Block_count,lst_5,end_pos)
  elif int(start_pos) == 6:
    return pop_elements_add(Block_count,lst_6,end_pos)
  elif int(start_pos) == 7:
    return pop_elements_add(Block_count,lst_7,end_pos)
  elif int(start_pos) == 8:
    return pop_elements_add(Block_count,lst_8,end_pos)
  elif int(start_pos) == 9:
    return pop_elements_add(Block_count,lst_9,end_pos)
    
    
def pop_elements_add(number,lst_name, end_pos):
  global lst_1 
  global lst_2
  global lst_3
  global lst_4
  global lst_5
  global lst_6
  global lst_7
  global lst_8
  global lst_9 
  store_end_val = []
  for i in range(0,int(number)):
    #store_end_val.append(lst_name[-1])
    store_end_val.insert(0,lst_name[-1])
    lst_name.pop(-1)
  if int(end_pos) == 1:
    lst_1 = concatenate(lst_1, store_end_val)
  elif int(end_pos) == 2:
    lst_2 = concatenate(lst_2, store_end_val)
  elif int(end_pos) == 3:
    lst_3 = concatenate(lst_3, store_end_val)
  elif int(end_pos) == 4:
    lst_4 = concatenate(lst_4, store_end_val)
  elif int(end_pos) == 5:
    lst_5 = concatenate(lst_5, store_end_val)
  elif int(end_pos) == 6:
    lst_6 = concatenate(lst_6, store_end_val)
  elif int(end_pos) == 7:
    lst_7 = concatenate(lst_7, store_end_val)
  elif int(end_pos) == 8:
    lst_8 = concatenate(lst_8, store_end_val)
  elif int(end_pos) == 9:
    lst_9 = concatenate(lst_9, store_end_val)
  

  
  

#data extraction phase two
req_len = len(req_lst)
final_lst = []
for i in req_lst:
  final_lst.append(rearrange(i[0],i[1],i[2]))

print(lst_1[-1])
print(lst_2[-1])
print(lst_3[-1])
print(lst_4[-1])
print(lst_5[-1])
print(lst_6[-1])
print(lst_7[-1])
print(lst_8[-1])
print(lst_9[-1])

