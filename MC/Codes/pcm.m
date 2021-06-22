clc;
close all;
clear all;
 
cycles=3; %Number of cycles
original_frequency=2000; %Frequency of the signal = 2 kHz
t=[0:1/1000000:cycles/original_frequency]; %Here 1000000 is the 'Matlab' Sampling frequency
original_signal=1*sin(2*pi*original_frequency*t);%Signal pk-pk is 2 units

% Encoding and Sampling
sam_freq=20000; %sampling Frequency = 20 kHz
sam_time=1/sam_freq; %Sampling Time period
n=[0:1/sam_freq:cycles/original_frequency];
num_samples=length(n);
sam_signal=sin(2*pi*original_frequency*n);

%N is num of bits used for quantizing
N=3;
num_levels=2^N; %using N bits we get 2^N levels
width=2/(num_levels-1);
levels=[-1:width:1];
boundaries=[-1+(width/2):width:1-(width/2)];
codes=[0:num_levels-1];
quant=zeros(1,num_samples);
signal_after_coding=zeros(1,num_samples);

% Quantization and coding 
for i=1:num_samples
	index=1;
	if(sam_signal(i)>=boundaries(end))
		signal_after_coding(i)=codes(end);
		quant(i)=levels(end);
	else
		for boundary=boundaries
			if(sam_signal(i)<=boundary)
				signal_after_coding(i)=codes(index);
				quant(i)=levels(index);
				break;
            end
			index=index+1;
        end
    end
end

%Signal after coding
binary_coded_signal=dec2bin(signal_after_coding)


% PCM Decoder

signal_after_coding=bin2dec(binary_coded_signal)
xa=zeros(1,num_samples);
ind=1;
for i = 1:num_samples
    x(i)=levels(signal_after_coding(i)+1);
end
x=x';
t=sam_time*(1:num_samples);
ts = [0:1/1000000:cycles/original_frequency];
[Ts,T] = ndgrid(ts,t);

% Here, Sinc interpolation is used
y = sinc((Ts - T)/sam_time)*x;

%plotting
subplot(2,2,1),
plot(ts,original_signal,'LineStyle','--');  %original Signal
hold on
stem(n,sam_signal);  %Sampled Signal
title('Original and Sampled Signals')
xlabel('Time/n'), ylabel('Signal');
legend('Original Signal','Sampled Signal');

subplot(2,2,2),
plot(ts,original_signal,'LineStyle','--');  %original Signal
hold on
stem(n,quant);  %Quantized signal
title('Original and Quantized Signals')
xlabel('Time/n'), ylabel('Signal');
legend('Original Signal','Quantized Signal');

subplot(2,2,3),
plot(ts, y)
title('Reconstructed Signal')
xlabel('Time'), ylabel('Reconstructed Signal');