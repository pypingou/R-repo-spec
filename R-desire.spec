%global packname  desire
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Desirability functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-loglognorm 

BuildRequires:    R-devel tex(latex) R-loglognorm 

%description
Harrington and Derringer-Suich type desirability functions

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
%doc %{rlibdir}/desire/html
%doc %{rlibdir}/desire/DESCRIPTION
%{rlibdir}/desire/data
%{rlibdir}/desire/NAMESPACE
%{rlibdir}/desire/Meta
%{rlibdir}/desire/help
%{rlibdir}/desire/unittests
%{rlibdir}/desire/INDEX
%{rlibdir}/desire/demo
%{rlibdir}/desire/R
%{rlibdir}/desire/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora