%global packname  cgdsr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.13
Release:          1%{?dist}
Summary:          R-Based API for accessing the MSKCC Cancer Genomics Data Server (CGDS).

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.oo 

BuildRequires:    R-devel tex(latex) R-R.oo 

%description
The package provides a basic set of R functions for querying the Cancer
Genomics Data Server (CGDS), hosted by the Computational Biology Center at
Memorial-Sloan-Kettering Cancer Center (MSKCC).

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.13-1
- initial package for Fedora