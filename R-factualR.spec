%global packname  factualR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          thin wrapper for the Factual.com server API

Group:            Applications/Engineering 
License:          Apache License 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-RJSONIO R-RCurl 


BuildRequires:    R-devel tex(latex) R-methods R-RJSONIO R-RCurl



%description
Per the Factual.com website, "Factual is a platform where anyone can share
and mash open, living data on any subject." The data is in the form of
tables and is accessible via REST API.  The factualR package is a thin
wrapper around the Factual.com API, to make it even easier for people
working with R to explore Factual.com data sets.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora