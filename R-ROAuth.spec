%global packname  ROAuth
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          R interface for OAuth

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RCurl R-digest R-methods 
Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-RCurl R-digest R-methods
BuildRequires:    R-methods 


%description
This package provides an interface to the OAuth 1.0 specification,
allowing users to authenticate via OAuth to the server of their choice.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora