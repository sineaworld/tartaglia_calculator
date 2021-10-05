import random   #在jupyter notebook首次运行或者用pycharm运行本程序时要启用这一条
#“*************”所标的，是计算时需要按情况修改的地方
duck=0
wai=0
d0w0=0
d0w1=0
d1w0=0
d1w1=0
d1w2=0
d2w0=0
d2w1=0
d2w2=0
d2w3=0
d3w0=0
d3w1=0
d3w2=0
d3w3=0
d4w0=0
d4w1=0
d4w2=0
d5w0=0
d7=0
ou=0
dian=13   #垫数*****************
chou=98   #攒的抽数****************
total=dian+chou
ourecord="超欧记录：\n"
trytime=10000000   #尝试次数，尝试次数越多概率越准
for k in range(0,trytime):   
    blue=0
    purple=0
    goldc=0   #出鸭
    goldw=0   #歪了
    countp=0    #给紫保底计数
    countg=dian    #给金保底计数
    countw=0    #给大保底计数，如果是大保底，需要将此处修改为1。******************
    for i in range(dian,total):        #攒的抽数
        a=random.random()
        #print(a)
        if countg>=89:
            b=random.random()
            if b>0.5 or countw==1:
                goldc+=1
                countw=0
            else:
                goldw+=1
                countw+=1
            #print("gold",i,a)
            countg=0
            countp=0
            continue
        elif countg>72:
            if a>1-((countg-72)*0.06):
                b=random.random()
                if b>0.5 or countw==1:
                    goldc+=1
                    countw=0
                else:
                    goldw+=1
                    countw+=1
                #print("gold",i,a)
                countp=0
                countg=0
            elif a>0.057:
                if countp==9:
                    purple+=1
                    #print("purple",i,a)
                    countp=0
                    countg+=1
                else:
                    blue+=1
                    countp+=1
                    countg+=1
            elif a>0.006:
                purple+=1
                #print("purple",i,a)
                countg+=1
                countp=0
            else:
                b=random.random()
                if b>0.5 or countw==1:
                    goldc+=1
                    countw=0
                else:
                    goldw+=1
                    countw+=1
                #print("gold",i,a)
                countp=0
                countg=0
        else:
            if a>0.057:
                if countp==9:
                    purple+=1
                    #print("purple",i,a)
                    countp=0
                    countg+=1
                else:
                    blue+=1
                    countp+=1
                    countg+=1
            elif a>0.006:
                purple+=1
                #print("purple",i,a)
                countp=0
                countg+=1
            else:
                b=random.random()
                if b>0.5 or countw==1:
                    goldc+=1
                    countw=0
                else:
                    goldw+=1
                    countw+=1
                #print("gold",i,a)
                countp=0
                countg=0
    #print("第",k,"次，蓝",blue,"紫",purple,"鸭",goldc,"歪",goldw)
    duck+=goldc
    wai+=goldw
    if goldc==0 and goldw==0:
        d0w0+=1
    elif goldc==0 and goldw==1:
        d0w1+=1
    elif goldc==1 and goldw==0:
        d1w0+=1
    elif goldc==1 and goldw==1:
        d1w1+=1
    elif goldc==1 and goldw==2:
        d1w2+=1
    elif goldc==2 and goldw==0:
        d2w0+=1
    elif goldc==2 and goldw==1:
        d2w1+=1
    elif goldc==2 and goldw==2:
        d2w2+=1
    elif goldc==2 and goldw==3:
        d2w3+=1
    elif goldc==3 and goldw==0:
        d3w0+=1
    elif goldc==3 and goldw==1:
        d3w1+=1
    elif goldc==3 and goldw==2:
        d3w2+=1
    elif goldc==3 and goldw==3:
        d3w3+=1
    elif goldc==4 and goldw==0:
        d4w0+=1
    elif goldc==4 and goldw==1:
        d4w1+=1
    elif goldc==4 and goldw==2:
        d4w2+=1
    elif goldc==5 and goldw==0:
        d5w0+=1
    elif goldc>=7:
        d7+=1
    else:
        ou+=1
        record="第"+str(k)+"次时，抽到"+str(goldc)+"个鸭加"+str(goldw)+"个常驻"+"\n"
        ourecord+=record
print("输入：垫",dian,"攒",chou)
print("总计：鸭",duck,"歪",wai)
print("鸭0歪0概率：",d0w0/trytime*100,"%")
print("鸭0歪1概率：",d0w1/trytime*100,"%")
print("鸭1歪0概率：",d1w0/trytime*100,"%")
print("鸭1歪1概率：",d1w1/trytime*100,"%")
print("鸭1歪2概率：",d1w2/trytime*100,"%")
print("鸭2歪0概率：",d2w0/trytime*100,"%")
print("鸭2歪1概率：",d2w1/trytime*100,"%")
print("鸭2歪2概率：",d2w2/trytime*100,"%")
print("鸭2歪3概率：",d2w3/trytime*100,"%")
print("鸭3歪0概率：",d3w0/trytime*100,"%")
print("鸭3歪1概率：",d3w1/trytime*100,"%")
print("鸭3歪2概率：",d3w2/trytime*100,"%")
print("鸭3歪3概率：",d3w3/trytime*100,"%")
print("鸭4歪0概率：",d4w0/trytime*100,"%")
print("鸭4歪1概率：",d4w1/trytime*100,"%")
print("鸭4歪2概率：",d4w2/trytime*100,"%")
print("鸭5歪0概率：",d5w0/trytime*100,"%")
print("大胆点，直接满命概率：",d7/trytime*100,"%")
#print(ourecord)
