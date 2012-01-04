%global packname  semdiag
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Structural equation modeling diagnostics

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sem 


BuildRequires:    R-devel tex(latex) R-sem



%description
Outlier and leverage diagnostics for SEM.

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
%doc %{rlibdir}/semdiag/DESCRIPTION
%doc %{rlibdir}/semdiag/html
%{rlibdir}/semdiag/NAMESPACE
%{rlibdir}/semdiag/Meta
%{rlibdir}/semdiag/INDEX
%{rlibdir}/semdiag/R
%{rlibdir}/semdiag/help
%{rlibdir}/semdiag/data
%{rlibdir}/semdiag/CHANGES

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora