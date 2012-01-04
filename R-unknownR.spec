%global packname  unknownR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          You didn't know you didn't know?

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-utils 

BuildRequires:    R-devel tex(latex) R-tcltk R-utils 

%description
Utility to quickly find useful functions in R that you didn't know you
didn't know.

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
%doc %{rlibdir}/unknownR/NEWS
%doc %{rlibdir}/unknownR/html
%doc %{rlibdir}/unknownR/DESCRIPTION
%{rlibdir}/unknownR/Meta
%{rlibdir}/unknownR/INDEX
%{rlibdir}/unknownR/R
%{rlibdir}/unknownR/NAMESPACE
%{rlibdir}/unknownR/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora