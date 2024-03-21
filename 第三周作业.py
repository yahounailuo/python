count=0
for ge in range(1,5):
    for shi in range(1,5):
        for bai in range(1,5):
            if ge!=shi and ge!=bai and ge!=shi and shi!=bai:
                he=ge+shi*10+bai*100
                print(he)
                count=count+1
print("总数为",count)
