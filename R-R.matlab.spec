%global packname  R.matlab
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Read and write of MAT files together with R-to-Matlab connectivity

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.oo 

BuildRequires:    R-devel tex(latex) R-R.oo 

%description
This package provides methods to read and write MAT files.  It also makes
it possible to communicate (evaluate code, send and retrieve objects etc.)
with Matlab v6 or higher running locally or on a remote host.

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
%doc %{rlibdir}/R.matlab/DESCRIPTION
%doc %{rlibdir}/R.matlab/NEWS
%doc %{rlibdir}/R.matlab/html
%{rlibdir}/R.matlab/INDEX
%{rlibdir}/R.matlab/NAMESPACE
%{rlibdir}/R.matlab/help
%{rlibdir}/R.matlab/R
%{rlibdir}/R.matlab/Meta
%{rlibdir}/R.matlab/mat-files
%{rlibdir}/R.matlab/externals

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.2-1
- initial package for Fedora