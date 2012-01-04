%global packname  websockets
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          HTML 5 Websocket Interface for R

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-caTools R-digest 


BuildRequires:    R-devel tex(latex) R-caTools R-digest



%description
A simple HTML5 websocket interface for R.

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
%doc %{rlibdir}/websockets/html
%doc %{rlibdir}/websockets/DESCRIPTION
%doc %{rlibdir}/websockets/NEWS
%doc %{rlibdir}/websockets/doc
%{rlibdir}/websockets/help
%{rlibdir}/websockets/basic.html
%{rlibdir}/websockets/demo
%{rlibdir}/websockets/Meta
%{rlibdir}/websockets/tests
%{rlibdir}/websockets/libs
%{rlibdir}/websockets/NAMESPACE
%{rlibdir}/websockets/R
%{rlibdir}/websockets/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora