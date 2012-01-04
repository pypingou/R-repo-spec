%global packname  ADaCGH2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Analysis of data from aCGH experiments using parallel computing and ff objects

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tilingArray R-aCGH R-waveslim R-cluster R-snapCGH R-snowfall R-ff 

BuildRequires:    R-devel tex(latex) R-tilingArray R-aCGH R-waveslim R-cluster R-snapCGH R-snowfall R-ff 

%description
Analysis and plotting of array CGH data. Allows usage of Circular Binary
Segementation, wavelet-based smoothing (both as in Liu et al., and HaarSeg
as in Ben-Yaacov and Eldar), HMM, BioHMM, GLAD, CGHseg. Most computations
are parallelized.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora