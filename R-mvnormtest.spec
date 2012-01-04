%global packname  mvnormtest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Normality test for multivariate variables

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Generalization of shapiro-wilk test for multivariate variables.

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
%doc %{rlibdir}/mvnormtest/COPYING
%doc %{rlibdir}/mvnormtest/DESCRIPTION
%doc %{rlibdir}/mvnormtest/html
%{rlibdir}/mvnormtest/Meta
%{rlibdir}/mvnormtest/INDEX
%{rlibdir}/mvnormtest/ChangeLog
%{rlibdir}/mvnormtest/NAMESPACE
%{rlibdir}/mvnormtest/help
%{rlibdir}/mvnormtest/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora