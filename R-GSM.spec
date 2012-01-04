%global packname  GSM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Gamma Shape Mixture

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gtools R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-gtools R-methods R-utils 

%description
This package implements a Bayesian approach for estimation of a mixture of
gamma distributions in which the mixing occurs over the shape parameter.
This family provides a flexible and novel approach for modeling
heavy-tailed distributions, it is computationally efficient, and it only
requires to specify a prior distribution for a single parameter.

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
%doc %{rlibdir}/GSM/DESCRIPTION
%doc %{rlibdir}/GSM/html
%{rlibdir}/GSM/help
%{rlibdir}/GSM/Meta
%{rlibdir}/GSM/R
%{rlibdir}/GSM/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora