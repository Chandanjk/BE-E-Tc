%function to calculate ht
clear all;
close all;
clc;

%Function to modulate a binary stream using GMSK modulation
nrz_data = [0 1 0.5 1 0 0.5 0.5 1 0.5 1 1 0 0 0 0.5];
Fc = 935200000;
L = 4;
pi=3.14;
Tb=1; %bit duration
BT=0.3; %BT product of filter (Bandwidth time product)
sps=32;
Ts=Tb/sps; %sample period
t=0.5;
%s - GMSK modulated signal with carrier
%t - time base for the carrier modulated signal
%s_complex - baseband GMSK signal (I+jQ)
Fs = L*Fc; Ts=1/Fs;Tb = L*Ts; %derived waveform timing parameters
nrz_data=nrz_data(:); %serialize input stream
ck = 2*nrz_data-1;%NRZ format
ct = kron(ck,ones(L,1));%Convert to waveform using oversampling factor

k=1;%truncation length for Gaussian LPF

%Gaussian LPF with BT=0.25
alpha=2*pi*BT/(sqrt(log2(2))); %=1/sigma(variance)
gauss=(alpha*(2*t-0.5))-(alpha*(2*t+0.5)); % q function 
K=pi/2;
gauss=K*gauss;

nrz_gauss = conv(gauss,ct,'full'); %convolve with Gaussian LPF
%delay = (length(h)-1)/2; %FIR filters group delay
%gt = gt(delay+1:end-delay);%remove unwanted portions in filter output
nrz_gauss = nrz_gauss/max(abs(nrz_gauss));%normalize the output of Gaussian LPF to +/-1
phi = filter(1,[1,-1],nrz_gauss*Ts);
phi = phi *0.5*pi/Tb; %h=0.5 - %integrate to get phase information

I = cos(phi); Q = sin(phi); %cross-correlated baseband I/Q signals
s_complex = I - 1i*Q; %complex baseband representation

t=((0:1:length(I)-1)*Ts).'; %for RF carrier
iChannel = I.*cos(2*pi*Fc*t); 
qChannel = Q.*sin(2*pi*Fc*t);
s =(iChannel - qChannel).'; %real signal - with RF carrier

subplot(2,4,1);
plot((0:1:length(ct)-1)*Ts,ct);
title('c(t)');

subplot(2,4,2);
plot(-k*Tb:Ts:k*Tb,gauss);
title(['gauss')

subplot(2,4,5);
plot((0:1:length(nrz_gauss)-1)*Ts,nrz_gauss);
title('nrz_gauss');

subplot(2,4,6);
plot((0:1:length(phi)-1)*Ts,phi);
title('\phi(t)');

subplot(2,4,3);
plot(t,I,'--');
hold on;
plot(t,iChannel,'r');
xlim([0,10*Tb]);
title('I(t)cos(2 \pi f_c t)');

subplot(2,4,4);
plot(t,Q,'--');
hold on;
plot(t,qChannel,'r');
xlim([0,10*Tb]);
title('Q(t)sin(2 \pi f_c t)');

subplot(2,4,7);
plot(t,s);
title('s(t)');
xlim([0,10*Tb]);

subplot(2,4,8); 
plot(I,Q);
title('constellation');