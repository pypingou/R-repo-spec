%global packname  RDS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.01
Release:          1%{?dist}
Summary:          R Functions for Respondent-Driven Sampling

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides functionality for carrying out estimation with data
collected using Respondent-Driven Sampling.  Current functionality is
extremely limited.

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
%doc %{rlibdir}/RDS/html
%doc %{rlibdir}/RDS/DESCRIPTION
%{rlibdir}/RDS/R
%{rlibdir}/RDS/Meta
%{rlibdir}/RDS/data
%{rlibdir}/RDS/INDEX
%{rlibdir}/RDS/help
%{rlibdir}/RDS/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.01-1
- initial package for Fedora