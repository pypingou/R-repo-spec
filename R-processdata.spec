%global packname  processdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Process Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ggplot2 R-Matrix R-methods 

BuildRequires:    R-devel tex(latex) R-ggplot2 R-Matrix R-methods 

%description
This package implements data structures for stochastic processes, which
consists of either discretely observed continuous time processes, marked
point processes or a combination.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora