%global packname  ifa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          7.0
Release:          1%{dist}
Summary:          Independent Factor Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mvtnorm 


%description
The package performes Independent Factor Analysis

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
%doc %{rlibdir}/ifa/DESCRIPTION
%doc %{rlibdir}/ifa/html
%{rlibdir}/ifa/data
%{rlibdir}/ifa/R
%{rlibdir}/ifa/libs
%{rlibdir}/ifa/NAMESPACE
%{rlibdir}/ifa/INDEX
%{rlibdir}/ifa/Meta
%{rlibdir}/ifa/help

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 7.0-1
- Update to version 7.0

* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 6.0-1
- initial package for Fedora