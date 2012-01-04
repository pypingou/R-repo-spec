%global packname  bayesGARCH
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.00.10
Release:          1%{?dist}
Summary:          Bayesian Estimation of the GARCH(1,1) Model with Student-t Innovations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1-00.10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-coda 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-coda 

%description
This package provides the bayesGARCH function which performs the Bayesian
estimation of the GARCH(1,1) model with Student's t innovations.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.00.10-1
- initial package for Fedora