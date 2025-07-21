# lst=[[1,2,3],[4,5,6,[3,6,[4,6]]],10]
# lst.append('hello')
# print(lst)
# print(lst[1][-1][-1])
# lst[1][-1][-1]='hi bye'
# print(lst)
lst1=[[101,'vinay','k',27,'bigdata',1000],
      [102,'vivek','ps',30,'python',1503],
      [401, 'prv', 'p', 28, 'python',1750],
      [103,'erd','e',28,'bigdata',1500],
      [132, 'orv', 'o', 30, 'python',324]]
sum1=0
for i in lst1:
        sum1+=i[5]
print(sum1)
    # print(i[1],i[2],i[3])
    #   if i[3]==30:
    #        print(i[1:4])
      # if i[4] == 'python':
      #       print(i[1:])
      # if i[3]<28 and i[4]=='python':
      #     print(i[1:4])