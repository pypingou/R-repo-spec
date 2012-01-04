%global packname  waveclock
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Time-frequency analysis of cycling cell luminescence data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rwave 

BuildRequires:    R-devel tex(latex) R-Rwave 

%description
waveclock is an R function designed to assess the period and amplitude of
cycling cell luminescence data. The function reconstructs the modal
frequencies from a continuous wavelet decomposition of the luminescence
data using the 'crazy climbers' algorithm described in "Practical
Time-Frequency Analysis: Gabor and Wavelet Transforms with an
Implementation in S", by Rene Carmona, Wen L. Hwang and Bruno Torresani,
Academic Press, 1998.

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
%doc %{rlibdir}/waveclock/DESCRIPTION
%doc %{rlibdir}/waveclock/html
%{rlibdir}/waveclock/Meta
%{rlibdir}/waveclock/INDEX
%{rlibdir}/waveclock/NAMESPACE
%{rlibdir}/waveclock/help
%{rlibdir}/waveclock/data
%{rlibdir}/waveclock/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora