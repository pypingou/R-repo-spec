%global packname  SV
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Quasi-likelihood and indirect inference in non-Gaussian stochastic volatility models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-setRNG 


BuildRequires:    R-devel tex(latex) R-setRNG



%description
Quasi-likelihood and indirect inference in non-Gaussian stochastic
volatility models for univariate and multivariate financial data. For
univariate data both quasi-likelihood estimation and indirect inference
are implemented, while for the bivariate data a quasi-likelihood method is

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.5-1
- initial package for Fedora