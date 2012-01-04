%global packname  its
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Irregular Time Series

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-stats R-Hmisc 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-Hmisc 

%description
The its package contains an S4 class for handling irregular time series

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
%doc %{rlibdir}/its/html
%doc %{rlibdir}/its/DESCRIPTION
%doc %{rlibdir}/its/COPYING
%{rlibdir}/its/examples
%{rlibdir}/its/help
%{rlibdir}/its/changes
%{rlibdir}/its/INDEX
%{rlibdir}/its/Meta
%{rlibdir}/its/dev
%{rlibdir}/its/test
%{rlibdir}/its/R
%{rlibdir}/its/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8-1
- initial package for Fedora