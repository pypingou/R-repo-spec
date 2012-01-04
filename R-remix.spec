%global packname  remix
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Remix your data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-plyr R-survival 
Requires:         R-Hmisc R-ascii 

BuildRequires:    R-devel tex(latex) R-plyr R-survival
BuildRequires:    R-Hmisc R-ascii 


%description
remix provides remix, a quick and easy function for describing datasets.
It can be view as a mix of cast (in package reshape) and summary.formula
(in package Hmisc).

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
%doc %{rlibdir}/remix/NEWS
%doc %{rlibdir}/remix/html
%doc %{rlibdir}/remix/DESCRIPTION
%{rlibdir}/remix/INDEX
%{rlibdir}/remix/Meta
%{rlibdir}/remix/R
%{rlibdir}/remix/help
%{rlibdir}/remix/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora