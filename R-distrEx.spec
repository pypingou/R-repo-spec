%global packname  distrEx
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Extensions of package distr

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-distr R-evd R-actuar R-startupmsg 

BuildRequires:    R-devel tex(latex) R-methods R-distr R-evd R-actuar R-startupmsg 

%description
Extensions of package distr and some additional functionality

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