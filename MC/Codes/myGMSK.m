clear all;
close all;
clc;
% Set the samples per symbol variable.
sps = 8;

% Generate random binary data.
data = randi([0 1],1000,1);

% Create GMSK and MSK modulators that accept binary inputs. Set the PulseLength property of the GMSK modulator to 1.
gmskMod = comm.GMSKModulator('BitInput',true,'BandwidthTimeProduct',0.3,'PulseLength',2,'SamplesPerSymbol',sps);
mskMod = comm.MSKModulator('BitInput',true,'SamplesPerSymbol',sps);

% Modulate the data using the GMSK and MSK modulators.

modSigGMSK = step(gmskMod,data);
modSigMSK = step(mskMod,data);

Fs=100;

% PSD of GMSK and MSK
[Pxx,F] = periodogram(modSigGMSK,[],length(modSigGMSK),Fs);
[Pxx1,F] = periodogram(modSigMSK,[],length(modSigMSK),Fs);

plot(F,10*log10(Pxx1),F,10*log10(Pxx));
title('PSD of GMSK and MSK');
xlabel('F(Hz)');
ylabel('P(dB)');

legend('MSK','GMSK');


