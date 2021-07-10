# pytlwall configuration file guide
## Table of contents
 - [Basic information](#base_info)
 - [Layer basic information](#layer_info)
 - [Layer information details](#layerN)
 - [Information details for boundary layer](#boundary)
 - [Beam information](#beam_info)
 - [Frequency information](#frequency_info)

## Basic information
Section name [base_info]
The possible options in this section are:
- component_name = a label to identify the element, not necessary
- pipe_radius_m = the pipe radius in meter 
- pipe_hor_m = the pipe horizontal dimension in meter, if there is pipe_radius_m option this value is ignored
- pipe_ver_m = the pipe verical dimension in meter, if there is pipe_radius_m option this value is ignored
- pipe_len_m = the pipe length in meter        
- betax = the average twiss horizontal beta in the component (if not indicated default is 1) 
- betay = the average twiss vertical beta in the component (if not indicated default is 1) 
- chamber_shape = the shape of the vacuum chamber, allowed values are CIRCULAR (default), ELLIPTICAL, RECTANGULAR

## Layer basic information
Section name [layer_info]
- nbr_layers = number of layers before the boundary 

## Layer information details
Section name [layerN] where N is the layer number from 0 to number of layers before the boundary
For every layer N
- type= the kind of layer, possible value are:
 -- CW for conductive wall, 
 -- V for vacuum, 
 -- PEC for perfect conductive electric
- thick_m = layer thickness in meters
- muinf_Hz= mu infinity in Hz
- k_Hz= the relaxation frequency for permeability in Hz ZERO NOT ALLOWED      
- sigmaDC = DC conductivity in S/m INFINITY NOT ALLOWED      
- epsr = real relative permittivity     
- tau = relaxation time for permittivity in second
- RQ = RQ 

## Information details for boundary layer
Section name [boundary]
For the boundary layer
- type= the kind of layer, possible value are:
 -- CW for conductive wall, 
 -- V for vacuum, 
 -- PEC for perfect conductive electric
- muinf_Hz= mu infinity in Hz
- k_Hz= the relaxation frequency for permeability in Hz ZERO NOT ALLOWED      
- sigmaDC = DC conductivity in S/m INFINITY NOT ALLOWED      
- epsr = real relative permittivity     
- tau = relaxation time for permittivity in second
- RQ = RQ 

## Beam information
Section name [beam_info]
For the beam section: 
- test_beam_shift = the distance between the test and beam in meters
- betarel = the relativistic beta, if this option is set all the others cinematic option are ignored
- gammarel = the relativistic gamma, if betarel option is not defined and this option is set all the others cinematic option are ignored

##Frequency information
Section name [frequency_info]
For the frequency section:
fmin = the minimum frequency in Hz
fmax = the maximum frequency in Hz
fstep = the number of points exponent per decade
