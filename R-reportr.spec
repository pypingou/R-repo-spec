%global packname  reportr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          A general message and error reporting system

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The reportr package provides a system for reporting messages, which
provides certain useful features over the standard R system, such as the
incorporation of output consolidation, message filtering, automatic
generation of stack traces for debugging, and conditional reporting based
on the current "output level".

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
%doc %{rlibdir}/reportr/LICENCE
%doc %{rlibdir}/reportr/html
%doc %{rlibdir}/reportr/NEWS
%doc %{rlibdir}/reportr/DESCRIPTION
%{rlibdir}/reportr/INDEX
%{rlibdir}/reportr/help
%{rlibdir}/reportr/R
%{rlibdir}/reportr/NAMESPACE
%{rlibdir}/reportr/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora