clear all;
close all;
clc;

%Erlang's first distribution formula plot
%P(N)=(A^N/N!)/(Sum k from 0 to N A^k/k!)
%N : Number of Lines
%k : Availability

N = 30

P = zeros(1,N)

for A = 1 : N
    num = A^N/factorial(N)
    denominator = 0
    for k = 0 : N
        denominator=denominator + A^k/factorial(k)
    end
    P(A) = num/denominator
end

A = 1 : N
plot(A,P)
xlabel('A (traffic offered in E)')
ylabel('P(N) (Probability of congestion/Traffic)')
title('Erlang s 1st Distribution formula for N=30');

        
    