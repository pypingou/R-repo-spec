%global packname  dynsurv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Dynamic models for survival data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-survival R-ggplot2 R-nleqslv 

BuildRequires:    R-devel tex(latex) R-methods R-survival R-ggplot2 R-nleqslv 

%description
Functions to fit time-varying coefficient models for interval censored and
right censored survival data. Three major approaches are implemented: 1)
Bayesian Cox model with time-independent, time-varying or dynamic
coefficients for right censored and interval censored data; 2) Spline
based time-varying coefficient Cox model for right censored data; 3)
Transformation model with time-varying coefficients for right censored
data using estimating equations.

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
* Wed Dec 07 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora