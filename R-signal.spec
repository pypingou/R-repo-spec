%global packname  signal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Signal processing

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-grDevices R-MASS 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-grDevices R-MASS 

%description
A set of signal processing R functions originally written for
Matlab/Octave.  Includes filter generation utilities, filtering functions,
resampling routines, and visualization of filter models. It also includes
interpolation functions.

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
%doc %{rlibdir}/signal/DESCRIPTION
%doc %{rlibdir}/signal/CITATION
%doc %{rlibdir}/signal/html
%{rlibdir}/signal/R
%{rlibdir}/signal/help
%{rlibdir}/signal/INDEX
%{rlibdir}/signal/data
%{rlibdir}/signal/LICENSE
%{rlibdir}/signal/Meta
%{rlibdir}/signal/NAMESPACE
%{rlibdir}/signal/libs
%{rlibdir}/signal/README_Parks-McClellan

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1-1
- initial package for Fedora