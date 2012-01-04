%global packname  synchronicity
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.13
Release:          1%{?dist}
Summary:          Boost mutex functionality for R.

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package provides Boost mutex functionality in R.

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
%doc %{rlibdir}/synchronicity/DESCRIPTION
%doc %{rlibdir}/synchronicity/html
%{rlibdir}/synchronicity/R
%{rlibdir}/synchronicity/Meta
%{rlibdir}/synchronicity/INDEX
%{rlibdir}/synchronicity/libs
%{rlibdir}/synchronicity/help
%{rlibdir}/synchronicity/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.13-1
- initial package for Fedora