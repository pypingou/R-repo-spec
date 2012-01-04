%global packname  RCurl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          General network (HTTP/FTP/...) client interface for R

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-bitops 


BuildRequires:    R-devel tex(latex) R-methods R-bitops



%description
The package allows one to compose general HTTP requests and provides
convenient functions to fetch URIs, get & post forms, etc. and process the
results returned by the Web server. This provides a great deal of control
over the HTTP/FTP/... connection and the form of the request while
providing a higher-level interface than is available just using R socket
connections.  Additionally, the underlying implementation is robust and
extensive, supporting FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS,
telnet, dict, ldap, and also supports cookies, redirects, authentication,

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora