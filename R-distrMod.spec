%global packname  distrMod
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Object oriented implementation of probability models

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-startupmsg R-distr R-distrEx R-RandVar R-MASS R-stats4 

BuildRequires:    R-devel tex(latex) R-methods R-startupmsg R-distr R-distrEx R-RandVar R-MASS R-stats4 

%description
Object oriented implementation of probability models based on packages
'distr' and 'distrEx'

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora