%global packname  PCS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Calculate the probability of correct selection (PCS)

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-statmod R-multtest 

BuildRequires:    R-devel tex(latex) R-statmod R-multtest 

%description
Given k populations (can be in thousands), what is the probability that a
given subset of size t contains the true top t populations?  This package
finds this probability and offers three tuning parameters (G, d, L) to
relax the definition.

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
%doc %{rlibdir}/PCS/html
%doc %{rlibdir}/PCS/DESCRIPTION
%{rlibdir}/PCS/R
%{rlibdir}/PCS/help
%{rlibdir}/PCS/INDEX
%{rlibdir}/PCS/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora