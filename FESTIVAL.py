i=0
iteration=int(input())

for i in range(0, iteration):
    input_N_L=input()
    input_Number=input()

    N_L_arr = input_N_L.split()
    Number_arr = input_Number.split()

    N=int(N_L_arr[0]);
    L=int(N_L_arr[1]);

    x=0
    sum=0
    avg=0.0
    min=100.0
    
    while x<=N-L:
        for i in range(0, (N-x)-L+1):
            for j in range(0+x, L+x+i):
                sum=sum+int(Number_arr[j])
            avg=sum/(L+i)

            if min>avg:
                min=avg;
            sum=0
        x+=1
        
    print(min)        
